# Instructions for the implementing agent

1. Read README and every numbered specification before changing implementation. Read the source evidence notes; competitor marketing is not a security guarantee.
2. This is a new EVM product. Never inherit the Arc application or its supposedly passing tests as a trusted starting point. Do not modify the research archive's Arc or Stellar directories.
3. Use a new application repository when authorized. These documents stay the specification; code belongs in that repository. No Studio dependency is required.
4. Preserve both canonical launch paths. V4 is the primary UX and first protocol integration to prove. V3 is required for the complete product. Existing-token pools are a separate product lane.
5. Implement full work packages in dependency order. Track requirement IDs, test commands, actual output, commits and blockers in STATUS.md. Do not manufacture test counts or split commits solely to reach a number.
6. Use test-first development for accounting and state changes. Real upstream protocol integration is mandatory. Interface-compatible mocks cannot satisfy integration gates.
7. Pin upstream revisions, dependency lockfiles and compiler settings. Compile upstream bytecode using its required compiler; do not rewrite upstream pragmas just to fit a local project.
8. Never invent deployed addresses, fees, usage, audit badges, network availability or API responses. Example fixtures must be explicitly marked and cannot enable transactions.
9. No secret values in code, prompts, logs, screenshots, commits or chat. Use environment variable names only. Unsigned API responses must never require server custody of user keys.
10. No mainnet/testnet broadcasting, spending, external deployment or production publication without explicit owner authorization for that action. Local EVM tests are permitted once implementation is authorized.
11. Do not add arbitrary delegatecall modules, mint authority, principal withdrawals, hidden sell blocks, unlimited fee setters or a platform token.
12. Document actual trust and bypass boundaries. Pool hooks do not govern external pools. A source-verified contract is not an audited contract. Simulations are not execution guarantees.
13. Stop only the affected work package when an external dependency is genuinely unavailable. Record a reproducible blocker and continue independent authorized work. Never downgrade acceptance requirements to make the status green.
14. Never use transaction volume alone as proof of community growth. Distinguish own-pool activity, external activity, fees, realized payouts and wash-trading indicators.
15. Final delivery must include runnable app, backend/indexer, contracts, tests, manifests, deployment preparation, operational runbooks and truthful known limitations. A design-only output is not implementation completion.
