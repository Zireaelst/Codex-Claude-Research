# Original user-facing research exchange

Contains the accessible user messages and assistant commentary/final responses in order. Internal reasoning, tool payloads, runtime configuration and credentials are excluded. Artifact links may be relocated for this archive.


## User — user

Act as a venture researcher, crypto product strategist, and technical diligence partner. Investigate what substantial company I could build starting on Stellar and potentially expanding across chains.

I want a complete product people repeatedly use and pay for—not a hackathon feature, generic wallet, tokenization dashboard, yield aggregator, x402 wrapper, or a privacy demo with no customer.

Research FOUR opportunity areas with equal seriousness:

A. Agentic commerce and payments:
Delegated wallets, bounded spending, agent purchasing, human approvals, agent-to-human requests, paid tools and services, fulfillment verification, refunds, seller software, and agent financial operations.

B. RWA and tokenization:
Distribution, investor access, secondary liquidity, price discovery, subscriptions and redemptions, collateral use, servicing, treasury use, and the gap between tokenized supply and genuinely usable assets.

C. DeFi, liquidity, and yield:
DEX and LP products, lending and borrowing, vaults, fixed versus variable yield, risk management, liquidity routing, RWA-backed strategies, and ways to make existing Stellar assets more useful. Investigate where yield actually comes from.

D. Cryptographic privacy:
Private payments, confidential balances, private agent purchases, private treasury actions, private RWA ownership or trading, and privacy-preserving DeFi. Consider both a standalone privacy product and privacy as a decisive feature of a larger product. Investigate genuine cryptographic guarantees rather than calling encryption of a database, a fresh wallet address, or an undisclosed UI field “private.”

Also investigate intersections: for example, an agent that can buy without exposing a user's financial history; a private payment with enforceable spending limits; confidential B2B settlement; privacy-preserving RWA access; or an LP/DeFi product that protects a commercially sensitive position. Do not force a combination if a focused product is stronger.

Starting references for the agentic area:
- Omamoris: https://ethglobal.com/showcase/omamoris-rn3nc
  Source: https://github.com/juanmaagd/yakusoku
- Yohaku: https://ethglobal.com/showcase/yohaku-m2d72
- OnchainRouter: https://ethglobal.com/showcase/onchainrouter-8r4jm

These are inspiration and competitive prior art, not templates to port to Stellar. Search well beyond them.

Research method:

1. Review relevant ETHGlobal winners and finalists across agentic payments, RWA, DeFi, and privacy. Include work on Ethereum, Base, Solana, Sui, Arc, Hedera, and other networks. Inspect the strongest projects' repositories and current product status. Verify award labels. Separate hackathon prototypes, testnet demos, deployed products, funded companies, and evidence of paying users.

2. Map the existing Stellar ecosystem and serious competitors elsewhere. Cover wallets, agent tools, x402/MPP, DEXs, LPs, lending markets, vaults, RWA issuers and distributors, and privacy systems. For privacy, examine relevant prior art such as privacy pools, shielded assets, confidential tokens, stealth-address payments, selective disclosure, ZK-based eligibility, and private execution. Include Stellar Private Payments, Moonlight, and confidential-token work, but verify their current maturity and supported assets. Compare with established privacy products on other chains rather than declaring a gap because something is new to Stellar.

3. Verify the technical reality using official documentation, repositories, audits, and deployed-product evidence. Distinguish Stellar Classic assets, SDEX and built-in LPs from Soroban tokens, contracts and liquidity venues. Check asset permissions, issuer restrictions, oracle availability, custody, trustlines, wallet support, MetaMask interoperability, agent signing, and mainnet status. Do not assume a tokenized RWA is freely transferable or usable in a pool. Do not assume that a privacy preview safely supports production USDC or an existing RWA.

4. For each serious privacy direction, write a precise threat model. State separately whether the design hides:
   - Sender identity
   - Recipient identity
   - Amount and asset
   - Balances
   - Transaction links and spending history
   - Commercial intent or agent instructions
   - Timing, network metadata, and cash-in/cash-out links

   Say who can still observe each item: public chain viewers, counterparties, issuers, relayers, RPC providers, application operators, compliance officers, and anyone holding a viewing key. Examine anonymity-set size, proof generation cost, key recovery, selective disclosure, revocation, and the trust assumptions of ZK, MPC, FHE, TEEs, or external privacy networks where relevant. Never call an approach “fully private” unless its defined threat model supports that claim.

