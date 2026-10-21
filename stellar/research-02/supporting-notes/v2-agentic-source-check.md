# Agentic implementation source check

Checked 20 October 2026. Read-only static inspection; no installation, repository code execution, tests, signing, transactions or deployments. This supplements `work/v2-agentic-research.md`. Links refer to mutable `main`; the fetch service did not expose an immutable commit SHA. Cached files had crawl ages of roughly six days to three weeks, so this is not a guarantee that every file reflects the latest commit.

## Omamori: implementation inaccessible in this environment

The public repository root/README remained readable. Actual implementation fetches for [`apps/firewall/pipeline.ts`](https://github.com/juanmaagd/yakusoku/blob/main/apps/firewall/pipeline.ts) and [`apps/firewall/merchant.ts`](https://github.com/juanmaagd/yakusoku/blob/main/apps/firewall/merchant.ts), through both GitHub blob and raw URLs, returned cache-miss errors. Other firewall and contract attempts also failed. Direct unauthenticated Python HTTPS fetching failed DNS resolution. No repository code was executed.

**Consequence:** We cannot independently confirm stage ordering, refuse dominance, merchant requirement binding, atomic budget accounting or onchain payment-limit enforcement from implementation. Those remain **author/README claims**. Do not describe this repository as source-audited, or report an invented code-level vulnerability/guarantee. Its architecture is meaningful competitive prior art, but this pass adds no implementation assurance for Omamori.

## Yohaku: two actual implementation files read

[`src/core/rules.ts`](https://github.com/kou-uni/ethglobal-tokyo2026-uni/blob/main/src/core/rules.ts) was readable, including `route()` and `onFailure()`.

**Observed guarantee within this function:** Expired requests deny; revoked delegates deny; delegates cannot write targets other than `proposal`. Explicit prohibition/revocation/expiry checks run before auto approval. `flagged` and `unavailable` screening deny. Sensitive categories, above-threshold amounts, first-seen counterparties and unknown requests require a human. Auto approval requires a matching standing grant and allowed category. Declared failure paths return deny.

**Boundary:** This pure router receives `ctx`, including time, screening and prior-counterparty knowledge, from its caller. Reading it does not establish authentic identity, truthful context, payment execution binding or truthful human output. The server integration was inaccessible. A permission verdict is not evidence a correctly bound transfer actually occurred.

[`src/adapters/intercepta.ts`](https://github.com/kou-uni/ethglobal-tokyo2026-uni/blob/main/src/adapters/intercepta.ts) was also readable.

**Observed behavior:** Malformed addresses, unsuccessful HTTP responses, malformed scores and exceptions return `unavailable`; the router above denies that result. Risk combines score and highest trait risk against a constant threshold of 50. Successful/flagged results can be reused for 60 seconds by default; unavailable results are not reused. Cache size is bounded.

**Concrete limitation:** `interceptaFromEnv()` returns undefined if required configuration is missing. Its comment describes keeping a stand-in and reporting screening false. Without the actual server wiring, this cannot support a blanket “missing screening configuration blocks every payment” claim. The author's comments also document a sanctions-address false negative; one provider score is not comprehensive compliance clearance. No live screening request was made by us.

## OnchainRouter: actual payment and HTTP execution source read

[`lib/x402.ts`](https://raw.githubusercontent.com/web3xDev/onchainrouter/main/lib/x402.ts) explicitly configures Hedera testnet and Arc `eip155:5042002`, with testnet facilitator/Gateway defaults. Thus the testnet description has **implementation evidence**, not only README support.

**Concrete detail:** `resolvePayout()` fills any missing per-rail seller payout using the router's own address. Therefore “every seller always receives funds directly” needs qualification: the configured route/payment option determines the actual recipient. This is a configuration fallback, not proof of misappropriation. Arc is advertised only when the router's Arc receiving address is set; missing required Hedera address throws.

[`app/api/tools/[slug]/route.ts`](https://raw.githubusercontent.com/web3xDev/onchainrouter/main/app/api/tools/%5Bslug%5D/route.ts) validates tool existence and Zod inputs before its local paywall. Local tool exceptions become 404 for no-answer or 502 for failures; successful return values become JSON without an independent semantic-quality verifier. The no-charge-on-error claim additionally depends on imported `withX402` behavior, not audited here.

**Important boundary:** External listed endpoints bypass the router's own paywall and handle settlement themselves. Relay failures return 502 with `charged:false`; that field cannot alone prove no remote settlement happened before a dropped response. It is not a refund or recovery mechanism.

A supplementary actual file, [`lib/relay.ts`](https://raw.githubusercontent.com/web3xDev/onchainrouter/main/lib/relay.ts), confirms POST forwarding of signed-payment headers, manual redirects, timeout and response-header passthrough. It contains no independent settlement verification, output acceptance, escrow or refund process. A timeout surrounds fetching response headers; it does not prove the remote service did not charge.

## Effect on company choice

These files strengthen the competitive baseline for deterministic permission routing, fail-closed live-provider failures, paid-tool input validation and multi-rail execution. They do **not** establish production security or paying adoption. They leave a precise commercial distinction for a procurement/recourse company: independently defined acceptance, binding orders to payment and delivery, ambiguous settlement recovery, enforceable seller response obligations, and actual buyer ownership of remediation. Buyer willingness to pay for that remains unverified.
