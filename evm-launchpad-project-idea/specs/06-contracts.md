# Contract boundaries and data flow

## Principles

Immutable per-launch economic contracts. Versioned factories deploy new implementations for new launches; old positions remain unchanged. Infrastructure administration cannot withdraw principal or rewrite recipients. Use upstream interfaces/types, not invented lookalikes. Pin compiler/EVM targets and deployment provenance.

## Components

| Component | Owns / authority | Responsibilities; prohibited behavior |
|---|---|---|
| LaunchRegistry | immutable records; authorized per-launch controller | Path, token, creator, config hash, canonical pool/locker and state; no global launcher can mutate another controller's launch |
| TokenFactory | allowlisted path factories | Deploy fixed supply directly to authorized custody, not arbitrary user-provided custody; deterministic ID chain/factory/creator/salt/path |
| StandardToken / AdvancedToken | no mint owner | Initial supply only; burn caller-owned tokens only (no privileged burn of other holders); Advanced checks separately specified |
| CurveFactory / CurveSale | curve backing + token inventory | Atomic launch, entitlement trading, accrual, pending graduation, retry and refunds |
| V3Launcher | transient seed custody | Canonical v3 create/init/mint and locker deployment; all-or-nothing |
| V3Locker | one founding NFT | Fee harvest and distribution only; no approve, transfer, decreaseLiquidity or arbitrary external call |
| GraduationExecutor | transient assets | Only registered sale/config; canonical v4 init/mint/settlement; reject arbitrary lookalike sales |
| V4Locker | one founding NFT | Zero-liquidity-delta fee collection, actual payout accounting; permanent principal custody |
| HookRegistry / CompositeHook | approved code metadata / per-pool state | CREATE2 permission validation, immutable config registration, bounded rule dispatch |
| ExistingPoolFactory | transient assets | Dedicated hook config/pool key, two-sided mint to depositor, token compatibility validation |
| LaunchRouter / Lens | no persistent custody / read simulation | Authenticated identity, exact-input execution, quote consistency; explicit unsupported routes |
| FeeVault | asset-specific liabilities | Authorized accrual backed by actual transfer, independent pull claims, no reserve borrowing |
| DustVault | bounded launch residues | Nonwithdrawable principal residues, public accounting; no revenue treatment |
| RewardVault / LPRewardVault | stake principal, funded rewards | Time-weighted distribution, safe principal exit and perpetual earned claims |
| MaintenanceVault | separately allocated fee funds | Auto-LP OR buyback; observation guards, bounded execution, no arbitrary swap targets |
| CommunityTreasury / WorkEscrow | available/reserved/claimable budgets | Optional funded work lifecycle; reviewer authority explicit |
| BlueprintRegistry | immutable template specs | Publish reviewed module combinations, disable discovery only; no code execution |

## Proposed interface contract between work packages

These are application ABI design requirements, not purported upstream ABIs. Encode structs/types in shared ABI package and generate clients; do not copy signatures by hand.

- `launchCurve(LaunchConfig, maxLaunchFee, creatorBuyBudget, minCreatorEntitlements, deadline)` returns launchId/token/sale. LaunchConfig includes creator=authenticated caller, metadata hash, quote, economics preset hash, profile, modules/configs and recipient shares.
- `launchInstant(InstantConfig, seedQuote, maxLaunchFee, minLiquidity, deadline)` returns launchId/token/pool/locker. Creator attribution requires caller or typed signed authorization.
- `buy(launchId, maxQuoteIn, minEntitlementsOut, recipient, deadline)` and `sell(launchId, entitlementsIn, minQuoteOut, recipient, deadline)` execute only own/delegated entitlements, never arbitrary balances.
- `graduate(launchId)` uses immutable onchain configuration only; `activateRefund(launchId)` checks exact state/time; `claimRefund(launchId, entitlementAmount, recipient)` burns caller's balance.
- `claimTokens(launchId, amount, recipient)` permitted only after GRADUATED and transfer-profile validation.
- `harvestFees(positionId)` may be permissionless but destinations frozen. `claim(asset, amount, recipient)` spends caller's accrued liability only.
- `createExistingPool(PoolConfig, amountTokenMax, amountQuoteMax, minLiquidity, deadline)` validates pool key, token behavior, approved modules, fee cap and exact received amounts.
- `quoteTrade(TradeRequest)` returns gross/net, breakdown, expected/max fee, execution limits, phase, configHash, blockNumber/hash, expiry and rule failure data. For non-view simulation use eth_call, never public transaction.

## V4 execution constraints

PoolKey uses canonical Currency and IHooks types, sorted by address. Pool ID via canonical library. Read state through official StateLibrary/extsload or StateView. Import Actions constants; initialization is not an invented modifyLiquidities action. Implement actual Permit2/settlement required by pinned periphery, with amount bounds, short expiration and allowance revocation. Verify token movements; a mock that accepts action bytes without settlement is insufficient.

Hook permission bits must match the deployed CREATE2 address and actual callbacks. The beforeInitialize sender may be PositionManager rather than end user: trusted sender alone is NOT sufficient if anyone can invoke it. Require registered exact key + expected price + active executor authorization context, and test malicious direct and periphery initialization before legitimate graduation. Close registration/initialization windows atomically. Register separate launch identities to prevent cross-launch replay.

Additional liquidity in launch pools is allowed only as full-range positions owned by their depositors and removable by them; those positions are never labeled founding locked LP. Enforce the range restriction in the actual add-liquidity hook callback. The founding locker accepts only its expected NFT and cannot manage unrelated depositor NFTs.

LP mint calculation uses actual available assets after authorized transfer from CurveSale. Verify NFT ownership, liquidity, complete pool identity, ticks and expected amounts before declaring success. Fee collection uses supported zero-delta liquidity action plus take action, never a custom COLLECT_ALL selector. Check pool position liquidity before/after and measure actual token receipts; not a mock liquidity getter returning a constant.

## Money flow

Curve buyer gross → actual net backing in CurveSale + fee transferred to FeeVault + unused input refunded. FeeVault accrual without transfer is forbidden. Graduation backing + LP token reserve → real AMM settlement; bounded leftovers → DustVault; buyer token inventory stays for claims. Post-graduation swap service fees → FeeVault; AMM LP fees remain in position until harvested. Treasury/referral receive allocations from the creator bucket, never from backing reserves.

Treasury spending and reward funding are separate authorized flows. Failed recipient claim must not block others. With USDC blacklist/freeze, preserve liability and permit owner-selected recipient where the token permits; do not promise protocol can override token issuer controls.

## Events

Emit LaunchCreated(configHash/path/profile/quote), CurveTrade(gross/net/fee/refund/entitlement), GraduationPending, GraduationAttemptFailed, Graduated(poolId/locker/liquidity/dust), RefundActivated(F/Q), RefundClaimed, TokensClaimed, FeesAccrued, FeesHarvested, FeeClaimed, RuleConfigRegistered, CampaignFunded/Claimed, JobStateChanged and MetadataUpdated. Use canonical upstream Swap events for actual pool amounts; do not double-count a routed swap as two trades. Events expose public economics; no privacy claims.
