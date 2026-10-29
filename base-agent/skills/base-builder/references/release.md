# Deployment and release preparation

Development guidance does not grant execution authority. Carry forward specific user authorization; do not request it repeatedly for the same action. A broad request to build/prepare is not a request to spend funds, sign trading orders, deploy public contracts, change account settings or publish production.

Before a public deployment prepare a concrete manifest: target network and chain ID, source/compiler/dependency revisions, ordinary deployed contract addresses and code hashes or native precompile activation evidence, constructor/config arguments, module flags/permissions, admin roles, deployer identifier, expected transactions, estimated cost, verification method and incident/recovery boundary. Never put a private key or seed in the manifest/chat. Keep signing in the user's approved wallet/keystore or secure runtime.

Separate gates: meaningful local unit/property tests; real upstream integration; browser against real local contracts; pinned target-network fork; independent review of custom financial logic; explicit public action authorization; post-action receipt/code/config verification. Testnet is also a public side effect. Use task-appropriate review for an ordinary UI fix; don't force a protocol audit for every documentation edit.

For launchpad, audit/review scope covers actual deployed revisions, curve accounting, hook composition, initialization, locker/vault boundaries and upgrade/incident authority. Source verification is not audit. Immutable defects may have no safe patch; do not promise rollback. For prediction, verify venue terms/access, wallet/order signature boundaries, idempotency and claim path; no custom custody contract does not mean no security work.

Publish operational readiness honestly: restore tested, RPC/venue outage behavior, reorg/reconciliation, stale data labels, alerts and user recovery paths. Rollback of a frontend cannot roll back a finalized onchain transaction. External token issuer freezes cannot be overridden by app UI.

Post-deployment evidence: transaction receipt status, expected contract state and roles, code/source verification, configured frontend network, actual executed user action and decoded Builder Code where supported. Do not publish claims of volume, users, grant approval, audit or partner status without evidence. If not authorized to broadcast, deliver the prepared plan and stop at signing; complete unaffected local work.
