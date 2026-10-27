# Rules engine and full-product catalog

## Enforcement domains

A Uniswap v4 swap hook is a contract called by the PoolManager at defined lifecycle points. A curve rule is enforced by our curve code. A token transfer rule is enforced by our token contract. An offchain webhook is a notification, never an onchain enforcement mechanism. Do not call these interchangeable hooks.

Use one audited dispatcher implementation per supported hook family, with immutable per-pool configuration and a bounded module list. Registry entries include module ID, version, address, runtime-code hash, allowed domains, conflict groups, config schema/hash, asset compatibility, gas budget and authority policy. Maximum selected modules: six. No arbitrary delegatecall, module upgrades or user-supplied executable callbacks. Prefer trusted fixed implementation calls with explicitly bounded return values; hold payout funds in a separate accounting vault.

Modules receive authenticated trade context: chain, pool/launch, phase, currency direction, actual executed amounts, caller and optional verified beneficiary. Router must bind actor/recipient to msg.sender or a valid nonce/deadline EIP-712 authorization. Never accept an unsigned trader field from hookData. For direct/aggregator routes where actor cannot be verified, economic fees still apply; identity-based rewards/referrals are unavailable, never spoofable. A rule requiring identity must explicitly reject that route or disclose its limited reach.

## Rule catalog (all included unless explicitly excluded)

| ID | Rule | Domains | Parameters and constraints | Funding / honest limitation |
|---|---|---|---|---|
| M01 | Opening buy cap | curve + own v4 pool | Optional, 0–10 minutes after each opening; transaction aggregate max 0.1–2% of S | Does not identify people; split wallets/transactions bypass wallet fairness |
| M02 | Opening fee decay | curve + pool | 0–200 bps surcharge, linear to zero within 10 minutes; subject to total ceiling | Creator bucket; sells unaffected; quote includes current value |
| M03 | Dynamic LP fee | pool only | Base 30 bps default, max 100; fee rises by floor((max-base)*min(quoteNotional/depth,1)); actual formula uses fixed-point full-range depth | Reject if trusted depth unavailable; no claim of eliminating MEV |
| M04 | Buy burn | pool only | 0–100 bps of purchased token output, fee ceiling includes it | Burn actual tokens through supply-reducing primitive, not merely dead-address accounting |
| M05 | Creator allocation | earnings | Up to five team recipients, optional treasury share; frozen | Allocates existing creator income, no new trade fee |
| M06 | Referral | verified curve/router buys | Up to 20% of creator income; attribution per signed trade; no permanent forced binding | No self-referral; Sybil self-referral remains economically possible |
| M07 | Funded Lock & Earn | separate staking vault | Fixed end/time-rate, exact funding, reward-per-share; duration 1–90 days | No rewards based simply on buying; principal and reward liabilities separate |
| M08 | External LP rewards | existing-token pools | Stake eligible full-range NFT; time-weighted liquidity; same funded accounting | Raw liquidity is comparable only inside same pool/range; no cross-pool leaderboard |
| M09 | Auto-LP | separate funding vault + pool | Opt-in portion <=20% of creator bucket; permissionless compound every >=30 minutes, <=5% budget per call | Uses historical-price protection, minimum output/liquidity, no arbitrary calldata; no unsafe compound without history |
| M10 | Buyback and burn | separate funding vault + pool | <=20% creator bucket; same cadence/cap as M09; conflicts with M09 | Purchased own token actually burned; no price-support guarantee |
| M11 | Temporary max-wallet | Advanced token only | Cap 1–5% S, duration <=24h after graduation; immutable exemptions | Transfer checks, partial claims, smart-wallet/aggregator incompatibility exposed; not Sybil-proof |
| M12 | Temporary allowlist | Advanced token only | Immutable Merkle root, expires <=24h after graduation; cannot block entitlement refund | Recipient eligibility, not anonymity or KYC; no root change; conflicts with M11 |

M01 aggregates within one transaction where hook execution supplies reliable transaction-scoped storage. Cross-transaction per-block fairness is not promised. Local tests must cover repeated swaps and router callbacks. Duration uses timestamps, not a cross-chain assumption about block duration.

M03 must define quoteNotional from actual specified-side exact-input amounts; for token-in sells use conservative pre-swap price conversion. Price manipulation can affect fee; ceiling bounds damage. If a token's behavior or route prevents an honest quote, reject module selection. Do not let an optional fee oracle turn into a global exit dependency.

