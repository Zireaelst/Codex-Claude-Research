# EVM Launchpad Project Idea

**A standalone, v4-first programmable meme and creator token launchpad, with a separate instant v3 launch path.**

This is a complete product specification and coding-agent handoff, not an existing application or an audit. Start a **new implementation repository**. Do not continue, import, rename or deploy the historical Arc application. Arc Studio, Circle wallets, Arc gas semantics, Arc contracts and grant requirements are not dependencies.

**Türkçe özet:** Yeni proje EVM ağları içindir. Ana deneyim bonding curve → kurallı Uniswap v4 havuzu; ikinci seçenek doğrudan Uniswap v3 havuzudur. Tam ürün; keşif, trading, hook seçimi, creator gelirleri, ödüller, mevcut token havuzları ve agent API içerir. Bu klasör başka bir kodlama agentına doğrudan verilebilir.

## Product commitment

Creators design a token's launch and bounded trading rules. Traders can understand those rules before buying. Contributors, liquidity providers and creators can claim what they have earned through the same application. Community funding is optional; it is not the product's organizing principle.

- **Programmable launch:** curve price discovery, automated graduation attempt, locked founding v4 liquidity, immutable launch configuration.
- **Instant launch:** immediate v3 pool and locked founding liquidity; no v4 hooks and no migration.
- **Existing-token pools:** separate v4 market creation, no minting, no curve, no claim of token-team endorsement, removable external LP positions.
- **Complete application:** board, launch wizard, token terminal, pool terminal, rules inspector, earnings, funded rewards, optional community jobs, creator dashboard, safe unsigned-transaction API.
- **Multi-network product:** Base is the initial engineering reference; additional EVM networks are independent deployments behind verified network manifests. Supporting a network is not the same as bridging a token.

## Read in this order

1. [Product requirements and scope](specs/01-product.md)
2. [User journeys and interface](specs/02-journeys.md)
3. [Economics and numerical specification](specs/03-economics.md)
4. [Lifecycles and recovery](specs/04-lifecycles.md)
5. [Rules engine and module catalog](specs/05-rules.md)
6. [Contracts and interfaces](specs/06-contracts.md)
7. [Networks and dependencies](specs/07-networks.md)
8. [Data, APIs and agent integration](specs/08-data-api.md)
9. [Security, authority and operations](specs/09-security.md)
10. [Acceptance matrix](specs/10-acceptance.md)
11. [Implementation work packages](agent/IMPLEMENTATION_PLAN.md)
12. [Ready-to-use agent prompt](agent/START_HERE.md)
13. [Decisions and boundaries](specs/11-decisions.md)
14. [Sources and evidence limitations](references/SOURCES.md)

[AGENTS.md](AGENTS.md) governs implementation intent. [STATUS.md](agent/STATUS.md) is the progress template; every item initially has **NOT STARTED** status.

## What is authoritative?

This package records the owner's direction on 2026-10-28 and explicit design defaults chosen to make it executable. All product parameters below are **our proposed policy**, not claims about competitors. Requirement IDs are stable. If prose conflicts, security/solvency constraints win; the agent must log and resolve the conflict rather than silently choose a different economic model.

"Complete product" describes the target scope. Work packages describe dependency order, not reduced releases. Do not declare the product complete after building a factory, a landing page, mocked swaps, or only one launch path.

This documentation does not authorize live deployment, real-value spending, token issuance, paid infrastructure or publication of an application. Local development, local-chain tests and implementation pull requests are distinct from public deployment and require their own execution instruction.
