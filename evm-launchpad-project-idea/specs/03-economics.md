# Economics: proposed policy and executable math

All numbers here are design defaults, not observed competitor parameters. Monetary arithmetic uses checked integers and full-precision multiplication/division. Fees use basis points (10,000 = 100%); Uniswap LP fees use pips (1,000,000 = 100%). Keep separate types/validation.

## Fixed supply and curve

Let S = 1,000,000,000 tokens with 18 decimals. Sold capacity qg = 4S/5; founding LP token allocation S/5. No team mint, future mint or hidden reserve. Creator may buy normally, with their first buy disclosed; default zero, hard cap 1% of S in the launch transaction and subject to the same opening rules.

Use continuous reference R(q) = A*q/(B-q), B = 16S/15, q in [0,4S/5]. A is denominated in quote asset units. R(0)=0, R(qg)=3A. Marginal price p(q)=A*B/(B-q)^2. At graduation p(qg)=15A/S and R(qg)/(S/5)=15A/S: the curve and seed inventory ratio match in the ideal reference model. Price ratio end/start is 16, not 20.

USDC design preset: A = 2,000 USDC, target backing = 6,000 USDC. Initial FDV = 1,875 USDC; terminal FDV = 30,000 USDC. These are FDV values, not dollars raised. Initial validation envelope for custom presets: A from 500 to 50,000 USDC, factory-approved presets only. Wrapped-native presets use explicit quote-denominated A; display live USD estimates but never modify curve parameters when an oracle price changes.

S is not divisible by 15 in raw units. Implement R(q) as the exact rational expression 15*A*q/(16*S-15*q), avoiding a rounded stored B. For integer buys use the difference of ceiling-valued cumulative reserves; sells pay the difference of floor-valued cumulative reserves. Keep a separately accounted rounding-surplus bucket; trading cannot spend fee liabilities. Solve output with full-precision math and adjust by bounded checks or binary search so quoted cost never exceeds budget. One-unit trades and repeated buy/sell cycles must not create profit from rounding.

The final purchase is capped by remaining q. Compute actual net cost for that q, charge fee only on that cost, refund all excess gross input. For net cost n and configured fee rate f, gross charge = ceil(n*10000/(10000-f)); fee = gross-n. Never charge a percentage of the unused budget. Sells apply ceil(grossQuote*f/10000), bounded by grossQuote; quote explicitly rejects zero net output. Quotes and execution share the same arithmetic library.

## Entitlements and failure refund

Before graduation, purchased tokens are nontransferable internal curve entitlements, not freely transferable ERC-20 balances. They can be sold back through the curve. All S ERC-20 tokens remain in custody. On graduation transfer only the LP allocation to the executor; reserve sold entitlements for user claims. After graduation users can claim actual tokens, including partial claims for Advanced-profile wallet caps. This prevents external curve-phase pools without hidden transfer taxes. Token page must distinguish entitlements from liquid tokens.

Refund after expiry or unrecoverable graduation is not a full original-payment guarantee. Freeze Q outstanding entitlements and backing F; each holder burns entitlement x and receives floor(F*x/Q). Historical trade fees are nonrefundable and disclosed. Claims have no expiry and no admin sweep. Residual rounding dust remains reserved; no last-claimer windfall. If Q=0, no holder refund exists; accounting tests must establish that backing is zero except rounding surplus, which follows the committed dust policy.

## Graduation liquidity and dust

ALL net backing goes toward founding liquidity, never creator or protocol revenue. Use canonical TickMath/LiquidityAmounts and tick-spacing-aligned full range. Round initial sqrt price down in raw currency units for the actual address ordering. Max price-continuity deviation: 1 basis point in supported parameter envelopes; test both currency orders and all quote decimals.

Finite full range and integer liquidity mean exact consumption of both seed balances is not guaranteed. Enforce maximum residual of max(2 raw units, 1 ppm of seed amount) per currency in approved envelopes; if exceeded, reject graduation and fix parameters. Residuals plus rounding surplus belong to a per-launch nonwithdrawable DustVault, explicitly visible, never counted as earned fees. No sweep/claim by creator or admin. Public disclosure: principal is in founding liquidity plus bounded locked dust; do not claim literally every last unit is in the AMM.

## Fees and revenue

| Component | Default | Bound / recipient |
|---|---:|---|
| Launch creation fee | 5 USDC | Manifest-approved equivalent for wrapped-native preset, fixed at launch; protocol, atomic rollback on failed launch |
| Curve trading fee | 100 bps total | 30 protocol + 70 creator by default; total ceiling 300 bps including opening surcharge |
| V4 launch service fee | 100 bps quote-side | 30 protocol + 70 creator; exact-input only, buys from input and sells from output |
| V4 LP fee | 30 bps | Fixed or dynamic; maximum 100 bps; distinct from service fee |
| V3 LP fee | 100 bps | Founding LP earnings: 70% creator / 30% protocol; no hook levy |
| Existing-token service fee | 30 bps protocol + 0 opener | Opener up to 50 bps; clearly not token-team revenue |
| Existing-token LP fee | 30 bps | Approved choices 5/30/100 bps; paid to active LPs |
| Opening surcharge | 0 | Optional temporary addition; included in aggregate ceiling |
| Blueprint royalty | 0 | No royalties in target scope; reusable templates do not require another fee |

At every phase cap effective deduction: quote-side service/opening fees plus worst-case LP fee plus token-side burn must keep conservative total loss from fees at or below 500 bps. Implement exact execution-order composition, not a misleading sum that understates effective cost. Quote must return each component in its own currency and total effective rate. Price impact is separate.

Creator can allocate their OWN income bucket among up to five team addresses, optional community allocation and referral share. Shares sum to exactly 10,000 within that bucket. Referral default zero, maximum 20% of creator's bucket; never added as a new trader charge. Self-referral disallowed; multi-wallet evasion is acknowledged. Treasury allocation default zero, maximum 50% of creator's bucket. Recipients and shares freeze at launch. No unilateral community takeover of fees.

V4 founding LP fee distribution is 70% creator / 30% protocol; optional community/team split applies within creator share. Service fees and LP fees are separate revenues. External LPs earn their own LP fees, not a share of creator service fees. Fees may be in either pool asset and are never silently sold into USDC.

## V3 seed model

Chosen design: creator supplies the entire fixed token supply minted to the launcher plus a quote seed; full-range position, spot set from quote/S, both assets deposited atomically. USDC seed envelope 500–100,000; default 1,000. Creator receives no free tokens. No post-creation initial buy inside this transaction. Trading begins after launch. Use real v3 math and bounded dust policy above. This intentionally differs from PONS if its liquidity construction differs; no copying an unverified mechanism.

## Economic attack tests

Test reserve conservation, fees versus principal separation, tiny final buys, repeated round trips, fee ceilings across modules, high-decimal/low-decimal pairs, manipulated external reference prices, toxic orders before auto-LP and self-referral wash trades. Fees are costs, not a Sybil proof. No APY or profit guarantees.
