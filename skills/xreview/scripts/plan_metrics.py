#!/usr/bin/env python3
"""Describe plan lengths; activate project targets only from curated references."""

import argparse
import hashlib
import json
import math
import re
import statistics
from pathlib import Path


def measure(text):
    fenced_words = 0
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is None and match:
            fence = match[1]
        elif fence and match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
            fence = None
        elif fence:
            fenced_words += len(line.split())
    return {"words": len(text.split()), "bytes": len(text.encode()),
            "fenced_code_words": fenced_words}


def distribution(records):
    values = [r["words"] for r in records]
    if not values:
        return {"n": 0, "q1": None, "median": None, "q3": None}
    q1, median, q3 = (statistics.quantiles(values, n=4, method="inclusive")
                      if len(values) > 1 else [values[0]] * 3)
    return {"n": len(values), "q1": q1, "median": median, "q3": q3}


def unique_records(paths):
    records = []
    seen = set()
    for path in sorted(set(paths)):
        text = path.read_text()
        digest = hashlib.sha256(text.encode()).hexdigest()
        if digest in seen:
            continue
        seen.add(digest)
        records.append({"path": str(path), "sha256": digest, **measure(text)})
    return records


def report(plans, plan=None, accepted=None):
    root = plans.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("--plans must be a directory")
    history = unique_records(p for p in root.rglob("*.md") if not p.is_symlink())
    references = []
    if accepted:
        paths = json.loads(accepted.read_text())
        if not isinstance(paths, list) or any(not isinstance(p, str) for p in paths):
            raise ValueError("Accepted references must be a JSON list of relative plan paths")
        selected = []
        for relative in paths:
            path = (root / relative).resolve(strict=True)
            if Path(relative).is_absolute() or not path.is_relative_to(root) or path.suffix != ".md":
                raise ValueError("Reference must be a Markdown path within --plans: " + relative)
            if plan and path == plan.resolve():
                raise ValueError("Current plan cannot calibrate its own target")
            selected.append(path)
        references = unique_records(selected)
    stats = distribution(references)
    active = {"min_words": 600, "max_words": 1500, "source": "experimental-default"}
    if stats["n"] >= 8:
        active = {"min_words": math.floor(stats["q1"]), "max_words": math.ceil(stats["q3"]),
                  "source": "explicitly-curated-project-references"}
    result = {"quantile_method": "inclusive", "historical_words": distribution(history),
              "historical_plans": history, "reference_words": stats,
              "reference_plans": references, "active_target": active,
              "limitations": ["Length is not work size or exposition adequacy.",
                              "Historical quartiles are descriptive, not quality certification.",
                              "No scalar weights or words-per-obligation rule are validated."]}
    if plan:
        current = measure(plan.read_text())
        words = current["words"]
        current["position"] = ("below" if words < active["min_words"] else
                               "above" if words > active["max_words"] else "inside")
        current["length_followup"] = {"below": ["skip-plan", "expand-guidance"],
                                      "above": ["split-work", "trim-detail"],
                                      "inside": ["assess-work-size-and-exposition"]}[current["position"]]
        result["current_plan"] = {"path": str(plan), **current}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plans", required=True, type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--accepted", type=Path)
    args = parser.parse_args()
    try:
        result = report(args.plans, args.plan, args.accepted)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
