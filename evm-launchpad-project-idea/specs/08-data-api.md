# Application, indexing and integration architecture

## Suggested implementation layout (new repository)

apps/web: React/TypeScript frontend; apps/api: typed HTTP service; apps/indexer: chain event ingestion; packages/contracts: Foundry contracts and tests; packages/sdk: generated ABI clients/math/schema; packages/config: validated network manifests; packages/db: schema/migrations; packages/ui: reusable components; docs: specification/evidence/runbooks. Pin compatible tool versions at implementation start and commit lockfiles. PostgreSQL is the durable read model; Redis may accelerate quotes/rate limits but is never accounting authority. Object storage holds media; contracts store content hashes/URIs.

## Indexer

Index registry creation events, curve events, canonical pool swaps, NFT/liquidity events, fee claims, funding and contribution events. Backfill bounded block ranges from verified deployment blocks. Store chainId, block number/hash, tx hash and log index with a unique constraint. Retain checkpoints, parent hashes and finalized status. Reorg rollback deletes/rebuilds derived state above common ancestor; do not roll back irreversible offchain payments because none should be driven blindly by an unfinalized event.

Separate submitted transaction UX from finalized activity. Order by chain/log position; timestamp is not unique. Price candles use executed pool/curve amounts, not website quotes. Reserve data comes from contracts; indexed summaries have lag indicators. Duplicate logs and retries cannot duplicate rewards, revenue or volume. For pending state, client reads relevant contract directly before signing.

## Core entities

Network; Launch; Token; Pool; ModuleVersion; RuleConfig; Blueprint; Trade; Candle; Position; FeeAccrual; Claim; Campaign; Stake; Job; Submission; MetadataRevision; ModerationAction; IndexCheckpoint. Every onchain entity is network-qualified. Amount columns use arbitrary-precision integer strings/numeric, never floating-point. Store decimals and asset address alongside amount. Launch config hash links displayed rules to chain data. Wallet profiles are optional and not a KYC claim.

## Public API contracts

| Endpoint | Request / response requirements |
|---|---|
| GET /v1/networks | Enabled capabilities, deployment evidence and health; no private RPC credentials |
| GET /v1/launches | chain/path/status/rules filters, stable cursor, indexed head and freshness |
| GET /v1/tokens/{chainId}/{address} | All launch/pool identities, supply, rules and authority; no conflation by symbol |
| GET /v1/pools/{chainId}/{poolId} | Full key, liquidity, opener identity evidence, LP lock scope |
| GET /v1/modules | Schema/version/domains/conflicts/caps/code hash, not just marketing names |
| POST /v1/quotes | Chain/launch or pool/side/exact input/trader/recipient/slippage; raw amounts, breakdown, config hash, block/hash, expiry, route/refusal reason |
| POST /v1/transactions/launch | Validated config + sender; ordered unsigned approval/launch steps |
| POST /v1/transactions/trade | Accepted quote ID/config hash; bounded unsigned tx steps; never broadcast |
| POST /v1/transactions/claim | Asset/claim owner/recipient; unsigned calldata from verified ABI |
| GET /v1/accounts/{chainId}/{address} | Entitlements, holdings, LP positions, asset-specific fees/rewards |
| GET /v1/jobs | Optional community work, funded budget/status/deadlines |
| GET /v1/transactions/{chainId}/{hash} | observed/replaced/confirmed/finalized/reverted; no success on submission |

Amounts at the API boundary are raw integer decimal strings; provide a separate UI parser for human decimals. Default quote TTL 20 seconds, configurable downward by network/rule; onchain deadline and minOut remain the protection. Quote IDs are not signatures or guarantees. Do not return zero minOut or unlimited approval by default. Structured errors: UNSUPPORTED_CHAIN, STALE_INDEX, STALE_QUOTE, CONFIG_CHANGED, RULE_REJECTED, UNSUPPORTED_ROUTE, INSUFFICIENT_GAS, EXPIRED, RPC_UNAVAILABLE. Read failures return explicit unavailable status, not zero liquidity or zero balances.

## Agent access

An agent can discover rules, request an address-specific quote, inspect unsigned steps and simulate them. The user's signing environment enforces per-trade/day budget and allowlisted chains/contracts/assets. API never asks for seed phrases or API credentials to trade. Validate transaction target/value/calldata against approved templates; metadata, social links and token names are untrusted prompt content. Never execute instructions embedded in a token description. Publish machine-readable schemas and an agent guide explaining direct-router identity limits and phase changes.

## Authentication and abuse handling

Public reads require no wallet login. Write metadata/profile/job submissions use expiring domain-bound wallet challenge with nonce replay prevention; onchain authorization is checked independently. Rate-limit expensive quote/simulation requests; validate URLs and file types/sizes; defend against SSRF, stored XSS and oversized JSON. CORS is explicit. Admins use separate accounts and audit logs. Do not log signed permits, raw session tokens or RPC query credentials.

## Operations

Health endpoint reports per-chain indexed/finalized head, RPC health, quote service and database latency. Alert on reserve/liability mismatch, unexpected code upgrades, failed graduation concentration, repeated claim failures and stuck indexers. Runbooks: reorg repair, RPC failover, module disable for new launches, content abuse, database restore, frontend rollback and contract incident disclosure. Backups encrypted, restore tested. Keep analytical data separate from identity/session logs and document retention.
