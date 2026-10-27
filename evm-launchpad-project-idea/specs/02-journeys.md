# User journeys and UI specification

## Shared conventions

Network always visible. Token identity is chain ID plus address, not name. Pool identity includes chain and complete pool key. Present quote asset amounts separately from USD estimates. Every transaction shows spender, asset, exact amount, maximum cost, recipient, network, deadline and applicable rules. Never format raw integers through floating-point arithmetic.

### Creator: programmable launch

Discover product → connect wallet → choose supported network → choose Programmable → name/symbol/image/socials → select quote asset and validated curve preset → choose Standard or Advanced profile → choose rule preset or compatible modules → configure creator recipients and optional treasury/referral allocation → review maximum aggregate fees, immutable settings, restrictions and expiry → optional disclosed creator first buy → simulate approvals/launch → sign → receipt → canonical token page → manage metadata, earnings and campaigns.

Defaults must be useful without opening advanced options. Creator first buy uses the same curve and fee rules, is separately shown and capped as specified in economics. There are no undisclosed creator-only launch blocks. Launch failure leaves no partial token, fee payment or initialized pool.

### Creator: instant launch

Same identity/metadata flow → Instant → quote seed and resulting initial FDV → fixed v3 pool fee and immutable recipients → preview full-range founding position and permanent lock → simulate atomic launch → trade page. No hook picker. No curve-progress bar and no migration promise. Explicitly show creator's capital remains in the locked founding LP.

### Trader

Board → filter by network/path/rules → token page → inspect rule summary, creator first buy, holdings concentration and lock evidence → buy or sell → address-specific executable quote → bounded approval → simulation → sign → submitted/replaced/confirmed/failed state → balances/activity updated. On curve graduation between quote and send, fail safely and offer a fresh pool quote; never silently route under different rules.

Show price impact separately from slippage tolerance and fees. Normal sell controls must remain available when buy-only limits apply. RPC unavailable, stale quote, unsupported route and insufficient gas are distinct errors. Do not silently switch the user's network or bridge assets.

### Existing-token pool opener and LP

Enter token address → inspect token code/behavior and external controls → choose allowlisted quote asset → receive external-price reference if available, explicitly non-authoritative → enter seed amounts and implied price → select compatible pool-only rules → confirm community-pool designation and opener fee → deposit both assets atomically → receive removable NFT → add liquidity, collect fees, reduce or exit own position. No ordinary LP action can touch founding locked positions of launchpad-issued tokens.

A pool can exist alongside other pools; UI lists them without merging liquidity or pricing. Opener is never labeled token creator solely because they opened a pool.

### Creator earnings and community

Dashboard shows pending collection, accrued claimable balances and paid amounts by asset. Harvesting LP fees does not mean converting them into USDC. Optional community allocation → Treasury dashboard → fund job with quote asset → reserve budget → assign contributor → submit content hash/URI → independent reviewer accepts/rejects → contributor claims accepted payment. Details and deterministic timeout exits are specified in 04-lifecycles. No promise that onchain settlement verifies creative quality.

### Rewards participant

Read reward asset, funded budget, rate, eligibility and end time → stake if using Lock & Earn → see accrued and reserved balances → claim → unstake principal. External LP participants see full-range-only eligibility, staked-NFT custody and claim history. No fixed reward per buy: splitting/wash trades must not print subsidies.

## Screens and minimum content

| Screen | Required content |
|---|---|
| Board | Search by address/name; new/active/near graduation/graduated; network/path; explicit sponsored labels; stale-data indicator |
| Launch wizard | Identity, economics, rules, earnings, final review; drafts keyed by network; contract-equivalent validation |
| Token terminal | Chart, trade ticket, status, curve progress when relevant, rules, supply/holders, LP lock, fees, activity, verified links |
| Pool terminal | Complete pool key, opener badge, seed reference, depth, LP positions, rules and add/remove controls |
| Rules inspector | Module addresses/code hashes, version, parameters, fee ceilings, duration, trusted routers and bypass limits |
| Earnings | Collect versus claim, each currency, recipients, payout history, failing-recipient isolation |
| Campaigns | Funding, staking, rewards, deadlines, unreserved balance and closure |
| Community | Available/reserved/claimable budgets, work submissions, reviewer actions and deadlines |
| Portfolio | Curve entitlements, liquid tokens, staked tokens, LP NFTs, fee/reward claims across networks without fake aggregation |
| Blueprint catalog | Immutable template version, compatibility, author, inspection link, usage counts defined precisely |
| Admin console | New-launch pause, quote/module allowlist proposals, moderation, evidence links and audit history |

## UI behavior and accessibility

Responsive mobile trading and keyboard-operable forms. Amounts and warnings cannot rely on color alone. Handle loading/empty/error/offline states. Drafts store no signatures or secrets. Sanitized metadata and proxied images; forbid executable HTML and arbitrary remote fetches from user URLs. Social sharing uses canonical chain/address links and displays path and material restrictions. Moderation may hide content from discovery but never blocks a user's contract withdrawal or claim.

Comments and reactions are optional social surfaces; if included, use wallet-authenticated posting, rate limits, reports and explicit removal reasons. Do not reward engagement solely by raw counts.
