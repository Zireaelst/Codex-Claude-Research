# Acceptance and evidence matrix

A test is evidence only if it runs against the specified artifact. Record command, tool versions, git revision, seed, network/block when applicable, output and failure count. The counts below are test identities, not claimed passing tests. No implementation currently exists in this new project.

| Test ID | Requirements | Scenario and expected result |
|---|---|---|
| A01 | P01,S01,S05 | Launch curve atomically; exactly S minted into authorized custody; frozen config matches registry/UI |
| A02 | P01,S02 | Buy/sell a range of amounts; backing plus fee liabilities plus refunds reconcile to actual balances |
| A03 | P01,S02,S15 | Independent high-precision model vs integer math; both currency orders/quote decimals; no rounding-profit cycles |
| A04 | P01,S03 | Final oversized buy charges only used input + its fee; rest returned; no fee on refund |
| A05 | P01,S06 | Fault actual graduation at initialize/mint/settle/locker steps; no partial effects; pending purchase retained correctly |
| A06 | P01,S04,S15 | Real upstream PoolManager/PositionManager/Permit2, real curve and hook: graduation creates funded LP and correct custody |
| A07 | P04,S08 | Deploy hook by CREATE2 with exact permission bits; wrong bits and spoofed hookData rejected; no etch as proof |
| A08 | P01,S05 | Attacker initializes exact key directly/through real periphery before authorized flow; no unauthorized valid launch |
| A09 | P05,S04 | Execute actual swaps then harvest fees repeatedly; real position liquidity unchanged; paid fee assets conserved |
| A10 | P01,S07 | Expiry and 72h pending timeout; proportional refunds independent of claim ordering except bounded rounding; no expiry |
| A11 | P01,P14 | Post-graduation token claims conserve inventory; partial advanced-profile claims work; restrictions permanently sunset |
| A12 | P02,S04 | Real v3 factory/NPM: seed, full-range NFT, permanent custody, fee claims; conflicting init rolls back seed and fee |
| A13 | P03,S13 | Path immutable; malicious launch/controller cannot mutate another record or register arbitrary sale |
| A14 | P04,S09 | All approved combinations; reject duplicates/conflicts, excessive fee, invalid profile/domain, unknown code hash |
| A15 | P04,S10 | Buy-only restrictions do not block supported sell path; direct/aggregator limits and bypasses match disclosures |
| A16 | P07,S03,S14 | Reentrant or blocked claim recipient; no double claim and no obstruction of unrelated recipients |
| A17 | P08,S13 | Existing token pool: genuine two-sided seed; NFT depositor ownership; proportional add/remove and fee collection |
| A18 | P08 | Last LP exits then pool is illiquid; unsupported partial swap reverts; adding liquidity restores operation |
| A19 | P09 | Funded staking/LP campaign: late joins, empty periods, principal exit, reward failure, no rewards beyond funding |
| A20 | P10,S07 | Job acceptance/rejection/revision/timeouts; reserved budget never spent twice; accepted payment never expires |
| A21 | P04,S09 | Auto-LP/buyback with stale observation, manipulated spot, slippage, repeated execution; unsafe maintenance rejected without blocking swaps |
| A22 | P11,S08,S11 | API generates bounded unsigned tx; injected metadata instructions, wrong chain, forged actor/referral/nonce rejected |
| A23 | P12,S11 | Two independent local chains: no identity/claim collision; invalid manifest/chain/code blocks writes |
| A24 | P06,P16,S12 | Reorg, duplicate logs, replay/backfill, RPC failure; same canonical read model and no fake zero metrics |
| A25 | P05 | Browser connects wallet, quotes, approves, trades, handles replacement/revert/graduation race and reconciles actual balance |
| A26 | P01,P02,P07 | Browser creates BOTH paths, harvests and claims real local-contract earnings; no fixture substitute |
| A27 | P08,P09,P10 | Browser external pool, LP exit, campaign stake/claim and funded job delivery/payment complete |
| A28 | P13 | Blueprint spec/config hash reproducible; edited/hidden template cannot mutate existing launches |
| A29 | P15,P16 | UI matches chain rule/authority/lock state; stored XSS, SSRF, impersonation and misleading badges prevented |
| A30 | P16 | Fresh clone installation, submodules, compile, typecheck, lint, tests, app build and DB migration all reproducible |
| A31 | S01–S16 | Fuzz/stateful invariant tests including max modules, multiple launches/users, donations and malicious recipients |
| A32 | P12 | Pinned fork per activated network with verified actual code and actual periphery; no assumption from local passing tests |

## Evidence ladder

Unit → property/stateful → real local upstream integration → browser against local deployed contracts → pinned network fork → separately authorized public verification. Each level proves different things. A canonical ABI import with a fake manager is only a unit test. A frontend screenshot proves appearance, not settlement. A successful compile proves no security property.

## Product completion checklist

- All P01–P16 map to passing evidence; any unsupported network/module remains disabled and identified.
- Every screen has real empty/loading/error paths and no fabricated live activity.
- Reserve, liabilities, claims, founding principal and dust reconcile.
- No secrets, leaked credentials, fake audits or unsupported deployment claims in repository.
- Reproducible commands, evidence artifacts, operator runbooks and threat-model limitations delivered.
- No public-release assertion before independent gates and explicit authorization.
