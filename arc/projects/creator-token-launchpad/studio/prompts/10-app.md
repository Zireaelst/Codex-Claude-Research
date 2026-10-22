Build the dual-path application screens against generated typed ABIs and explicit
data interfaces: discovery, launch wizard, token/trade page, creator dashboard,
community budget/workspace, contributor workspace and portfolio.

Use user-facing launch language. Both v3 and v4 must be selectable once their readiness gates pass. An unavailable path blocks the complete release; do not simulate it.
Implement wallet/network states, approval explanations, slippage controls,
transaction progress, retries and clear liquidity-lock disclosures.

Separate fixtures from real data. Never show invented TVL, trades, claims or
successful transactions. Make available USDC visibly different from estimated
or token-denominated fees. Do not deploy or publish.

Include frontend requirements for curve trading, target progress,
immutable rule summaries, graduation retries, token claims and refunds.
Keep curve balances visually distinct from transferable tokens.

Show price impact, fee treatment, target partial fills, expiry and the exact
meaning of pro-rata refunds before users sign. Display which rules apply
only to the canonical v4 pool. Specify UI acceptance cases covering successful
graduation, failed graduation recovery and expired-curve redemption.
Do not enable the path in production or deploy any contracts.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
