# Original research prompt

Editorial note: copied from the user message; transport escaping is normalized for readability in research-01 only. `prompt-source.txt` retains the accessible source text, subject to privacy redaction.

Act as a venture researcher, Stellar ecosystem analyst, fintech product strategist, and technically rigorous founder. Conduct a deep, current, source-backed investigation into the best **full product or company** I could build with Stellar as a core part of its architecture.

My goals are related but distinct:

1. Find a product with real users, a recurring problem, a credible business model, and the potential to become a substantial company. It may eventually be multichain or include offchain infrastructure.
2. Identify a concrete first slice of that product that could plausibly fit a **$5,000 Stellar Instaward**, without shrinking the overall company idea into a grant demo.

I am particularly interested in **real-world asset tokenization and distribution, payments, financial privacy, and useful agent-driven financial workflows**. The recent MetaMask integration with Stellar may create opportunities. Investigate those themes deeply, but do not force the final recommendation into any one of them. Surprise me if another Stellar-specific opportunity is stronger.

I want products people or businesses would use repeatedly. Avoid ideas that are merely a smart contract, wallet connection, generic payment button, token issuance wizard, privacy wrapper, AI chatbot, or hackathon feature.

## Research principles

- Browse current sources. State when each important platform or program fact was checked.
- Prefer primary sources: Stellar and MetaMask documentation, the SCF handbook and funded-project database, live product sites, public repositories, deployed contracts, transactions, customer documentation, pricing pages, and direct user discussions.
- Distinguish **verified fact**, **vendor claim**, **user anecdote**, **reasonable inference**, and **unvalidated hypothesis**.
- Verify whether a product is live on Stellar mainnet, only on testnet, a developer preview, merely announced, or no longer maintained.
- Do not equate grant funding with traction, tokenization volume with active product usage, wallet support with dapp compatibility, or technical feasibility with customer demand.
- Search aggressively for direct competitors and previously funded Stellar projects. A missing search result is not evidence that a market is empty.
- Do not invent interviews, TAM estimates, revenue, active users, transaction counts, partnerships, regulatory permissions, or grant eligibility.
- If a strong business is better as a multichain product with Stellar as one important rail, say so. Explain what must stay on Stellar for the product to create genuine ecosystem value.
- Continue the research until you can make a defensible recommendation. Do not stop after producing a list of attractive-sounding ideas.

## First: verify the actual Stellar opportunity surface

Build a current, concise map of what is usable today:

- Stellar classic assets versus Soroban contracts; Stellar Asset Contracts; trustlines, account reserves, asset authorization, freeze and clawback; smart accounts and sponsorship.
- USDC and relevant stablecoins, on/off-ramps, anchors, crossborder distribution, interoperability and crosschain transfers.
- Existing RWA issuers and products, but distinguish issuance from actual accessibility, composability, distribution and secondary use.
- Payments infrastructure for merchants, businesses, contractors and consumers.
- Privacy primitives and products, especially Stellar Private Payments, Confidential Tokens and ZK verification. Specify exactly what privacy property each provides, who still sees what, audit status, and whether real assets can safely use it on mainnet now.
- Agent infrastructure: Stellar CLI and agent tooling, policy controls, x402, MPP, smart account permissions, and currently deployed services.
- MetaMask’s Stellar integration: supported assets and operations, dapp signing, Soroban authorization, supported platforms and networks, onboarding limitations, account activation, trustlines and reserves.
- **Do not conflate MetaMask’s Stellar wallet integration, MetaMask Agent Wallet, and the separately funded Stellar AI Agent Kit.** Verify whether MetaMask Agent Wallet actually supports Stellar before suggesting a combined product.

Useful starting points, to verify rather than assume:

