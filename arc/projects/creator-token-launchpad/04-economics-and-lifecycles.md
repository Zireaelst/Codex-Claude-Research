# Economics, v3 lifecycle, curve and v4 graduation

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The initial economics should be deliberately constrained.**

The following are **proposed defaults**, not established optimal parameters.

| Parameter | Recommended initial policy |
|---|---|
| Supply | 1 billion tokens, 18 decimals, minted once. No creator allocation, future minting, transfer tax or blacklist. |
| Instant-launch liquidity | Creator-funded, two-sided, full-range v3 position. Pilot UI accepts 500–25,000 USDC; exact supported bounds must follow simulation. All issued tokens enter the position except explicitly bounded rounding residue. |
| Opening price | Derived from supplied USDC and tokens, with correct decimal scaling. With essentially all supply deposited, opening FDV is approximately the USDC seed—not an independently selectable valuation. |
| v3 pool fee | Fixed 1%; no additional interface trading fee initially. |
| Collected founding-LP fee split | **40% creator team / 50% community treasury / 10% protocol**, applied separately to each received asset. Immutable per launch. |
| Creator team | Up to five recipients; fixed percentages at launch. Recipient changes require the existing recipient’s consent and settle prior accrual first. |
| Launch fee | 5 USDC, charged only on successful creation. Separate from seed liquidity. |
| Curve fee | 1% on buys and sells, explicitly excluded from backing reserves. |
| Curve graduation | One reviewed preset initially; illustrative net reserve target of 6,000 USDC, 80% sold and 20% reserved for LP. |
| Curve expiry | Fixed at creation; initially 30 days. No discretionary creator extension. |
| v4 base fee | Fixed 1% first; bounded dynamic presets introduced only after separate review. |
| Community rewards | Funded work payments first. No automatic rewards for trading volume or wallet count. |
| Burns | Disabled initially. Later, an immutable option may burn a bounded share of collected token fees, never principal. |
| Bounty budgets | Fully funded from available USDC before publication. No spending against estimated future fees. |

**The seeded v3 choice has a real cost:** creators need starting capital, unlike single-sided launchpads. In return, the app can show an actual USDC reserve from the start. If target creators reject that tradeoff, evaluate a separately specified single-sided v3 preset before building; do not silently replace the liquidity model.

Full-range LP is less capital-efficient than a concentrated launch range. That is an acceptable initial tradeoff for simpler custody and fewer range-management assumptions.

Crucially, **v3 fees arrive in the input asset**. Buys commonly generate USDC fees; sells commonly generate token fees. The treasury must display:

- Available USDC.
- USDC committed to work.
- Uncollected estimated USDC fees.
- Token-denominated fees, separately.
- Completed USDC payments.

Do not mark token fees to a manipulable spot price and present the result as spendable dollars. Uniswap’s collection interface explicitly returns both assets. [v3 fee collection](https://developers.uniswap.org/docs/protocols/v3/guides/managing-liquidity/collect-fees)



**The two lifecycles need different failure semantics.**

For **Start trading now**:

```text
DRAFT → VALIDATED → SUBMITTED → ACTIVE_LOCKED
                         └── transaction reverts → retryable draft
```

Creation is atomic: deploy token → register canonical path → initialize pool at the committed price → mint LP directly to the locker → register fee policy and treasury → emit launch record.

There must never be a successful “token created, LP will be locked later” state.

- A failed transaction returns transferred assets through EVM rollback; gas is not refunded.
- An existing unexpected pool or price causes a revert, not opportunistic reuse.
- Unused USDC is returned; token rounding residue follows a predefined locked-residue policy.
- Successful launch is irreversible. The seed cannot be reclaimed by the creator.
- Selling occurs through the pool, not through a launch refund function.
- Founding LP principal cannot be decreased, transferred, approved away or rescued.
- Fee collection is permissionless, but proceeds can only enter the fixed accounting path.
- An app moderation flag may hide a token from discovery; it cannot freeze token transfers or seize LP.

For **Launch toward a community target**:

```text
DRAFT → CURVE_ACTIVE → READY_TO_GRADUATE → GRADUATED
              │                │
              │ expiry         │ unresolved migration failure
              ▼                ▼
          REFUNDABLE ← fixed timeout
              │
              ▼
            CLOSED
```

To prevent pre-graduation transfers from undermining the curve, I recommend **internal curve balances redeemable for the eventual token**, rather than introducing permanent restrictions into the ERC-20.

During the curve:

- Users buy and sell curve balances.
- The UI explicitly says these are claimable launch balances, not transferable ERC-20 holdings.
- The fixed token supply remains in contract custody.
- No creator-only first-buy privilege.
- Buys and sells use the same published pricing function and explicit slippage limits.

At the target:

- The final buy is capped to remaining capacity; excess USDC is returned.
- Curve trading closes.
- Graduation is attempted permissionlessly and atomically.
- Net backing USDC plus reserved tokens form the v4 LP.
- The LP is locked before graduation is recorded.
- Curve balances become redeemable 1:1 for tokens.
- Token claims do not depend on the website or indexer.

If graduation fails, reserves and balances remain intact. Anyone can retry. After a fixed recovery timeout—proposed **72 hours**—users can trigger the predefined refund state.

If the curve expires or migration becomes unrecoverable, redeem balances against a fixed pro-rata snapshot of remaining backing reserves. **This is not a refund of each user’s original purchase price.** Earlier buys, later buys, sells and trading fees make that promise impossible without separate insurance. Unclaimed refunds must not become an owner sweep.

An immutable hook initialization guard should permit only the registered graduation executor to initialize the canonical pool. Otherwise an attacker can initialize the future pool at a hostile price before migration.



**Curve continuity must be derived, not approximated by marketing numbers.**

A workable research model uses virtual constant-product reserves. Let:

- \(S\): total supply;
- \(q\): curve tokens sold;
- \(A\): virtual initial USDC;
- \(B\): virtual initial token reserve.

Then:

\[
R(q)=\frac{Aq}{B-q},
\qquad
p(q)=\frac{AB}{(B-q)^2}
\]

Here \(R\) is net backing USDC, excluding fees. To graduate with remaining tokens \(S-q_g\), require approximately:

\[
p(q_g)=\frac{R(q_g)}{S-q_g}
\]

For an 80% sale, this gives \(B=\frac{16}{15}S\). With \(A=2{,}000\) USDC:

- Graduation reserve: 6,000 USDC.
- Tokens for LP: 200 million.
- Terminal marginal price: 0.00003 USDC.
- Initial marginal price: approximately 0.000001875 USDC.

These are **analytical parameters, not production-ready Solidity constants**. Integer rounding, token ordering, finite v4 tick bounds and minting dust must be reconciled against actual pool mathematics. Require a documented continuity tolerance, proposed at most one basis point before trading fees, backed by differential tests.

A marginal-price match does not mean a large trade has identical execution before and after graduation: liquidity depth also changes.