5. Investigate actual economic demand. For DeFi and LP ideas, examine trading volume, fee income, liquidity depth, slippage, incentives, impermanent loss, liquidation depth, and dependence on subsidized yield. For RWA ideas, distinguish total tokenized AUM, accessible inventory, eligible holders, actual secondary trading, redemption rights, and usable collateral. For agentic ideas, distinguish genuine third-party purchases from demos and self-payments. For privacy ideas, identify a specific buyer harmed by today's information leakage and establish why they would pay to change it. State when reliable data is unavailable.

6. Generate 14–18 DISTINCT full-product theses across the four areas and their intersections. For each, specify:
   - Exact first user and economic buyer.
   - Recurring job and current workaround.
   - End-to-end product experience, including failure and recovery.
   - Why this is an independent company rather than a feature, contract, or SDK.
   - Why Stellar is a good starting point and whether multichain expansion is required.
   - Closest competitors and the specific unmet need.
   - Revenue model, distribution channel, technical dependencies, and principal risks.
   - Strength of evidence for the problem versus evidence that a new entrant can win.
   - For privacy ideas: the exact guarantee, the remaining leakage, and whether real assets can be used today.

7. Eliminate weak theses explicitly. Challenge generic agent wallets, x402 directories, undifferentiated tokenization platforms, APY dashboards, emission-funded LP farms, vaults with unclear yield sources, “private” apps that only hide data in their frontend, and shielded pools that require liquidity or issuer support they cannot obtain. Do not replace weak demand evidence with ecosystem enthusiasm or grant awards.

8. Select 4–5 finalists spanning materially different directions. Include at least one serious privacy candidate and strong candidates from agentic products, RWA, and DeFi/liquidity—unless the evidence genuinely rules out an area. For each finalist, provide:
   - A concrete weekly user journey and purchasing reason.
   - Technical architecture and the genuinely difficult mechanism.
   - Asset and money flows, custody, permissions, trust assumptions, and failure recovery.
   - Liquidity, issuer, privacy-infrastructure, or partner dependencies.
   - Closest incumbent and the narrow reason a customer would switch.
   - First distribution channel and a realistic path to 5–10 buyer conversations.
   - Pricing hypothesis, venture-scale expansion path, and three observations that would kill the idea.
   - A clearly separated view of what is buildable now versus what depends on future infrastructure.

My possible access is to Stellar DevRel, not yet to committed customers, issuers, market makers, or payment operators. Treat introductions as possible, not secured. Identify when lack of buyer, asset, liquidity, or infrastructure access makes an idea unsuitable for me now.

9. Make a decision. Rank finalists separately for venture potential, current customer evidence, founder-accessible entry, Stellar advantage, technical defensibility, and delivery risk. These rankings may differ. Recommend one direction only if the evidence supports it; otherwise state exactly what evidence is missing. Give the smallest customer-discovery or technical experiment that could change your decision. Only after selecting the company direction, briefly suggest what a small Stellar Instaward-sized implementation could validate. Grant fit must not drive the company recommendation.

Write in English. Be analytical and opinionated. Cite primary sources next to consequential claims. Label verified facts, vendor claims, and your inferences. Do not spend space on application deadlines, demo scripts, grant checklists, or generic market-size figures. I want a decision-quality investigation of products people might actually use.


## Assistant — commentary

I’m reopening the conclusion rather than carrying forward the earlier payments recommendation. I’ll use the brainstorming and parallel-research workflows to examine agentic commerce, RWA, DeFi/liquidity, and cryptographic privacy with equal seriousness. DeFi economics and precise privacy threat models need substantial new diligence; I’ll also inspect the three projects you named and verify what their awards and implementations actually demonstrate.


## Assistant — commentary

The evidence is separating “assets and tools exist” from “a new company can win.” The three agent projects you named are finalist prototypes with test or author-controlled activity, rather than verified paying demand. On the DeFi side, there is measurable borrowing and trading, but a documented RWA-oracle manipulation incident makes liquidity-aware risk controls a more serious candidate than another yield interface.


## Assistant — commentary

Direct market snapshots show why RWA liquidity needs caution: some pools hold roughly $2 million while reporting less than $100 in daily trading. That can support issuance or treasury storage without supporting a market-making business. I also found existing Stellar risk-scoring and institutional liquidity projects, so neither a risk dashboard nor “managed LPs for Stellar” is an uncontested opportunity.


## Assistant — commentary

