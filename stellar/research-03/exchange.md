# Original user-facing research exchange

Contains the accessible user messages and assistant commentary/final responses in order. Internal reasoning, tool payloads, runtime configuration and credentials are excluded. Artifact links may be relocated for this archive.


## User — user

Important new development — Stellar Bell / Protocol 30:

Investigate the newly announced Bell upgrade as a potential change to the opportunity landscape, not as proof that its features are already live. Start with the official announcement and upgrade guide:
- https://stellar.org/blog/developers/introducing-bell-protocol-30-on-stellar
- https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide

Examine the product implications of each proposal:

- CAP-84, muxed contract addresses: A W address adds a customer identifier to a contract address. Explore whether this makes multi-customer smart-account products economically and operationally viable: agent spending accounts, payment acceptance, ramps, marketplaces, treasury accounts, or privacy-aware financial applications. Compare it with the previous one-contract-per-customer approach. Examine internal balance accounting, authorization isolation, refunds, event indexing, address compatibility, and what happens if a customer ID is misassigned. A shared contract address and a visible customer ID must not be presented as cryptographic privacy.

- CAP-87, ML-DSA verification in smart contracts: Explore whether post-quantum authorization creates a real customer problem and product opportunity for wallets, custodians, high-value RWA holders, or long-lived agent mandates. Distinguish smart-contract authorization from network transaction signatures, which remain Ed25519. Do not treat post-quantum signatures as payment confidentiality or invent urgent demand without buyer evidence.

- CAP-88, millisecond-resolution ledger timing: Examine whether it creates any plausible future opportunity for payments, trading, or agent workflows. Do not assume Bell itself produces sub-second ledgers or faster user-facing settlement. Identify what further protocol changes and observed performance would be required.

For every Bell-enabled thesis, classify the dependency as: buildable on today's mainnet, buildable only after a successful Protocol 30 activation, or dependent on further upgrades or third-party adoption. Check the announced vote status at research time.

Search for 3–5 product opportunities that become materially stronger because of Bell, then compare them against the other agentic, RWA, DeFi, and privacy ideas. Do not promote a Bell idea just because the upgrade is new. Re-rank the finalists only if Bell changes customer value, distribution, economics, or defensibility in a concrete way.


## Assistant — commentary

I’ll check Bell’s announcement, activation status and CAP specifications, then test whether its changes materially improve any company thesis. I’ll separate what works on current mainnet from what requires Protocol 30 or later adoption.


## Assistant — commentary

CAP-84 has a consequential limit: the proposed W address attributes an incoming SAC transfer to a customer ID; it does not create a separate balance or spending authority. I’m using parallel research to examine the commercial opportunities and post-quantum/timing changes while I trace the shared-account accounting and refund risks.


## Assistant — commentary

The live mainnet endpoint reports Protocol 29, even though its Core binary is version 30. Bell’s votes are still scheduled for November 3 on testnet and November 23 on mainnet.

Bell could reduce deployment and deposit-attribution work for shared accounts. The savings are not automatic: tenant accounting and authorization still need to be built, and pooling can increase contention and the impact of an accounting error.


## Assistant — commentary

The strongest Bell-specific candidate is stablecoin payment operations: helping existing operators credit receipts, reconcile balances, investigate exceptions and handle refunds. There is a concrete public request for customer-tagged deposits into smart contracts, but no evidence yet that a buyer would pay a new vendor to solve it.

I’m keeping the earlier finalists’ ranking unchanged. Bell improves some account plumbing; it does not resolve their harder questions around demand, issuer access, liquidity or confidentiality.

## Assistant — commentary

The addendum now covers five company candidates, their activation and partner dependencies, and the accounting and recovery risks of shared accounts. The decision turns on one missing piece of evidence: an operator’s real exception records and willingness to pay for a pilot.

CAP-87’s strongest business hypothesis is recurring authority and migration assurance. Its value would come from managing keys, recovery and policy drift across institutions—not merely adding an ML-DSA verifier.

## Assistant — final_answer

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
