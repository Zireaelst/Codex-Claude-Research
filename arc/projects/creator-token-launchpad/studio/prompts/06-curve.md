Implement only the approved USDC curve and internal curve balances, with a
separate reference model. Derive pricing, backing reserve and graduation
parameters together. Separate trading fees from backing. Support buy/sell
slippage, exact target partial fills, expiry and pro-rata refund snapshots.

Curve balances are not transferable ERC-20 tokens; expose that distinction.
No privileged creator buys. Test dust cycling, reserve solvency, arbitrary
buy/sell sequences, expiry boundaries and refund conservation. Keep graduation
behind an interface until its implementation is reviewed. No deployment.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