Privacy is a real product category, but its maturity differs sharply by system. Current Stellar privacy previews still do not justify putting business funds into them; meanwhile, Base confidential tokens, Solana confidential transfers, and Aleo payroll provide more advanced comparators. The remaining question is whether a specific customer needs guarantees these products cannot already provide—and whether that customer gives Stellar a meaningful role.


## Assistant — commentary

I’m narrowing to five different businesses: DeFi risk operations, RWA cash-readiness operations, bounded agent procurement with recourse, issuer liquidity operations, and confidential business disbursements. None yet has verified demand for this founder’s proposed product. The report will rank commercial potential separately from accessible entry, and distinguish a worthwhile discovery test from a justified product build.


## Assistant — commentary

The clearest distinction is who has a recurring decision to make and authority to act on it. The leading hypothesis now targets an earn-product operator who must assess collateral, exits and permissions, then approve actions and account for the outcome. Before calling that a company opportunity, we still need a buyer who can show the work, name the missing control, and pay for it.


## Assistant — commentary

The full draft now covers 16 company theses, five finalist briefs, separate rankings, and privacy threat models by information type and observer. I’m checking the findings that could change the decision: RWA quote arithmetic, disabled collateral configurations, privacy asset support and audit scope, and whether the strongest agent prototypes enforce their stated controls in code.


## Assistant — commentary

The final checks confirmed the quote calculations and found one counting correction: the trade sample contains 33 distinct account addresses, plus pool-side records—not 34 addresses. Code inspection also exposed a useful recovery boundary: a relay returning `charged:false` cannot prove that a remote service never charged before the response failed. The report now includes both qualifications, along with the preserved public snapshots.


## Assistant — final_answer

**Best company hypothesis:** a **liquidity-aware risk and incident operations platform** for businesses offering onchain earn or lending products.

**Best backup:** **RWA execution and cash-readiness software** for eligible treasurers and distributors managing multiple issuers.

**Main reason I might be wrong:** the apparent gap may belong inside existing risk advisers, custody platforms or issuer systems. Neither hypothesis has verified purchase intent for a new entrant.

**My decision is to validate the first direction—not commit to a major build yet.**

[Read the full investigation](../research-02/report.md). It contains **16 distinct company theses, explicit eliminations, five detailed finalist briefs, separate rankings, privacy threat models, interview routes and a small implementation proposal**. [Preserved evidence and methodology](../research-02/evidence/README.md) accompany it.

All capability and product-status findings were checked **20 October 2026**, with source/snapshot dates distinguished in the report.

The strongest findings:

