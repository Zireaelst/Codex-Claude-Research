# Copy/paste coding-agent prompt

Read the entire `evm-launchpad-project-idea/` directory from this repository, starting with README.md and AGENTS.md, then every numbered spec, the acceptance matrix and IMPLEMENTATION_PLAN.md. This is the complete context; do not depend on access to the original chat.

Build a NEW end-to-end EVM meme and creator token launchpad according to this specification. Do not continue the old Arc project. V4 curve-to-pool programmable launch is primary; instant V3 and existing-token V4 pools are required separate lanes. No Arc Studio/Circle/Arc gas dependency. Base is the initial integration reference; network manifests must allow independent verified EVM deployments.

First produce a concise requirement-to-work-package map and dependency check. Choose and pin a compatible toolchain. If a required rule conflicts with an upstream behavior, document the exact conflict and proposed resolution before changing economics. Do not ask me to restate decisions already made in this package.

After implementation is explicitly authorized, create/use the authorized new application repository, copy this spec into docs/product, and execute the work packages in order. Use test-first accounting/state-machine development, real upstream Uniswap v3/v4/Permit2 integration, generated ABI clients, frontend, API, indexer and operational tests. Local mock fixtures are allowed for unit tests only. Never call them integration proof.

Maintain STATUS.md with completed requirement IDs, actual commands/results, evidence and remaining blockers. Make meaningful commits; do not manufacture commit count. Preserve both launch paths and full required scope. Do not stop after a token factory, mocked UI or one launch path.

Do not deploy publicly, spend funds, issue real tokens, publish production services or provision paid resources without explicit permission. Never request or expose keys/tokens in chat. You may build and test locally once authorized. Ask only for a genuinely indispensable product decision or external authorization; continue independent work when a dependency is blocked.

Deliver runnable product source, repeatable setup, real integration evidence, acceptance-matrix status and truthful security limitations. No claim of audit, mainnet readiness, network deployment or actual adoption without corresponding evidence.

## How the owner uses this

Provide the repository URL plus this file or the whole folder to the coding agent. Explicitly add the desired new application repository and whether local implementation is authorized. The research archive must remain documentation-only; the agent should not scaffold application code into Arc or Stellar folders. Live deployment permission is separate from permission to implement locally.
