.PHONY: install

# Install the suite together; the skills share workflow and planning references.
install:
	npx --yes skills add ./skills --global --yes \
		--skill xplan xwork xreview xtask --agent claude-code codex opencode
