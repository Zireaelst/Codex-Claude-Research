# Arc, Uniswap and Studio: verified scope and gates

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The infrastructure is sufficiently documented to design against, but several deployment gates remain.**

Official Uniswap documentation lists the following **Arc mainnet, chain 5042** deployments:

| Component | Officially listed address |
|---|---|
| v3 Factory | `0xf0db7b58379503491d857dB50AC9ece64c653918` |
| v3 Position Manager | `0x39654A85A4C05127f5Fd6ED22CAeC077A0fB1377` |
| v3 SwapRouter02 | `0x53BF6B0684Ec7eF91e1387Da3D1a1769bC5A6F77` |
| v4 PoolManager | `0x8366a39CC670B4001A1121B8F6A443A643e40951` |
| v4 PositionManager | `0x6049c9a0e26405C0985f9E3685C87d0aE917f82B` |
| Universal Router 2.1.2 | `0x8702463e73f74d0b6765aBceb314Ef07aCb92650` |

Source: [Uniswap deployment registry](https://developers.uniswap.org/deployments.json) and [v4 deployment documentation](https://developers.uniswap.org/docs/protocols/v4/deployments). The registry also lists launch infrastructure on Arc, further weakening any claim that basic issuance is missing.

Before implementation targets these addresses, verify chain ID, runtime bytecode, implementation/version, factory relationships and relevant immutable values. Do not paste deployment addresses from competitor documentation into production configuration.

Arc’s USDC ERC-20 interface is `0x3600000000000000000000000000000000000000`, using **6 decimals**. Native USDC uses **18 decimals**, but represents the same underlying balance. Arc recommends the ERC-20 interface for application balance reads and transfers. Use it consistently for pools, fees and treasuries; do not invent wrapped USDC or count native and ERC-20 balances as separate assets. [Arc contract documentation](https://docs.arc.io/arc/references/contract-addresses)

| Capability | Design status |
|---|---|
| Mainnet EVM, USDC gas, wallet configuration | Officially documented; mainnet 5042, testnet 5042002. [Network documentation](https://docs.arc.io/arc/references/connect-to-arc) |
| Official mainnet v3/v4 | Listed by Uniswap; independent runtime verification remains a release gate. |
| Canonical Arc **testnet** v3/v4 deployments | Not established in this research. Use a clearly labelled test deployment or local fork; never present it as canonical. |
| CCTP/Gateway funding | Official Arc addresses are documented; useful later for onboarding, unnecessary for the first launch/trade loop. |
| Custom v4 hook | Must be built, reviewed and deployed separately. Existing v4 infrastructure does not certify our hook. |
| Charts, treasury accounting, discovery | Require our indexer and application backend; not supplied automatically by Arc or Uniswap. |
| Embedded wallets | Optional later integration, subject to current provider support and recovery model. Wallet connection is sufficient initially. |
| Studio mainnet deployment/public hosting | Not supported by the inspected terms; use independent tooling and hosting. |

The local CLI was available. `whoami` returned **not authenticated**. `agent-guide`, `skills --json` and command help were readable. The guide describes a Vite/Foundry workspace, named sessions, file export and a **10,000-character prompt limit**. Its Uniswap skill says “Arc mainnet only,” but that describes integration context—not permission for Studio to broadcast.

Studio’s terms explicitly place mainnet review, testing, deployment and operation outside Studio, and say Studio does not host apps. Mainnet references in a preview are not a deployment. [Studio terms, §§1.2, 4.1, 4.8](https://studio.arc.io/terms-of-use)



**Studio should be the build workspace; export and independent review should be the release boundary.**

Use Studio to generate and iterate on contracts, tests, frontend, indexer code, schemas and integration tests. Its preview can demonstrate UI behavior, but must not be presented as production hosting.

Export the source, lockfiles, compiler settings, ABIs, test suites and configuration. Outside Studio:

1. Rebuild in a clean environment and inspect dependencies/licenses.
2. Verify canonical Arc contracts and runtime behavior.
3. Run local/fork tests and separately authorized testnet tests.
4. Obtain independent review of custody, accounting and any curve/hook.
5. Prepare exact mainnet deployment transactions with your own tooling and signer.
6. Deploy only after approval; verify source and configuration.
7. Host frontend/API/indexer independently.
8. Run a small-value production acceptance check.

A later controlled acceptance check could use an explicitly labelled team-owned launch, a **1 USDC buy**, a small sell, fee collection and a **0.01 USDC contributor payment**. The treasury can receive an explicitly labelled test top-up if actual collected fees are insufficient. Seed liquidity, launch fees and gas are additional costs. Do not imply that a 1 USDC trade finances the whole test or proves organic demand.

The records must show successful transaction receipts, the actual transfer events, pool/locker identity, fee allocation and the contributor’s received amount. None of this has been executed.