- [https://developers.stellar.org/](https://developers.stellar.org/)
- [https://developers.stellar.org/docs/build/apps/privacy](https://developers.stellar.org/docs/build/apps/privacy)
- [https://developers.stellar.org/docs/build/agentic-payments](https://developers.stellar.org/docs/build/agentic-payments)
- [https://github.com/MetaMask/connect-stellar](https://github.com/MetaMask/connect-stellar)
- [https://support.metamask.io/configure/networks/stellar/](https://support.metamask.io/configure/networks/stellar/)
- [https://docs.metamask.io/agent-wallet/reference/supported-chains/](https://docs.metamask.io/agent-wallet/reference/supported-chains/)
- [https://stellar.org/solutions/real-world-assets](https://stellar.org/solutions/real-world-assets)
- [https://communityfund.stellar.org/](https://communityfund.stellar.org/)
- [https://github.com/stellar/scf-handbook/blob/main/scf-awards/instawards/official-rules.md](https://github.com/stellar/scf-handbook/blob/main/scf-awards/instawards/official-rules.md)

## Second: find market demand and the gaps between infrastructure and usable products

Investigate at least these opportunity areas, then follow stronger evidence into other areas:

1. **RWA access and utility:** issuer operations, investor onboarding, eligibility, distribution, settlement, reporting, collateral use, redemption, and the gap between “tokenized asset exists” and “someone can use it.”
2. **Payments:** crossborder B2B, contractor and creator payouts, collections, merchant workflows, remittances, FX, refunds, reconciliation, treasury and cash-to-crypto or crypto-to-cash access.
3. **Privacy for real financial workflows:** payroll, supplier payments, treasury, donations, investment positions, sensitive business relationships and selective disclosure. Test whether privacy is necessary to unlock a paying customer, and whether current production-grade primitives can deliver it.
4. **Agent-driven commerce and finance:** paid APIs, procurement, payment approval, spending policy, audit trails, service delivery verification and human oversight. Seek the user problem behind the “agent payments” narrative.
5. **Consumer products unlocked by easier wallet access:** examine whether MetaMask materially changes acquisition or conversion for a particular user group. Do not assume an existing MetaMask user automatically becomes a Stellar user.

Compare Stellar products with strong products on Base, Ethereum, Solana, Avalanche and relevant traditional fintech markets. Include products with actual distribution and paying customers where evidence is available. Inspect ETHGlobal projects and SCF winners for ideas and competitive threats, but treat awards as evidence of building activity, not demand.

Search for customer pain in credible direct sources: developer requests, support forums, app reviews, issuer or merchant documentation, pricing complaints, operational workarounds, and public case studies. Prioritize problems where customers already spend money or significant staff time.

For regulated or institution-facing ideas, identify **who would need a license, issuer relationship, custodian, KYC/AML program, banking partner, or legal approval**. Do not casually assign those responsibilities to “the protocol.” Separate what a startup can build independently from what requires a commercial partner.

## Third: generate and eliminate company theses

Produce **12–15 meaningfully different full-product opportunities**. For each, state:

- First specific customer and buyer
- Painful job and current workaround
- Complete product experience and reason for repeat use
- What Stellar uniquely improves
- Why a customer would choose this over existing products
- Revenue model and realistic path to distribution
- Essential partners, permissions and technical dependencies
- Whether and why it should become multichain
- Strongest competitor or substitute
- Strongest reason the idea may fail
- Confidence in the evidence

Then eliminate weak ideas explicitly. Reject ideas with no credible buyer, no distribution path, no repeat use, a dependency on unavailable privacy infrastructure, an implausible regulatory path, or no reason to use Stellar.

## Fourth: perform serious diligence on the best candidates

Select **4–5 finalists**. Compare them on customer pain, willingness to pay, market size and expansion, distribution, recurring use, Stellar advantage, competitive intensity, technical feasibility, regulatory complexity, defensibility and venture potential. Explain the evidence behind judgments instead of hiding uncertainty behind numeric scores.

For the **top three**, provide a founder-level brief:

1. One-sentence thesis and a concrete example user journey
2. The narrow initial customer segment and why it is reachable
3. Existing workflow, its cost or friction, and direct alternatives
4. Full product surface: user-facing application, operations, integrations and necessary onchain components
5. What is genuinely hard to build and what should be reused
6. Stellar-native architecture; where classic assets, Soroban, SAC, anchors or external systems belong
7. Privacy and data model, including what is public and what remains confidential
8. MetaMask integration only if it materially improves the journey and is technically supported
9. Business model, possible pricing, and main unit-economics constraints
10. Go-to-market path to the first 10 and first 100 real users or business customers
11. Multichain expansion strategy and what would remain valuable on Stellar
12. Defensibility, including data, workflow lock-in, distribution, partnerships or network effects
13. Principal legal, security, dependency and adoption risks
14. The smallest demand tests that could falsify the thesis before a major build

Do not call a concept VC-backable unless you can explain how it grows beyond a small Stellar-only audience and why a funded competitor cannot simply copy its main feature.

## Fifth: separate the company from the Instaward

Only **after selecting the best company thesis**, consult the current official Instawards rules and produce a separate, realistic first sprint. Confirm the actual application path, Ambassador Chapter involvement, award range, currency, time limit, eligibility and deliverable expectations. Do not assume a $5,000 award is automatic.

Propose a scope that could be completed within the official sprint window and meaningfully de-risk the chosen product. Include:

- One concrete product or technical deliverable
- A specific user or pilot it serves
- Measurable acceptance criteria
- A credible budget for an approximately $5,000 request
- What evidence would justify a follow-on Instaward, SCF Build application, customer revenue or investment

Do not use the Instaward to fund vague research or claim that the entire venture will be built for $5,000. Do not write the final grant application yet; I want to choose and validate the idea first.

## Required output

Start with a direct executive verdict: **best company thesis, best backup, and the main reason you might be wrong**.

Then provide:
A. Verified Stellar capability and maturity map
B. Competitive landscape and evidence of customer demand
C. Longlist with explicit eliminations
D. Comparison of finalists
E. Detailed briefs for the top three
F. Recommended Instaward-sized first sprint for the winner
G. Unanswered questions and the exact evidence needed to resolve them

Link each material factual claim to its source. Include an evidence-quality note for major market claims. Be candid if the strongest conclusion is that no currently verified Stellar-specific opportunity satisfies the venture standard, or that a multichain-first company with Stellar as a core rail is the better strategy.

Research and analysis only. Do not deploy contracts, transact, contact organizations, or submit any application.
