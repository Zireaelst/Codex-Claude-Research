# Final product decision: both v3 and v4

**Authority:** user's final direction on October 22, 2026. [Original Turkish message](../../research-06/decision-original.md).

The platform will offer **both launch paths**. The token creator selects one during creation. Each path exposes its own compatible feature set. This decision supersedes the historical v3-first-release recommendation, not the underlying security constraints.

| Choice | Canonical path | Creator-facing behavior | Path-specific features |
| --- | --- | --- | --- |
| Start trading now | Immediate Uniswap v3 token/USDC pool | Choose identity, reviewed initial liquidity and fee recipients; launch and lock founding LP atomically. | Immediate final market; fixed pool fee; no curve, migration or v4 hooks. |
| Launch toward a community target | USDC bonding curve, then locked Uniswap v4 pool | Choose identity and an approved bounded rule preset; users trade curve balances until graduation. | Curve progress, target/expiry, partial fills, recovery/refunds, graduation, pool-specific hook presets. |

## Shared product

Creator profiles, discovery, charts, wallet trading, transparent fee collection, creator claims, community USDC budget, funded assignments, submissions, review, contributor payments, portfolio and public completion history.

## Binding boundaries

- One token has one immutable canonical launch path; no later v3/v4 toggle.
- v4 pool hooks never apply to v3 pools. Neither path controls every external pool for its token.
- Contract implementation can proceed in dependency order, but the complete initial launchpad must allow a creator to select either working path. An internal v3 milestone is not the finished product.
- A placeholder, disabled selector or mock v4 flow does not satisfy the two-path release scope.
- Each path must independently pass its security and integration gates. Missing dependencies block that path and therefore the complete release; do not disguise them as implemented features.
- Different feature sets do not mean arbitrary creator code. Use bounded, reviewed presets with explicit compatibility rules.
- Initial v4 presets: standard fixed fee and protected opening surcharge. More advanced volatility fees, external LP incentive campaigns and automatic burns remain separately gated extensions, not claims of completed functionality.
- Proposed seed amounts, splits, curve parameters and fees remain design proposals requiring validation; the user confirmed the two-path scope, not every numeric parameter.
- The current task authorizes documentation and GitHub publication only. It does not authorize implementation, wallet creation, deployment or spending.
