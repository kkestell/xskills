"""Local deterministic regressions; no model calls or repository fixtures needed."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan_metrics.py"
SPEC = importlib.util.spec_from_file_location("plan_metrics", SCRIPT)
metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metrics)


class MeasurementTests(unittest.TestCase):
    def test_whitespace_and_utf8_bytes(self):
        text = "café\talpha\n\nbeta  gamma"
        self.assertEqual(metrics.measure(text), {
            "words": 4, "bytes": len(text.encode("utf-8")), "fenced_code_words": 0,
        })

    def test_fences_count_content_not_delimiters(self):
        text = "intro\n```python\na b\n```\n~~~\nc d e\n~~~\nend"
        self.assertEqual(metrics.measure(text)["fenced_code_words"], 5)
        self.assertEqual(metrics.measure(text)["words"], len(text.split()))

    def test_shorter_or_other_fence_does_not_close(self):
        text = "````python\na b\n```\n~~~\nc\n````"
        self.assertEqual(metrics.measure(text)["fenced_code_words"], 5)

    def test_empty_and_singleton_distributions(self):
        self.assertEqual(metrics.distribution([]), {
            "n": 0, "q1": None, "median": None, "q3": None,
        })
        self.assertEqual(metrics.distribution([{"words": 12}]), {
            "n": 1, "q1": 12, "median": 12, "q3": 12,
        })


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plans = self.root / "plans"
        self.plans.mkdir()
        self.current = self.plans / "current.md"
        self.manifest = self.root / "references.json"

    def write_plan(self, path, words):
        path.write_text(" ".join([path.stem] * words), encoding="utf-8")
        return path

    def references(self, counts):
        paths = [self.write_plan(self.plans / f"ref-{i}.md", count)
                 for i, count in enumerate(counts)]
        self.manifest.write_text(json.dumps([p.name for p in paths]))
        return paths

    def test_default_band_is_inclusive_and_followups_are_advisory(self):
        for words, position, followup in [
            (599, "below", ["skip-plan", "expand-guidance"]),
            (600, "inside", ["assess-work-size-and-exposition"]),
            (1500, "inside", ["assess-work-size-and-exposition"]),
            (1501, "above", ["split-work", "trim-detail"]),
        ]:
            with self.subTest(words=words):
                self.write_plan(self.current, words)
                result = metrics.report(self.plans, self.current)
                self.assertEqual(result["active_target"], {
                    "min_words": 600, "max_words": 1500,
                    "source": "experimental-default",
                })
                self.assertEqual(result["current_plan"]["position"], position)
                self.assertEqual(result["current_plan"]["length_followup"], followup)
                self.assertNotIn("actions", result)
                self.assertNotIn("verdict", result)

    def test_history_does_not_activate_project_target(self):
        self.references(range(10, 90, 10))
        result = metrics.report(self.plans)
        self.assertEqual(result["historical_words"]["n"], 8)
        self.assertEqual(result["reference_words"]["n"], 0)
        self.assertEqual(result["active_target"]["source"], "experimental-default")

    def test_seven_curated_references_keep_default(self):
        self.references(range(10, 80, 10))
        result = metrics.report(self.plans, accepted=self.manifest)
        self.assertEqual(result["reference_words"]["n"], 7)
        self.assertEqual(result["active_target"]["source"], "experimental-default")

    def test_eight_curated_references_use_inclusive_quartiles(self):
        self.references(range(11, 19))
        result = metrics.report(self.plans, accepted=self.manifest)
        self.assertEqual(result["reference_words"], {
            "n": 8, "q1": 12.75, "median": 14.5, "q3": 16.25,
        })
        self.assertEqual(result["active_target"], {
            "min_words": 12, "max_words": 17,
            "source": "explicitly-curated-project-references",
        })

    def test_duplicate_text_cannot_reach_reference_minimum(self):
        paths = self.references(range(10, 80, 10))
        duplicate = self.plans / "duplicate.md"
        duplicate.write_text(paths[0].read_text())
        self.manifest.write_text(json.dumps([p.name for p in paths] + [duplicate.name]))
        result = metrics.report(self.plans, accepted=self.manifest)
        self.assertEqual(result["reference_words"]["n"], 7)
        self.assertEqual(result["historical_words"]["n"], 7)
        self.assertEqual(result["active_target"]["source"], "experimental-default")

    def test_current_plan_cannot_set_its_own_target(self):
        self.write_plan(self.current, 20)
        self.manifest.write_text(json.dumps([self.current.name]))
        with self.assertRaisesRegex(ValueError, "cannot calibrate its own target"):
            metrics.report(self.plans, self.current, self.manifest)

    def test_manifest_requires_relative_markdown_paths_within_plans(self):
        outside = self.write_plan(self.root / "outside.md", 10)
        text_file = self.write_plan(self.plans / "not-markdown.txt", 10)
        for entry in [str(outside), "../outside.md", text_file.name]:
            with self.subTest(entry=entry):
                self.manifest.write_text(json.dumps([entry]))
                with self.assertRaisesRegex(ValueError, "Markdown path within"):
                    metrics.report(self.plans, accepted=self.manifest)

    def test_manifest_requires_list_of_strings(self):
        for value in [{"path": "ref.md"}, [1], None]:
            with self.subTest(value=value):
                self.manifest.write_text(json.dumps(value))
                with self.assertRaisesRegex(ValueError, "JSON list"):
                    metrics.report(self.plans, accepted=self.manifest)

    def test_cli_outputs_repeatable_json(self):
        self.write_plan(self.current, 650)
        command = [sys.executable, str(SCRIPT), "--plans", str(self.plans),
                   "--plan", str(self.current)]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)
        result = json.loads(first.stdout)
        self.assertEqual(result["current_plan"]["words"], 650)
        self.assertEqual(result["current_plan"]["position"], "inside")


if __name__ == "__main__":
    unittest.main()
