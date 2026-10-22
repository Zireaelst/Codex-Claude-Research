# Security, failure recovery and release gates

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**Security review must focus on the following failure modes.**

| Risk | Required design and test |
|---|---|
| Curve rounding and reserve insolvency | Integer-only arithmetic; explicit rounding direction; differential model; repeated dust trades cannot extract value; reserve accounting survives arbitrary buy/sell sequences. |
| Graduation discontinuity | Derive parameters together; compare actual initialized pool price and depth; prevent reserve deductions disguised as graduation fees. |
| Slippage and stale quotes | Every swap has minimum output/maximum input and expiry. Never use indexer prices as execution authority. |
| First buys and MEV | Atomic initialization; no hidden creator allocation or privileged curve price. v3 offers no hook-based protection. Private submission is optional only if actual Arc support is verified. |
| Pool initialization griefing | Reject unexpected v3 pool state; caller-bound launch salts reduce copying but are not complete protection. v4 initialization must require the registered executor. |
| External pools | Display rule scope. External trading can avoid our hook and creator fees. Additional LPs in the same pool earn their own share. |
| Locker escape routes | No generic execution, NFT approval, upgrade, rescue, migration or inactivity sweep affecting principal. Inspect inherited and callback paths. |
| Fee accounting | Credit actual received amounts; separate assets and launches; settle accrued fees before recipient changes; prevent duplicate claims and dust leakage. |
| Arc USDC representation | Use ERC-20 units consistently; reject unintended native value; test shared-balance behavior and gas budgeting on Arc. A mock ERC-20 is insufficient proof. |
| Hook permissions | Validate callback address flags, PoolManager caller, registered pool key and supported swap directions. Disabled callbacks cannot be invoked successfully. |
| Reentrancy and malicious recipients | Update state before external transfers; use pull claims; a blocked recipient must not halt all fee collection or other beneficiaries. |
| Treasury abuse | Manager authority is explicit. A manager can make poor or collusive awards; the contract cannot judge artistic quality. No arbitrary treasury call execution initially. |
| Sybil behavior | No “one wallet equals one person” claims; no volume mining, first-buy rewards or wallet-count rewards. |
| Metadata and social impersonation | Content hashes, edit history, signed creator linkage and moderation. A verified social link is not a safety endorsement. |
| Operational dependency | Indexer outages must not block claims/refunds. Stale data is labelled stale, never substituted with zero. |
| Licensing and legal exposure | Review copied code licenses, operating jurisdictions, token promotion and paid-contribution terms before release. Avoid implying token ownership conveys IP or financial rights. |

For work payments, use explicit states:

```text
FUNDED → ASSIGNED → SUBMITTED → ACCEPTED → CLAIMABLE → PAID
             └──────────────→ REJECTED / EXPIRED
```

A manager may cancel unassigned work. Once assigned, the agreed amount and acceptance terms cannot change unilaterally. Rejected or expired funds return to the **community treasury**, not the creator’s personal wallet. Accepted claims cannot be cancelled. Public rejection reasons and reviewer identities make discretionary trust visible.

**Exclude “every Nth buy wins the pot.”** The counter is predictable. Bots can split purchases, fill the remaining positions, bundle transactions or compete on ordering when the pot exceeds fees and price impact. Minimum buys and wallet caps do not solve this.

Randomness changes the mechanism but introduces oracle, entry-allocation, Sybil and potentially gambling issues. For this product, a fixed-budget creative commission or judged contest has a clearer purpose. Do not reward manufactured volume.



**Before any mainnet launch, every applicable release criterion must pass.**

| Check | Pass criterion |
|---|---|
| Network/dependencies | Correct chain ID; independently verified canonical contracts, versions and runtime code; no placeholders. |
| Reproducibility | Clean build reproduces release artifacts with pinned settings and dependencies. |
| Supply/path | Exactly one issuance and canonical path; no hidden allocation or mutable economics. |
| Liquidity custody | No reachable principal withdrawal, approval, transfer, upgrade or recovery escape path. |
| USDC accounting | Native/ERC-20 aliasing and decimal behavior tested on Arc; gas is not double-counted as spendable balance. |
| Fees | Collected amounts reconcile by asset and beneficiary; UI never labels token fees as USDC cash. |
| Trading | Correct quoting, slippage, expiry, approvals and receipt handling; buys and sells tested. |
| Work payments | Fully backed commitments; accepted payments cannot be cancelled or paid twice. |
| Curve/v4, when enabled | Solvency, continuity, initialization protection, retries, claims and refunds pass adversarial tests. |
| Hooks, when enabled | Permission bits and callback authentication verified; bounds hold across every enabled configuration. |
| Indexer | Replay produces matching accounting; stale or incomplete data is labelled; claims work without it. |
| Security review | No unresolved critical/high findings; independent reviewer has examined custody and accounting. |
| Operational control | No production keys in Studio, browser bundles, repositories or logs; monitoring and recovery procedures tested. |
| Product honesty | Lock, fee, refund, manager authority and external-pool limitations are visible before signing. |
| Production acceptance | Small-value receipts and balance changes reconcile end to end; no simulated success presented as real. |
