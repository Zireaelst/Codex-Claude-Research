# Original final chat response

**Bell adds a credible challenger, but does not change my recommendation yet.** Keep liquidity-aware DeFi risk and recovery operations as the first company hypothesis to validate, with RWA execution and cash readiness as backup. Add **stablecoin collections and payment-exception operations** to buyer discovery.

**Main reason I might be wrong:** an existing ramp or fintech may have expensive receipt-attribution problems that CAP-84 materially solves. Its operational records and a paid pilot could move that opportunity into first place.

The [full Bell investigation](../research-03/report.md) covers five company candidates, technical architecture, failure recovery, competition, interview targets and decision-changing experiments.

**Activation checked 21 October 2026:** Bell is not active on mainnet. The public endpoint reported **Protocol 29**, although its connected Core software was version 30. The announced votes remain **3 November for testnet** and **23 November for mainnet**, both at 17:00 UTC and conditional on validator approval. [Official upgrade guide](https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide), [saved mainnet observation](../research-03/evidence/bell-mainnet-root-2026-10-21.json).

The consequential findings are:

- **CAP-84 improves deposit attribution, not customer isolation.** W addresses attach an identifier to a shared contract destination. Tenant balances, spending authority, reconciliation and recovery remain application responsibilities. Shared contracts already support explicit customer-tagged deposit calls; Bell reduces address-level integration friction. It supplies no cryptographic privacy. [CAP-84](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0084.md).
- **CAP-87 enables new contract authorization policies.** ML-DSA verification does not replace Ed25519 network transaction signatures or conceal payments. Classical admin, upgrade or recovery paths can undermine an otherwise post-quantum spending policy. The credible business hypothesis concerns managing the entire authority lifecycle. [CAP-87](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0087.md).
- **CAP-88 improves clock precision, not demonstrated settlement speed.** Millisecond timestamps do not establish sub-second ledgers, millisecond contract deadlines or faster fiat availability. Trading/payment theses need observed production performance and downstream support. [CAP-88](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0088.md).

Five opportunities deserve different treatment:

| Full-product opportunity | Concrete Bell benefit | Decision |
|---|---|---|
| **Collections, reconciliation and refund operations** for existing payment businesses | Attributable receipts into programmable pooled treasuries | Strongest new discovery challenger |
| **Agent-commerce budget and recourse operations** | Easier funding of shared customer budgets | Conditional; real purchases and fulfillment remain unproven |
| **Marketplace seller balances and dispute operations** | Simpler order/customer receipt attribution | Requires an existing transaction channel |
| **Customer treasury and RWA cash servicing** | Better attribution in issuer-approved pooled structures | Strengthens existing RWA operations thesis modestly |
| **Authority and post-quantum migration assurance** | Native verification enables enforceable contract-policy tests | Technically meaningful; hardest institutional sale |

For each, the report separates **buildable today**, **Bell-dependent functionality**, and **third-party adoption or further-upgrade dependencies**.

The strongest demand evidence specific to CAP-84 is a [public builder request concerning inbound smart-contract payments](https://github.com/orgs/stellar/discussions/1950). That establishes an integration problem—not purchasing demand. Existing wallet, ledger, custody and escrow providers also make these crowded markets.

**The next decision-changing evidence is customer evidence:** reconstruct actual payment exceptions with eight operations, finance and engineering buyers; obtain two redacted histories and one credible paid-pilot path. Then compare W against existing memo/M-address and explicit contract-deposit workflows. If those already solve the problem adequately, Bell supplies little independent company advantage.
