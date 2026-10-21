# Research 04: Venture-scale diligence — payment operations

## Original prompt

Source: this conversation, message timestamp `2026-10-18T22:00:59.286Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

Act as a venture researcher, product strategist, and technical founder evaluating what substantial company could be built on Arc.

I am looking for a **full product with credible venture-scale potential**, not a hackathon demo, a single smart-contract feature, or a generic copy of an existing crypto app. The product should solve a real, recurring problem for identifiable users. Arc should give it a meaningful advantage, but the business may become multichain when that helps users or distribution.

Do not start by assuming that the answer is a memecoin launchpad, privacy app, agent marketplace, payment splitter, or any other category discussed previously. Investigate the market and let evidence change the direction.

## Core question

**What should a founder build on Arc today that people would actually use, that the Arc ecosystem would benefit from, and that could plausibly become a venture-backed company?**

Treat “venture-backed” as a demanding hypothesis: a large or expanding market, a credible initial customer, repeated use, a way to reach those customers, a business model, and a defensible path beyond one chain. Do not call an idea “VC-scale” merely because its theoretical TAM is large.

## Research scope

1. Map Arc’s current capabilities and constraints using current official documentation and verifiable deployments. Include USDC payments and gas, wallets and onboarding, crosschain movement, liquidity, smart contracts, agent payments, stablecoin FX, tokenized assets, and any limitations that materially affect product design. Distinguish what is live on mainnet from testnet, announced, planned, or demonstrated only.

2. Map products already operating or being built on Arc. Inspect actual product sites, documentation, repositories, contract addresses or transactions where available. Include launchpads, trading products, payments, creator tools, commerce, SaaS billing, treasury, marketplaces, agent infrastructure, and other relevant categories. Do not infer a market gap from a missing search result. Distinguish a live product with observable usage from a landing page or hackathon submission.

3. Look outside Arc for strong products and unmet demand across Ethereum, Base, Solana, Avalanche, Arbitrum, Optimism, BNB Chain, and relevant non-crypto markets. Study products that have genuine users, transactions, revenue, distribution, or strong community adoption. ETHGlobal and other hackathon winners may supply ideas, but do not treat prizes as proof of demand. Identify which user behavior or business model might transfer to Arc and which would fail there.

4. Search for evidence of user pain, not just founder pitches: product reviews, support discussions, developer forums, public customer requests, workflow complaints, usage data, pricing, and credible adoption signals. Label anecdotes as anecdotes. Do not fabricate interviews, revenue, user counts, TAM figures, or competitor gaps.

Explore multiple categories, including consumer and social products, crypto-native products, creator commerce, developer tools, SMB workflows, crossborder work and payments, agent-to-agent commerce, financial operations, privacy, and marketplaces. Do not force equal coverage if evidence clearly favors some categories.

## Product standard

A candidate must be describable as an end-to-end product:

- Who is the first specific user or buyer?
- What job are they trying to complete, and what do they use now?
- What is the complete user journey, from discovery or onboarding to repeat use?
- Why would they switch, pay, or invite others?
- What is the product’s recurring use loop?
- What creates distribution: an existing workflow, integrations, community, marketplace liquidity, content, network effects, or another concrete channel?
- What does Arc improve for the user, rather than merely for the pitch deck?
- What happens if the product supports other chains?
- What business model could work, and what are its likely costs or margins?
- What becomes difficult for a fast follower to copy?
- Which dependency could kill the company: liquidity, regulation, licensing, external data, dispute resolution, user trust, platform access, or another bottleneck?

Reject ideas whose main description is “an escrow contract,” “a private payment,” “a launchpad with a different bonding curve,” “an AI wrapper,” or “an aggregator” unless you can show the broader product, real user pull, and a differentiated distribution path.

Previous research over-weighted clever mechanisms, speculative privacy, grant scoring, and demo feasibility. Correct for that bias. Technical depth is welcome when it creates a user advantage or defensibility, but cryptographic complexity alone is not a product.

## Method and evidence rules

- Search broadly before selecting favorites. Actively look for competitors that disprove each proposed gap.
- Prefer primary sources: official docs, live apps, public repositories, verified contracts and transactions, company pricing pages, product changelogs, and direct user discussions. Use secondary sources only for context or leads.
- For every important factual claim, give a direct source link. State when a claim is an inference.
- Separate **verified fact**, **company claim**, **user anecdote**, and **your hypothesis**.
- Record the date on which current ecosystem facts were checked, but do not spend the report on deadlines or grant logistics.
- Where possible, distinguish supply-side activity from real demand: token deployments are not equivalent to active traders; listed agents are not equivalent to paid usage; TVL is not equivalent to revenue.
- If the evidence is too thin to call an opportunity open, say so. A crowded category can still be attractive if there is a specific underserved customer and a credible route to distribution.
- Do not assume that building on Arc must mean remaining Arc-only forever.

## Analysis to produce

**A. Market map.** A concise map of Arc’s relevant infrastructure and existing product categories, with the strongest incumbents and apparent gaps. Mark the confidence level of each gap.

**B. Opportunity longlist.** Generate 10–15 meaningfully different full-product theses. For each, provide the first customer, core workflow, comparable products, Arc advantage, potential expansion beyond Arc, business model, biggest obstacle, and the strongest reason to reject it. Avoid cosmetic variations of the same idea.

**C. Shortlist.** Select the 4–5 strongest theses using evidence, not arbitrary enthusiasm. Compare them on:
- Severity and frequency of user pain
- Evidence that users already spend money or time on the problem
- Clear initial customer and distribution path
- Product depth and repeat use
- Arc-specific advantage
- Multichain expansion potential
- Revenue quality and plausible venture scale
- Competitive intensity and defensibility
- Technical and regulatory execution risk

Use qualitative judgments with supporting evidence. If you use numerical scores, explain the assumptions; do not let a score conceal weak evidence.

**D. Deep diligence on the top three.** For each, write a compact founder brief:
1. One-sentence product thesis
2. Exact initial customer and current alternative
3. The user journey and repeat-use loop
4. What the first complete version of the product includes
5. Why Arc matters and whether other chains belong in the product
6. Direct competitors and the proposed wedge
7. Pricing/revenue model and likely unit-economics constraints
8. Go-to-market path to the first 10, 100, and 1,000 active users or paying customers; distinguish a testable plan from evidence
9. Defensibility if a funded competitor copies the features
10. Key technical architecture and external dependencies, only to the depth needed to judge feasibility
11. Risks, failure modes, and explicit kill criteria
12. The cheapest real-world tests that would validate or falsify demand before a major build

**E. Final judgment.** Recommend one thesis, one credible backup, and explain why the others lose. Be willing to conclude that **no clearly venture-grade Arc-native opportunity is yet established** and recommend a multichain-first approach if that is what the evidence shows. Tell me what new evidence would change your recommendation.

Start your response with a short, direct investment-style verdict. Then provide the supporting research. I care much more about the quality of the reasoning and evidence than the number of ideas.

Do **not** optimize for an Arc Microgrant, propose a submission schedule, produce a demo script, or turn this into a grant application. Do not build anything or perform onchain transactions. Complete the research autonomously using reasonable assumptions; only ask me a question if the answer is indispensable.

