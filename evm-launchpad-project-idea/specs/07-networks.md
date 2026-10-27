# EVM networks and dependency policy

Base is the default development reference, not a chain-exclusive product. Candidate additional networks include Ethereum, Arbitrum, Optimism, Avalanche, BNB Chain and Unichain. This is a target list, NOT a claim that all selected versions and services work on each network. No Arc dependency or configuration is inherited.

## Network activation manifest

Each network needs chain ID, name, native currency/decimals, RPC providers, explorer, finality policy, multicall, wrapped-native asset, approved quote assets with decimals, v3 factory/NPM/router/quoter, v4 PoolManager/PositionManager/quoter/StateView, Permit2, protocol deployments, deployment block numbers, code hashes, compiler/upstream pins and enabled capabilities. Include source URL, checked date, checked block/hash and evidence for each address. Never copy addresses across networks on the assumption of deterministic equality.

Four states: UNCONFIGURED, LOCAL_VERIFIED, FORK_VERIFIED, PUBLIC_VERIFIED. Enabling UI writes requires correct wallet chain AND verified contract addresses/code/config AND path-specific capability, not a boolean 'configured' field alone. A network with v3 only must not display active v4 launches. Do not infer source verification or review from nonzero bytecode.

## Quote assets

Default pairs: canonical USDC and wrapped native token where individually verified. Native gas is separate. Native input can wrap atomically in our router; protocol custody uses ERC-20 wrapped asset. Never send native refunds by forced reentrant pushes; allow explicit pull fallback. No assumption that native currency shares balance with USDC.

Allowlist standard non-rebasing, non-fee-on-transfer quote assets. External-token lane also excludes rebasing, fee-on-transfer and arbitrary callback tokens. A behavioral test cannot prove an upgradeable token stays compatible: disclose issuer/proxy powers, monitor upgrades and halt NEW pool creation if assumptions change. Existing user exits cannot be promised during issuer-level freeze.

No stock-token bridge, share-based derivatives or unsupported custom quote assets. Quote-native economics do not need USD oracle settlement. USD estimates must have timestamp/confidence and can be unavailable without blocking plain quote-denominated trades.

## Upstream dependency strategy

Read official deployment inventories and actual verified code at build time; pin coherent source revisions corresponding to addresses. Relevant sources: [v4 deployments](https://developers.uniswap.org/docs/protocols/v4/deployments), [Base v3 deployments](https://developers.uniswap.org/docs/protocols/v3/deployments/v3-base-deployments), [v4-core](https://github.com/Uniswap/v4-core), [v4-periphery](https://github.com/Uniswap/v4-periphery), [Permit2](https://github.com/Uniswap/permit2).

Compile real upstream contracts with their required compiler into isolated artifacts when exact pragmas differ from our contracts. Pin recursive dependencies; clean clone must reproduce artifacts from source. Never bypass this with mocked managers. Review upstream license obligations before distribution and commercial deployment; availability of source does not imply unrestricted reuse.

## Multi-network behavior

Token identity = chainId/address; pool identity = chainId/poolId or v3 address. Same name across chains means different tokens. No bridges, shared total supply or cross-chain reserve balancing in target product. Profiles and watchlists can span networks; all financial aggregates show valuation source and missing data. Users explicitly select execution chain. Each chain indexer recovers independently. Chain outage does not corrupt another chain's state.

## Wallets and services

Use EIP-1193 connectors, typed viem clients and wagmi-compatible UI. Support injected wallets, WalletConnect-compatible connection and common smart-account flows only after simulation coverage. EIP-712 permits include chain/domain/nonce/expiry. Agent signatures require bounded policy and the human user's wallet; no server-managed spending keys. Optional gas sponsorship is not assumed, and must expose caps and costs if added.

Runtime dependencies: RPC, indexer database, metadata/image storage, API and wallet connection provider. Build-time tools: Foundry, Node/package manager, browser tests, static analyzers, optional documentation MCP tools. No runtime reliance on a coding agent, MCP server or Arc Studio session.
