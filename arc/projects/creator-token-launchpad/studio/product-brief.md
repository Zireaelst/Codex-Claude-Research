Build a creator-community token launchpad on Arc.

Primary user: an existing meme-art or content team that regularly commissions
artists, editors or moderators. The product connects launch and trading with
a visible USDC operating budget, funded assignments, review and payments.

Two immutable launch paths:
1. Start trading now: fixed-supply token, creator-seeded full-range Uniswap v3
   token/USDC pool, atomic permanent founding-LP lock.
2. Launch toward a community target: USDC curve balances, permissionless
   graduation into locked Uniswap v4 liquidity, reviewed immutable rule presets.

The complete initial product MUST offer both working paths, selected by the
creator at launch. Implement in dependency order, but a v3-only release or
disabled v4 selector does not satisfy scope. Never enable incomplete paths.

Default policy: 1B tokens, 18 decimals, minted once; no creator allocation,
transfer tax, blacklist or subsequent minting. Fixed 1% v3 pool fee.
Collected founding-LP fees split 40% creator / 50% community / 10% protocol,
separately per asset. Token fees are not spendable USDC.
Launch fee 5 USDC. Pilot seed range 500–25,000 USDC, subject to validation.
No arbitrary creator-selected hooks, lottery, volume rewards or guaranteed yield.

Arc application accounting uses the USDC ERC-20 interface with 6 decimals.
Native USDC uses 18 decimals and shares the balance. Never double-count it.
Verify dependencies against official sources; missing verification is a gate.

Contracts separate launch, permanent LP custody, fee liabilities, community
budget and work escrow. Founding principal cannot be withdrawn, approved away,
upgraded away or swept. Work payments require explicit reviewer approval;
do not claim that creative quality is verified onchain.

Use the attached specification as the detailed requirements.
Develop contracts and adversarial tests before transaction UI.
Keep mocks and fixtures clearly separated from real chain data.

For every turn: report changed files, tests actually run, failures, assumptions
and unresolved gates. Do not invent deployment addresses or passing results.
Do not deploy, broadcast, spend funds, create wallets, provision credentials,
publish the app or expose secrets. Local tests and read-only inspection only.
Any later deployment requires a separate explicit instruction.
