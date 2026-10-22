Implement the indexer and read API required by the app. Index registered
launches, canonical pools, swaps, fee collection, credits, claims, treasury
commitments and work events. Use transaction hash/log index identity,
checkpointing, replay and rollback handling.

Provide paginated tokens, trades, candles, holders, fee ledger, treasury, work
and health endpoints. Include source block and staleness information. Store
public content separately from chain accounting.

Test duplicate delivery, restarts, missing blocks and complete reconstruction.
No private keys in the indexer. Do not provision hosted services or credentials.
Also index curve buys/sells, target state, graduation, claimable curve balances, token redemption, refunds and v4 pool/hook events. Distinguish phases and pool IDs.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
