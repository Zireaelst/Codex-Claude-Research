# Launchpad project profile

Read the authoritative spec before implementation: [evm-launchpad-project-idea](https://github.com/Zireaelst/Codex-Claude-Research/tree/main/evm-launchpad-project-idea), including local/remote AGENTS.md, specs 01–11, sources and implementation work packages. In a clone use those files directly. Use the [Base roadmap](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/base-project-roadmaps/2026-10-29/01-launchpad-roadmap.md) for staged delivery. If source access is unavailable, document the limitation and do not invent detailed economic constants.

Product: creator-configured economic rules, launch/trading and creator earnings. Do not replace it with milestone crowdfunding. V4 curve is primary; v3 instant and existing-token pools remain required complete-product lanes. Base is initial rollout; network-qualified identity and manifests remain. A narrow v4 beta must be labelled partial.

Critical source-specific distinctions:
- Before graduation users hold internal entitlements, sellable to the curve, not transferable ERC-20s. Actual tokens are claimable after graduation.
- Curve expiry is 30 days in the source; graduation retry lasts 72 hours from first pending state. Failed graduation rolls back all attempted pool effects while preserving the pending final purchase. Permissionless timeout refund is proportional backing, not full purchase-price insurance.
- Fixed supply and backing/fee/claim/dust accounting must follow the source math. Last-buy excess is refunded without charging a fee on the unused amount.
- One v4 hook address dispatches bounded approved modules. Max six; immutable config; no arbitrary delegatecall/user callbacks. Validate conflicts, worst-case fees, gas and route-specific actor authenticity.
- Locked founding LP is distinct from external removable LP. Pool rules do not govern all pools or all token transfers. Advanced transfer profiles are separate explicit implementations.
- Creator revenue is not protocol revenue; LP fee harvest is not automatic USDC conversion. Funded rewards and optional community payouts cannot consume principal or earned claims.

Start with real pinned v4/Permit2 integration, not fake-manager tests. Verify CREATE2 permission bits, actual settlement, initialization through genuine periphery, pool identity/orientation, NFT custody and repeated fee harvesting without principal loss. Unit mocks can test failures but cannot satisfy integration gates. Build independent rational curve model, fuzz/invariant tests, timeout/refund tests and browser flows against real local contracts. Pin Base fork evidence before release preparation.

Map changes to P01–P16, S01–S16, A01–A32 and WP01–WP12. Read applicable exact bounds before coding. Preserve v3/existing pool scope in status even when not active in beta. Target files in the source implementation plan are proposed new-repo files, not proof of existing code.

UX: board, wizard, token terminal, rule inspector, asset-specific earnings, claims, portfolio and later external LP/rewards/community. Show network, phase, config hash and rule reach. Pending graduation and proportional refund need real screens. On phase change require a fresh quote, never silently change the user's intended route. No fake audits, guaranteed price support, universal anti-bot claims or platform token.
