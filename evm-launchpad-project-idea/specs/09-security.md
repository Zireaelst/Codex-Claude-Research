# Security model, authorities and operational boundaries

## Adversaries and trust

Assume malicious creator, sniper/bundler, quote manipulator, fake token, compromised web/API, spoofed router, malicious recipient, sybil users, dishonest contributor/reviewer, RPC outage and chain reorg. No claim of Sybil resistance, anonymity, risk-free liquidity or guaranteed sellability under all chain/token failures. User signatures are trusted only after domain/nonce/expiry checks. Upstream AMMs, selected quote tokens and network execution are dependencies, not our guarantees.

## Non-negotiable invariants

| ID | Invariant |
|---|---|
| S01 | Supply can only decrease after the single initial mint; no creator allocation except explicit purchases |
| S02 | Curve backing, collected fee liabilities, reward commitments and unrelated launches never cross-subsidize |
| S03 | Every recorded fee claim is backed by received asset; accrual cannot mint an IOU without funds |
| S04 | Founding LP principal has no withdrawal/approval/arbitrary-call escape; fees alone can leave |
| S05 | Creator/hook/recipient/economic settings are committed before first buy and cannot be replaced by a graduation caller |
| S06 | A failed graduation attempt has zero pool/approval/asset side effects outside the retained pending purchase |
| S07 | Refund/earned-payment rights never expire; repeated claims cannot exceed entitlement |
| S08 | Untrusted hookData cannot spoof trader, referrer, token or quote direction |
| S09 | Unsupported module combinations and aggregate fee cap are enforced onchain, including worst-case conditions |
| S10 | No launch configuration can block normal sells through a documented supported route using an advertised buy-only rule |
| S11 | Network/domain identifiers prevent cross-chain signature/config replay |
| S12 | Indexer/API failure cannot change onchain accounting or authorize funds movement |
| S13 | One launch's controller cannot mutate another record; external-pool opener cannot impersonate token owner |
| S14 | Returned approvals, native refunds and arbitrary recipient hooks cannot reenter accounting |
| S15 | Actual minted LP liquidity, token inventories, principal dust and sold entitlements reconcile |
| S16 | Module deactivation for new launches does not silently alter old launch behavior |

## Threat-specific requirements

MEV: slippage and deadlines mandatory; transaction simulation is not private order flow. A public curve and last buy are predictable. No claims that price continuity removes sandwiching. A high opening fee is an economic rule, not proof of fairness. Wrong opening price in external-token pools is depositor risk and must be previewed.

Initial pool griefing: validate deterministic token address, exact key, authorized initialization context and expected price. Test attacker calling the genuine periphery initializer. Merely allowlisting PositionManager as hook sender is insufficient because it is publicly callable. V3 atomic launch must revert safely on conflicting initialization; document that this is denial-of-service resistance by retrying new salt, not prevention of every adversarial attempt.

Reentrancy: checks/effects/interactions plus explicit guards across curve, fee claims, router and vault entry points. Handle ERC-777-like callback attempts by rejecting unsupported tokens and testing malicious mocks. Uniswap unlock callbacks must authenticate manager and active operation context; caller cannot trigger arbitrary payment from the executor.

Quote-token risks: USDC blacklist/issuer upgrades can stop transfers. Fee-on-transfer/rebase assets unsupported. Validate received deltas, not nominal transfer arguments. Governance can stop NEW launches in a compromised quote asset but cannot override issuer freezes or confiscate user balances.

Fee compounding: service fee, LP fee, burn and creator allocation have different denominators. Test execution-order effective price and maximum deduction. Integer overflow/truncation, exact-input partial fills and orientation reversal must have explicit tests. Do not distribute LP principal as fees when reading token balances with preexisting donations.

Immutable modules: no upgradeable module proxy for existing launches. If modules make external calls, target is fixed and return values bounded; a revert can affect swaps, so only reviewed implementations may be activated. Trade events cannot create unbounded arrays/loops. Gas exhaustion tests use maximum six modules and five recipients.

Identity: router sender is often not the economic user. Authenticated recipient and actor may differ; wallet cap uses actual recipient, referral entitlement uses authorized actor. Aggregators with anonymous actor get no identity reward, and their supported economic behavior is documented. EIP-7702/code-size heuristics do not establish human identity.

Community jobs: reviewer determines quality, cannot guarantee fairness. Timed acceptance/rejection policy protects deterministic exit, not subjective satisfaction. Offchain evidence retention is needed to inspect disputes; no claim that content hash proves quality.

## Authority matrix

| Role | Allowed | Forbidden |
|---|---|---|
| Creator | initial configuration; metadata edits; manage optional own treasury through declared role | change launch economics, mint, remove founding LP, seize claims |
| Protocol governance multisig | reviewed new module/asset/factory enablement via 48h timelock; fee policy for future launches | rewrite existing module configs or recipients; principal extraction |
| Emergency guardian | immediately stop new launches/new module selections and pause maintenance compound/buyback | stop earned claims, remove liquidity, change swaps' frozen fees |
| Reviewer | accept/reject submitted work with reason within deadline | take contributor payment; change accepted amount |
| Indexer/API operator | rebuild read model; rate-limit service | sign user transactions or modify onchain balances |
| Moderator | hide harmful content from first-party discovery with audit trail | freeze token or present hidden content as burned/deleted onchain |

## Public-release gates

Independent review of custom math/hook/accounting; pinned upstream license review; real local and fork tests; bytecode/config verification; authority disclosure; incident drill; network-specific launch authorization. Public deployment, even to testnet, is a separate user approval. Documentation makes no assertion that these gates have already passed.
