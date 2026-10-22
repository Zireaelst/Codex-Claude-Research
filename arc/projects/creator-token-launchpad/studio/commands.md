# CLI commands (not executed)

The CLI was unauthenticated during research. Authenticate through the official interface outside this archive; never paste credentials into prompts. Run one command at a time from this directory after authorizing implementation.

```bash
# Run from this studio directory after separate authorization to start building.
# Inspect each turn result before executing the next command.
arc-studio run --session arc-creator-launchpad --output json --file product-brief.md --file specification.md --prompt-file prompts/01-model.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/02-token-registry.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/03-v3-launch-lock.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/04-fee-treasury.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/05-work-escrow.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/06-curve.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/07-v4-graduation.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/08-hook-presets.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/09-contract-adversarial.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/10-app.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/11-indexer.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/12-integration.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/13-release-review.md
```

Each prompt is below 10,000 characters. The longer specification is attached with `--file`, not passed as prompt text. Inspect `status`, actual test outputs and unresolved gates; `needs_input`, `error` and `budget_exceeded` do not mean completion.

## Export

```bash
arc-studio ls --session arc-creator-launchpad
arc-studio pull --session arc-creator-launchpad --out ./studio-export --dry-run
arc-studio pull --session arc-creator-launchpad --out ./studio-export --paths "contracts/**"
```

Inspect actual paths and repeat for frontend, indexer, tests, ABIs, compiler settings and lockfiles. Do not export credential files. Mainnet deployment and public hosting occur outside Studio after independent review and separate authorization.
