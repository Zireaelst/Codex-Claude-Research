Integrate both v3 and v4 UI, indexer and contracts. Implement fresh onchain quote and
simulation checks before signatures; indexer prices are display-only.
Exercise launch, buy, sell, collect, fund work, submit, approve and claim using
local fixtures or an available read-only mainnet fork.

Test wallet rejection, wrong chain, insufficient gas, expired quotes, RPC
failure, stale indexer and page reload during a pending transaction. Confirm
every displayed financial state can be traced to contract state or receipts.
Do not send public-network transactions. Report untested integration gates.
Exercise each full lifecycle independently, including curve graduation, retries, expiry/refunds and token claims. Require both launch selections to function for release.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
