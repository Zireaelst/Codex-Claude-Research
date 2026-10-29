# Validation results — 2026-10-29

## Executed

- `python3 -m unittest discover -s base-agent/tests -v`: seven tests passed. Tests cover dry-run with no target creation, invalid client, malformed managed marker, conflicting skill refusal before writes, no MCP/global configuration change, preserving instructions with idempotent second install, and symlink escape refusal.
- Actual CLI installation into an isolated local fixture copied both client skills and instruction pointers. Second apply returned an empty changes list. Doctor reported executable/file presence and explicitly left network/credentials/readiness unverified.
- Official skill-creator `quick_validate.py`: **Skill is valid!** Default Python lacked PyYAML; validation succeeded after installing PyYAML 6.0.3 in a project-local temporary virtual environment. The installer itself is standard-library only.
- Direct Base Docs MCP initialize/list/search smoke test passed; see [source-review](source-review.md). This is not client integration testing.

## Behavioral checks

An independent baseline agent without the new skill already handled three pressure scenarios correctly: experimental-versus-mainnet capabilities, HTTP success versus venue fill, and copied instructions versus installed tools/deploy permission. There was no observed baseline behavioral failure, so no measured skill-induced improvement is claimed.

An independent forward reviewer read the package and simulated new-app setup/deployment and ambiguous prediction submission. It kept actual tool capability separate from guidance, retained both product profiles, required source-spec access for launchpad implementation, selected a real upstream contract harness/read-only venue spike as first work, and reconciled ambiguous orders rather than blindly re-signing. It also ran the seven tests successfully. Review found no critical installer defect; it noted the missing results file and path assumptions for standalone downloads. This record and explicit standalone-path instructions resolve those findings.

These are bounded instruction-following evaluations, not deployed app tests, security audits, venue execution tests, or proof of compatibility with every Codex/Claude version. No wallet was funded and no contract was deployed.

## Reproduce

From the research repo root:

```bash
python3 -m unittest discover -s base-agent/tests -v
python3 base-agent/scripts/setup.py install --target /tmp/base-agent-example-app --client both
```

Use a fresh fixture directory for `--apply` verification. Review proposed files first. Client MCP activation must be checked separately in the destination session with a real documentation search/read.
