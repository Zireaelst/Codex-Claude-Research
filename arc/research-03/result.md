# Research 03: High-conviction mechanisms — confidential financial coordination

## Original result

Source: this conversation, message timestamp `2026-10-18T17:30:19.014Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

**The strongest opportunity is to make confidential financial claims enforceable—not simply to make payments private.** My leading company hypothesis is a **confidential borrowing-base network**: lenders can verify which receivables support a credit line, whether they remain eligible, and whether participating lenders have already financed them, without receiving the borrower’s entire customer ledger.

The strongest protocol hypothesis is **confidential multilateral clearing**: competing businesses cancel reciprocal obligations without exposing their commercial relationships to a clearing operator. A third promising direction is a **market for reserved settlement capacity**, where payment companies purchase an enforceable right to destination-chain liquidity before they need it.

These are hypotheses with meaningful competitors, not undiscovered categories. Several findings materially narrowed the opportunity:

- **“Private credit scoring” is already occupied.** Credora explicitly describes privacy-preserving computation over borrower data; RedStone now combines ratings, pricing, and settlement infrastructure. A new entrant needs control over collateral eligibility and encumbrance, not another opaque risk score. [Credora’s explanation](https://medium.com/credora/data-driven-lending-is-better-5a8bc7c01ec1), [RedStone documentation](https://docs.redstone.finance/)
- **Instant liquidity for delayed redemptions is also occupied.** Centrifuge describes a live Symbiotic integration, while ETHGlobal’s Harbor demonstrates trading pending withdrawal rights. “Sell your withdrawal queue position” is insufficient differentiation. [Centrifuge–Symbiotic](https://centrifuge.io/blog/symbiotic-centrifuge), [Harbor](https://ethglobal.com/showcase/harbor-48dow)
- **Arc already has technically substantive agent-payment and netting experiments.** OpenBook, ACR, Verdikt, and arclear make generic verified payments, compute-price benchmarks, and obligation netting poor novelty claims. [OpenBook](https://ethglobal.com/showcase/openbook-8ngw6), [ACR](https://ethglobal.com/showcase/acr-sgdjr), [Verdikt](https://ethglobal.com/showcase/verdikt-mi2xq), [arclear source](https://github.com/aljosamakevic/arclear)
- **Cryptographic correctness does not imply commercially useful privacy.** Penumbra’s documented swap mechanism exposes input amounts while privately minting outputs; its threshold-encrypted swap design is described as a future upgrade. A research analysis of Renegade also identifies selective-abort and probing risks; those are researchers’ findings, not an independently reproduced security assessment here. [Penumbra mechanism](https://protocol.penumbra.zone/main/dex/swap.html), [Renegade analysis](https://arxiv.org/abs/2609.27100)

**What the evidence establishes**

The scan covered payment finance, credit, solver networks, auctions, confidential execution, and verifiable computation across Ethereum/L2s, Base, Avalanche, Solana, and privacy-focused networks.

| Reference group | Evidence and limitation |
|---|---|
| **Huma, Maple, Centrifuge** | Operational financial products with documentation and contract infrastructure. Huma publishes Solana, EVM, and Stellar addresses; this supports product existence, not independent verification of its reported volume. [Huma contracts](https://docs.huma.finance/ecosystem-resources/smart-contracts), [Maple](https://docs.maple.finance/), [Centrifuge vault mechanics](https://docs.centrifuge.io/developer/protocol/features/vaults/) |
| **Across, Everclear, OneBalance, CoW, Term** | Concrete mechanisms for solver financing, rebalancing, resource commitments, combinatorial execution, and fixed-term funding. Term publishes Avalanche deployments. These substantially constrain what counts as novel cross-chain coordination. [Across](https://docs.across.to/guides/concepts/intents-architecture), [Everclear](https://docs.everclear.org/developers/protocol-mechanics), [OneBalance](https://frontier.tech/onebalance), [CoW](https://docs.cow.fi/cow-protocol/concepts/introduction/fair-combinatorial-auction), [Term contracts](https://developers.term.finance/deployed-contracts/deployed-contracts-1) |
| **Penumbra, Renegade, Canton, Arcium, zkLedger** | Different confidentiality models: shielded accounting, MPC matching, stakeholder-restricted disclosure, confidential computation, and research-grade auditable ledgers. They are not interchangeable privacy libraries. [Renegade source](https://github.com/renegade-fi/renegade), [Canton privacy model](https://github.com/canton-network/cf-docs/blob/main/docs-main/appdev/deep-dives/privacy-model.mdx), [Arcium](https://www.arcium.com/build), [zkLedger paper](https://eprint.iacr.org/2018/241.pdf) |
| **Arc-sponsored ETHGlobal winners** | OpenBook won **Best Agentic Economy Application with Circle Agent Stack**; ACR won **Best DeFi or Agentic Application**. Their showcase descriptions identify testnet implementations. Awards establish recognition, not adoption or security. |
| **Technically interesting showcase projects** | Harbor identifies an unaudited Hoodi demonstration. Verdikt explicitly discloses simulated CRE execution broadcasting to testnet contracts. Proofs of Inference combines EZKL with payment verification and lists Protocol Labs and Hedera awards—not Arc awards. [Proofs of Inference](https://ethglobal.com/showcase/proofs-of-inference-6rug4) |

For Arc competition checks, I examined its official ecosystem and product announcements, relevant protocol documentation, ETHGlobal entries, and public repositories including arclear, alongside targeted searches for credit, clearing, private computation, and settlement products. Arc’s official material already identifies Aave, Morpho, and StableFX; “Arc needs lending or FX” is therefore not a defensible gap. **Confidence is high that the adjacent categories exist, moderate that the combinations below are differentiated, and low that search alone establishes an unserved market.** [Arc’s ecosystem announcement](https://www.arc.io/blog/arc-economic-os-internet?trk=public_post_reshare-text)

Arc’s useful contribution is a common USDC settlement and operating asset, deterministic local finality, and proximity to financial applications. These reduce operational friction; they do not establish source-data truth, force external chains to finalize, or create liquidity. None of the proposals assumes Arc-native privacy is available. [Arc design](https://www.arc.io/litepaper)

**Eleven distinct opportunities**

**1. Confidential borrowing-base network — strongest company hypothesis**

Payment processors and receivables financiers need revolving funding without disclosing every merchant, invoice, and customer relationship to each lender. They currently use collateral reports, servicing integrations, and private underwriting; Huma, Centrifuge, and Credora are the closest reference points. The mechanism combines authenticated receivable records, commitments, proofs of eligibility and concentration, a shared encumbrance registry, and enforceable control over collections. Arc would connect those proofs directly to USDC borrowing availability and repayments, while hiding underlying records from public observers and non-authorized lenders. The hardest objection is that cryptography cannot discover omitted liabilities, fictitious invoices, or pledges outside the participating system. It could become durable infrastructure if lenders accept its certificates and originators integrate their servicing data—distribution and legal recognition would form the moat.

**2. Reserved settlement-capacity market — strongest market-structure hypothesis**

Payment companies and cross-chain solvers need assurance that USDC will be available in a particular place when an obligation falls due. Across finances execution and Everclear coordinates rebalancing, while OneBalance makes resources credibly available for execution; those are substantial precedents. The proposed product sells **future, bounded capacity commitments**, backed by identifiable inventory or explicitly underwritten credit, with reservation exclusivity and defined failure compensation. Arc provides a common venue for collateral, premiums, and obligations without introducing a volatile gas-token balance. The central objection is economic: fully reserved liquidity can be expensive, while reused liquidity makes the guarantee vulnerable precisely during stress. A useful protocol could grow into a wholesale availability market, but only if customers pay for certainty beyond what existing routing services deliver.

**3. Confidential multilateral clearing — strongest protocol research direction**

Marketplaces, payment intermediaries, and service networks often owe one another money but cannot expose their gross business graph to a shared operator. Arc’s arclear already demonstrates collateral-backed multilateral netting, while Everclear and Canton supply adjacent clearing and confidentiality mechanisms. The new mechanism would privately compute eligible cancellations using MPC, then prove authorization, conservation, unique consumption of obligations, and exposure limits before settling residual USDC. Arc improves the settlement layer through common collateral and finality; the privacy claim concerns **gross obligations**, not the publicly visible residual payments. The hardest problems are selective abort, inference from repeated clearing rounds, and legally effective discharge of the underlying claims. If reciprocal flows are sufficiently dense, the product saves working capital as well as protecting commercial relationships—a stronger benefit than reducing transaction fees.

**4. Private cross-lender exposure cooperative**

Credit funds and lending curators cannot reliably detect when several apparently diversified borrowers share the same underlying debtor or collateral. Bilateral diligence and credit ratings help, but sharing full loan books creates competitive and confidentiality problems; Credora, Canton, and zkLedger are close conceptual references. Participants would use private entity matching and MPC aggregation to calculate overlap and concentration, with proofs binding results to committed portfolios. Arc could make admission of new USDC credit contingent on consortium-wide exposure limits rather than each lender’s isolated view. The adversaries are other members and the computation operator; approved aggregate results still leak information, and probing queries must be constrained. The opportunity is a shared risk utility, but it fails if institutions refuse complete submissions or cannot agree on canonical borrower identities.

**5. Proof-carrying financial computation market**

Lenders, treasury systems, and trading agents buy calculations whose correctness matters: portfolio exposure, covenant tests, or execution reconciliation. Boundless already provides a proof market, while Proofs of Inference and Arc’s Verdikt address adjacent verification problems, so another “pay for verified compute” marketplace is not enough. The differentiated product would bind a result to authenticated inputs, a precise financial specification, freshness rules, and a reusable proof that another institution can verify without rerunning the job. Arc makes the verified output composable with USDC credit and trading decisions, rather than merely attaching payment to computation. The main objection is that proving a calculation says nothing about whether its inputs are complete or its economic model is sensible. Its commercial potential is an interoperable market for financial evidence, with domain specifications and source integrations supplying the value beyond the proof engine. [Boundless source](https://github.com/boundless-xyz/boundless)

**6. Guaranteed redemption windows**

Corporate treasurers holding tokenized funds need predictable spending capacity, not merely an attractive offer to sell when conditions are calm. Harbor and Symbiotic already address immediate liquidity; the different product would let holders purchase a contractual right to exchange an eligible position for USDC during a defined window. Its mechanism is a capacity-backed liquidity option with explicit limits, eligibility conditions, exercise rules, and treatment of issuer suspension. Arc suits the premium, reserve, and settlement legs because the promised spending asset is USDC. Correlated exercise and issuer freezes are the decisive risks, and the product may have insurance or derivatives implications depending on its structure. It could support treasury asset allocation, but I would reject it if the guarantee is mostly discretionary exclusions wrapped around an ordinary RFQ.

**7. Recovery-capacity auctions for permissioned collateral**

RWA lenders need buyers who are legally eligible and financially able to absorb seized assets when ordinary liquidators cannot. Aave Horizon, RedStone Settle, and Symbiotic already address important parts of this problem, making the competitive bar unusually high. The remaining hypothesis is an auction for **committed recovery capacity before loan origination**, with issuer-specific eligibility, stressed price schedules, settlement limits, and controls against selling the same capacity repeatedly. Arc could make executable recovery capacity an input to USDC borrowing limits instead of relying solely on reported NAV. The hardest objection is that issuer-controlled transfers and redemptions can defeat an otherwise sound liquidation mechanism. This becomes a meaningful business only if independent lenders value portable capacity commitments more than issuer-arranged liquidity facilities. [Horizon mechanics](https://www.aave.com/docs/aave-v3/horizon), [RedStone’s competing offering](https://www.redstone.finance/asset-issuers/)

**8. Obligation-matched term funding**

Stablecoin payment businesses often finance predictable outgoing obligations with continuously repriced or withdrawable funding. Term Finance proves that fixed-term markets exist, while Maple and Huma address institutional and payment financing. The proposed adaptation matches signed cash-flow schedules against lender maturity preferences, creating a funding ladder that explicitly prices rollover gaps and contingent obligations. Arc allows incoming collections, debt service, and operating USDC to interact in one settlement environment. Its toughest objection is that finely tailored maturities fragment liquidity, and Term’s own evolution acknowledges this coordination problem. It could become treasury funding infrastructure, but a standalone Arc fixed-rate lending clone would not justify building it. [Term’s market-structure discussion](https://www.term.finance/post/ordermarkets)

**9. Confidential treasury RFQ with accountable execution**

Businesses seeking large stablecoin FX conversions reveal valuable information when dealers learn their full size, urgency, and reservation price. StableFX, Renegade, and CoW already cover FX, private matching, and competitive execution, respectively. A differentiated mechanism would combine hidden aggregate demand, committed dealer quotes, controlled disclosure, and verifiable quote selection while addressing the option to learn information and then abort. Arc’s existing financial counterparties and stablecoin settlement could make this commercially relevant without creating another speculative trading venue. Privacy would cover unexecuted intentions against rival dealers and the coordinator; ordinary settlement still reveals executed amounts and addresses. This could become institutional execution infrastructure, but attracting competitive dealers and proving meaningful protection against probing are harder than encrypting bids.

**10. Solvency-constrained cross-chain refinancing**

Treasury operators want to replace debt and move collateral across venues without temporarily creating an unsafe or unhedged balance sheet. Across, OneBalance, and CoW provide execution components, but the customer’s objective is a final portfolio satisfying debt, collateral, and liquidity constraints. The mechanism would combine a portfolio constraint solver, resource reservations, bridge financing, and explicitly bounded intermediate states. Arc could act as the USDC funding and obligation-coordination venue across those operations. The critical objection is that arbitrary cross-chain atomicity cannot be assumed: partitions, delayed messages, and venue changes require somebody to bear completion risk. A company could sell guaranteed refinancing outcomes, but only by pricing that balance-sheet exposure honestly.

**11. Confidential purchasing accounts for agent fleets**

A business running many agents may want merchants paid without publicly revealing its supplier graph, internal budgets, and allocation of spending across teams. Public smart accounts expose too much, while Penumbra and Canton demonstrate different forms of private accounting and controlled disclosure. The mechanism would be a shielded purchasing ledger with delegated spending capabilities, shared-budget conservation proofs, merchant receipts, and narrowly scoped audit access. Arc supplies USDC funding and withdrawals, but internal transfers would have to remain within the confidential ledger for the payment graph to stay concealed. The strongest objection is that distinctive deposits, rapid withdrawals, merchant collusion, or an omniscient operator can identify participants despite sound proofs. It could grow into business purchasing infrastructure only if suppliers retain and reuse balances; immediate cash-out after every purchase largely destroys its privacy advantage.

**Privacy boundaries that materially affect the choice**

These guarantees are architectural proposals, not claims that an existing implementation has achieved them.

| Ideas | Intended guarantee and adversary | What remains observable |
|---|---|---|
| **1: Borrowing base** | ZK hides committed receivable details from the public and unauthorized lenders; authorized servicers/auditors retain access. | Borrower and lender addresses, draw/repayment amounts, timing, gas payer, and policy events. Threshold outcomes can reveal deteriorating credit. |
| **3: Clearing** | MPC hides individual gross obligations from an operator and non-colluding participants; proofs establish valid net settlement. | Residual amounts, participating settlement addresses, timing, gas, and events. Repeated outputs and known invoices can reveal much of a sparse graph. |
| **4: Exposure cooperative** | Private matching/MPC protects other members’ underlying portfolios, subject to the specified collusion threshold. | Approved aggregates or threshold results, update timing, and subsequent public lending decisions. Small groups and repeated queries create inference attacks. |
| **5: Computation** | ZK can hide a witness from the verifier while proving a specified computation. | Public inputs, result or result commitment, payment parties, amount, timing, and gas. An outsourced prover generally sees plaintext unless another confidentiality mechanism is added. |
| **9: RFQ** | Confidentiality of unexecuted demand and losing quotes against dealers/operator under the chosen MPC or threshold-encryption assumptions. | Executed transfers and market outcomes; counterparties learn their own trades. Abort behavior and repeated requests leak information. |
| **11: Purchasing ledger** | ZK hides internal balances and transfers from ledger observers; scoped disclosure permits audits. | USDC entry/exit amounts, funding and withdrawal addresses, batch timing, submitter gas, commitments/nullifiers, and external transaction events. |

**None hides IP addresses or RPC metadata by itself.** Relaying changes the visible gas payer but introduces an operator who may correlate requests; it does not establish anonymity. Stealth addresses obscure address reuse, not amounts or timing. Encryption protects stored or transmitted plaintext, whereas ZK proves statements, MPC distributes computation trust, TEEs depend on hardware and attestation, and FHE computes over ciphertext while leaving decryption-key governance unresolved.

For all proof-based designs, verifier correctness, data availability, key compromise, and any proof-system setup assumptions remain part of the threat model. zkLedger is particularly useful inspiration because it addresses completeness **within its ledger**, rather than pretending to prove that an institution has no outside liabilities. [zkLedger](https://eprint.iacr.org/2018/241.pdf)

**The five strongest, investigated more deeply**

**A. Confidential borrowing-base network**

**Closest three competitors:** Huma, Centrifuge, Credora.

The non-obvious differentiation is **collateral-state enforcement**, rather than lending, tokenization, or scoring. The conceptual architecture is:

`Servicer-authenticated records → confidential asset registry → eligibility/encumbrance proofs → credit availability → controlled collections`

A canonical asset identifier prevents different commitments from representing the same registered receivable; an encumbrance state machine prevents simultaneous participating pledges. Source signatures or authenticated API evidence establish provenance, while legal assignment and collection control establish something worth lending against. TLS proofs can authenticate received data, but cannot establish that the source is honest or complete. [TLSNotary verification model](https://tlsnotary.org/docs/protocol/verification/)

**Main unsolved question:** Can a lender obtain an enforceable, sufficiently complete definition of the financed asset pool without demanding the full underlying ledger?

**Strongest failure reason:** Each originator requires bespoke legal and servicing integration, leaving a consulting business rather than a scalable network. Credora’s existing confidential underwriting also means “lenders prefer privacy” is not a differentiator.

**B. Confidential multilateral clearing**

**Closest three competitors:** arclear, Everclear, Canton.

The differentiation is enabling parties to obtain working-capital savings **without giving a coordinator the complete obligation graph**. The architecture is signed obligations committed into private inputs, MPC computation of a candidate clearing set, participant authorization, and proof-checked USDC residual settlement.

The key advance must address information release and default behavior together. A participant should not receive valuable clearing information, refuse settlement, and repeatedly probe the others; an abort penalty is useful only when blame is provable. arclear’s disclosed recovery-versus-withdrawal race illustrates why a valid netting calculation is only one part of a clearinghouse. [arclear threat model and source](https://github.com/aljosamakevic/arclear)

**Main unsolved question:** Is there enough reciprocal flow among mutually acceptable counterparties to save meaningful capital while keeping output leakage tolerable?

**Strongest failure reason:** The customers with sufficient volume already trust an operator, while the customers unwilling to share information have too little reciprocal flow.

**C. Reserved settlement-capacity market**

**Closest three competitors:** Across, Everclear, OneBalance.

The differentiation is a **priced right to future availability**, distinct from a quote for immediate execution or a lock on a user’s present resources. Conceptually:

`Capacity providers → exclusive inventory/credit commitments → reservation market → delivery evidence → release or compensation`

The contract must distinguish reserved cash, reusable capital, and underwritten promises. Arc collateral cannot prove that a provider controls destination-chain inventory without reliable cross-chain evidence, and compensation is not equivalent to delivery.

**Main unsolved question:** Will payment operators pay a reservation premium exceeding providers’ capital and operational costs?

**Strongest failure reason:** Existing routers can bundle acceptable availability guarantees using larger balance sheets, leaving a standalone market with adverse selection and fragmented liquidity. This is a market-design opportunity, not yet a demonstrated new cryptographic primitive.

**D. Private cross-lender exposure cooperative**

**Closest three competitors/reference systems:** Credora, Canton, zkLedger.

Its differentiation is measuring **relationships between lenders’ portfolios**, rather than scoring each borrower independently. Entity identifiers would be authenticated and privately matched; exposure values would enter MPC aggregation; restricted outputs would inform member-specific limits or shared risk alerts.

The system needs controls over fake entities, subsidiaries, stale reporting, and members who omit inconvenient loans. Query governance is essential: unlimited exact aggregate queries can reconstruct other participants’ positions. Differential privacy may help some statistical outputs, but noisy results are inappropriate for an exact collateral-conservation requirement.

**Main unsolved question:** Who can compel sufficiently complete reporting while remaining acceptable to competing lenders?

**Strongest failure reason:** A regulator or dominant industry consortium may be necessary to bootstrap participation, leaving little room for an independent founder-led network.

**E. Proof-carrying financial computation**

**Closest three competitors:** Boundless, Proofs of Inference, Verdikt.

The differentiation must be **portable financial evidence**, not generic proof generation. A result should identify the source-data commitment, computation specification, observation window, and permitted interpretation, allowing several institutions to reuse it in different decisions.

The architecture combines source authentication, deterministic execution, proof generation, and a verifier registry tied to precisely versioned financial specifications. ZK proves execution; it does not prove that a model predicts reality. The ETHGlobal Trustless Inference description is a useful caution: checking a model identifier in a local environment does not prove what a remote inference provider actually executed. [Trustless Inference](https://ethglobal.com/showcase/trustless-inference-ytrxy)

**Main unsolved question:** Which financial calculation is expensive enough to verify independently, yet standardized enough for multiple buyers to accept the same proof?

**Strongest failure reason:** Recomputing the answer is cheaper and simpler, or buyers already trust the data provider, making the proof commercially redundant.

**My top three**

| Category | Recommendation | Conviction and decisive objection |
|---|---|---|
| **Strongest company opportunity** | **Confidential borrowing-base network** | Medium conviction. Financing and servicing are established needs; the missing evidence is lender willingness to accept and pay for portable collateral certificates. |
| **Strongest technically original protocol** | **Confidential multilateral clearing** | Medium conviction on usefulness, lower on defensible novelty until its abort handling, leakage, and default mechanisms are specified. Plain netting is already occupied. |
| **Strongest privacy opportunity** | **Confidential borrowing-base network** | It protects commercially sensitive records without requiring payment anonymity or a large anonymity set. The privacy guarantee is limited but directly useful. |

I would choose **confidential borrowing-base enforcement** as the leading direction, with **confidential clearing** as the more ambitious protocol alternative. Neither needs a claim that Arc uniquely enables the cryptography; Arc’s advantage is connecting financial evidence to actual USDC obligations and capital.

The most important missing insight is whether **two independent lenders will recognize the same confidential asset certificate and encumbrance record**. If they will, this can become a network with increasing value as participants join. If they will not, better cryptography will not rescue the company thesis.