M04 is pool-only. Curve-phase burn is excluded because retiring purchased entitlements changes the reserve/refund denominator. Never burn the fixed founding LP allocation or user entitlement inventory. An external token must support a verified supply-reducing burn action on tokens actually received by the module; otherwise M04 is unavailable. Sending to a dead address alone must be labeled removed-from-circulation, not a totalSupply reduction; that alternative is not this module.

M09/M10 funding lifetime: fixed end time selected at launch, default 30 days, allowed 1–365 days. After end, new creator-income allocations go directly to the original creator bucket; no new maintenance spending is allowed. Uncommitted budget returns only to that precommitted bucket, never a caller-selected owner; earned liabilities remain claimable. Permanently locked Auto-LP positions remain locked after end.

M09/M10 execution: derive 30-minute price reference from our observation module with >=3 observations spanning >=30 minutes; spot deviation <=200 bps; disable execution on insufficient/stale observations, but keep swaps/claims working. Slippage <=100 bps, price impact <=100 bps, caller supplies bounded minOut and deadline checked against reference. Rewards to caller, if any, must come from a fixed separately funded keeper budget, never principal. Each operation uses a dedicated pool ID and immutable asset pair. No newest-pool lookup. Auto-LP positions are permanently locked; buyback vault funds do not become LP principal.

## Presets

Standard: fixed fees, M05 optionally configured, no opening rules. Protected: M01 + M02 + M05. Creator: M05 + M06 + M07. Liquidity Builder: M05 + M09. Burn: M04(pool-only) + M05 + M10. Advanced Access: M12 + M05; or Advanced Holding: M11 + M05. All presets remain editable only within registry-validated compatible parameters before launch.

## Conflict rules

M09 and M10 cannot coexist; their funding is a split of creator income, never an extra levy. M11 and M12 cannot coexist. M11/M12 unavailable for v3 and external tokens. M08 only external-token pools. M03 cannot coexist with another LP-fee controller. M02 plus service/LP/burn must satisfy aggregate ceiling at worst time/size. M06 unavailable without authenticated identity route. No duplicate modules or repeated conflict groups. Locked launch LP earns normal LP fees; external LP campaigns cannot redirect its principal or entitlement.

## Advanced transfer profile

Use a separate audited token implementation, selected at launch, not an upgrade to a standard token. Curve-phase tokens remain in custody for both profiles. After graduation M11 or M12 applies to all non-exempt receives until sunset. Protocol custody addresses necessary for settlement are immutable exemptions; every exemption is displayed. External pools/contract intermediaries may bypass intended economic limits via exemptions or pooling: do not claim global market control. Token checks cannot block full withdrawal of an unrelated user's external LP; if that guarantee cannot be proven for a route, label the route unsupported and prevent that pool configuration. Claims may be split; no expiration of rights. After sunset token transfers are standard permanently. No blacklist, sell freeze, rebasing, future mint or changeable exemptions.

## Existing-token pools

Allow M03, M04 only with compatible burnable token capability (otherwise reject, do not fake a burn), M05, M06 and M08. No M11/M12, no assumptions of S=1B, and no automatic seizure of external token holders' rights. Token addresses and runtime capabilities must be validated. Limit creator service fee as economics specifies. Do not label pool opener as token team without separate evidence.

## Registry administration and emergency policy

Registry may disable a module for NEW launches after discovery of a defect. Existing launches are never silently reconfigured. Optional fund-moving maintenance operations M09/M10 may be paused by a disclosed emergency multisig; this does not stop swaps, earned claims or principal exits. After campaign end, uncommitted maintenance budget returns to its precommitted funding owner; accrued claims remain. No global kill switch that unexpectedly changes existing economic rules. If a swap-critical immutable module is defective, report its risk: absent a disclosed recovery mechanism, there may be no safe patch. Audit before activation.

## Deliberate exclusions

Nth-buy pots, last-buyer jackpots, sell locks, arbitrary changing rivals, price guarantees, game-score holding unlocks, platform-token buybacks and stock-market hours are not target features. They are not needed to satisfy the intended product and introduce manipulation, exit or legal complexity. Never silently add them because a competitor lists them. Blueprint catalog contains parameter templates of approved modules, not an arbitrary-code marketplace; templates have no royalty in this spec.