- **Agentic commerce has substantial technical prior art, but weak verified demand for the proposed entrant.** Omamori, Yohaku and OnchainRouter are verified finalists; their demonstrated financial flows use testnets. Yohaku discloses generated demand, while OnchainRouter’s author owns its six tools. These are meaningful implementations, not evidence of recurring independent purchases. [Omamori](https://ethglobal.com/showcase/omamoris-rn3nc), [Yohaku](https://ethglobal.com/showcase/yohaku-m2d72), [OnchainRouter](https://ethglobal.com/showcase/onchainrouter-8r4jm).

- **Budgets, approvals, receipts and refunds are already competitive features.** Ramp documents agent spending controls and accounting; Stripe documents machine-payment refunds, reconciliation and settlement. An independent company would need to own service-specific acceptance, rework and enforceable commercial recourse. [Ramp](https://agents.ramp.com/), [Stripe](https://docs.stripe.com/payments/machine).

- **RWA inventory is much more substantial than observed secondary activity.** The sampled USDY/USDC Aquarius pool reported approximately **$2.02 million liquidity but only $91 in daily USDC-side volume**. An unsigned quote to sell 100,000 USDY returned approximately **10.14% below sampled marginal spot**. That comparison is against pool spot—not issuer NAV—and is an estimate, not a completed trade. [Primary venue data](https://amm-api.aqua.network/api/tickers/), [quote methodology and records](../research-02/evidence/README.md).

- **DeFi risk is an operating problem beyond contract audits.** The documented YieldBlox incident involved thin-market RWA pricing feeding a community-configured lending pool. That supports investigating realizable exits, oracle dependencies and response authority; it does not establish a budget for this startup. [First-party incident analysis](https://blockaid.io/blog/73-quarantined-how-blockaid-and-stellar-validators-contained-a-10m-price-manipulation-attack).

- **Privacy deserves serious consideration, with deployment-specific limits.** Stellar Private Payments and Confidential Tokens remain unaudited previews unsuitable for real assets. Meanwhile, Inco documents Base-mainnet USDC configuration, and Solana documents enabled confidential-transfer proof support. Neither fact establishes that every wallet, asset, recovery path or application is production-safe. [Stellar status](https://developers.stellar.org/docs/build/apps/privacy), [Inco configuration](https://docs.inco.org/ctoken/configuration), [Solana](https://solana.com/docs/tokens/extensions/confidential-transfer/transfer-tokens).

The five finalists resolve into different businesses:

| Finalist | Repeated outcome customers would buy | Decisive unresolved issue |
|---|---|---|
| **DeFi risk and incident operations** | Assess exposure, approve permitted responses, reconcile outcomes and unresolved losses | Does an actual operator own this workflow and budget? |
| **RWA cash readiness** | Choose redemption or market exit against real cash deadlines | Is the job frequent enough beyond issuer portals? |
| **Bounded agent procurement and recourse** | Purchase accepted third-party work and resolve failed delivery | Are outside purchases and costly unresolved failures recurring? |
| **Issuer liquidity operations** | Manage issuer-owned inventory against depth, risk and net-performance targets | Can you secure a paid mandate and demonstrate profitable execution? |
| **Confidential business disbursements** | Complete private contractor/vendor payments with recovery and accounting | Will buyers pay beyond bank payouts, and will normal cashout preserve the required privacy? |

Their rankings differ. These are analytical judgments about potential, not measured probabilities; **none has verified customers for this proposed startup**.

| Finalist | Venture potential | Customer-job evidence | Accessible entry | Stellar advantage | Potential technical defensibility | Delivery risk* |
|---|---:|---:|---:|---:|---:|---:|
| DeFi risk operations | 1 | 1 | 1 | 1 | 2 | 3 |
| RWA cash readiness | 2 | 4 | 2 | 2 | 4 | 1 |
| Agent procurement | 4 | 5 | 3 | 5 | 5 | 2 |
| Issuer liquidity operations | 5 | 2 | 5 | 3 | 1 | 4 |
| Confidential disbursements | 3 | 3 | 4 | 4 | 3 | 5 |

*For delivery risk, 1 means lowest.*

The leading company would serve a **financial decision owner**, such as the COO, CTO or risk lead of an existing earn business that controls its allocations. A wallet that merely links users to a lending pool might have neither responsibility nor purchasing authority.

Its complete product would connect:

**Exposure → exit and permission analysis → customer policy → human-approved response → execution evidence → reconciliation and incident closure.**

The hard mechanism is trustworthy financial semantics: distinguishing NAV from sale proceeds, normal quotes from stressed exits, configured collateral from enabled runtime markets, and a proposed action from one the customer can legally and technically execute. Defensibility would have to accumulate through validated integrations, operating history and embedded workflows. A risk score or dashboard alone would be readily copied.

Stellar is a useful starting specialization because classic liquidity, Soroban markets, issuer controls and RWA redemption constraints intersect there. **Multichain expansion is necessary for a substantial company.** Real Stellar exposures and customer actions must remain supported; a decorative Stellar transaction would contribute little.

For privacy, the report separately maps sender, recipient, amount, asset, balances, history, instructions, metadata and cash edges across public observers, counterparties, issuers, operators and key holders. A particularly important commercial baseline is that **aggregate funding followed by ordinary bank payouts already keeps individual salaries off the public chain**. Cryptographic disbursements need a customer whose requirements exceed that baseline.

MetaMask also changes less than a superficial thesis suggests: its Stellar wallet and signing adapter are distinct from **MetaMask Agent Wallet**, whose documented coverage is EVM. The separately funded Stellar AI Agent Kit is another product again. [Stellar adapter](https://github.com/MetaMask/connect-stellar), [Agent Wallet coverage](https://docs.metamask.io/agent-wallet/reference/supported-chains/).

The smallest experiment that could change the decision is:

1. Reach **5–10 qualified operating roles**, using possible DevRel introductions and public professional outreach. Introductions are not assumed.
2. Obtain consented, redacted examples of recent allocation, listing or failed-exit decisions.
3. Replay two cases through a read-only decision workflow and compare it with the customer’s existing tools.
4. Seek a **priced pilot decision**, not hypothetical enthusiasm.

An approximately **$5,000 implementation** could then build one operator’s source-backed risk-decision casebook with explicit blocked, stale, unavailable-exit and loss states. It would validate one repeatable workflow—not fund an autonomous treasury platform, managed fund or production privacy system.

No organizations were contacted, contracts deployed, transactions submitted or applications filed.
