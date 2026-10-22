Implement the v3 launcher and permanent founding-liquidity locker. Launch
must atomically create the token, initialize the expected token/USDC pool,
mint full-range liquidity directly into custody, register its position and
fee policy, and return permitted USDC dust.

Use ERC-20 USDC accounting. Reject unexpected existing pool state and unintended
native value. Expose only narrowly scoped fee collection; prohibit position
transfers, approvals, principal decreases, upgrades and arbitrary execution.

Test token ordering, 6/18 decimal scaling, slippage, initialization griefing,
reverts at every step and all possible principal escape paths. Label local
Uniswap fixtures separately from canonical Arc integration tests. No deployment.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
