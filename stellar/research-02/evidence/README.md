# Public evidence snapshot manifest

Checked 20 October 2026. Records were retrieved around 19:28–19:33 UTC. These are public read-only research snapshots; no signing or transaction submission occurred. Files preserve provider responses rather than an independent full-ledger replay.

| Files | Source and scope |
|---|---|
| `v2-usdy-asset.json`, `v2-benji-asset.json` | Horizon `/assets` with exact canonical code and issuer; issuer identities and request links appear in the report/responses. Counts are accounts/trustlines, not humans or legal eligibility. |
| `v2-usdy-book.json` | [Horizon USDY/USDC orderbook](https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=USDY&selling_asset_issuer=GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6&buying_asset_type=credit_alphanum4&buying_asset_code=USDC&buying_asset_issuer=GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN&limit=200). Bid values are USDC per USDY and bid amount USDY. Depth in report sums price × amount for bids within1% of the best bid. Not NAV or firm fill capacity. |
| `v2-benji-book.json` | Equivalent canonical BENJI/USDC request. Empty response is this venue/time only, not proof no dealer/P2P market exists. |
| `v2-usdy-trades.json` | [Horizon latest200 Classic trades](https://horizon.stellar.org/trades?base_asset_code=USDY&base_asset_issuer=GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6&base_asset_type=credit_alphanum4&counter_asset_code=USDC&counter_asset_issuer=GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN&counter_asset_type=credit_alphanum4&cursor=&limit=200&order=desc). Includes orderbook and native-pool trades, excludes Soroban swaps. 167orderbook+33pool-side records. 33 distinct account-address strings; pool-side missing account values excluded. Time window is page-bounded ~29h, not a24h aggregate. |
| `v2-aqua-tickers.json` | [Aquarius tickers](https://amm-api.aqua.network/api/tickers/). 369 rows. `liquidity_in_usd` is total two-sided poolTVL; base/target volumes are24h **token units**. RWA/USDC volume uses the USDC side. Indexer produced; no organic/wash classification. |
| `v2-aqua-quotes.json` | Read-only POST [find-path endpoint](https://amm-api.aqua.network/api/external/v1/find-path/) with six local input bodies, timestamps and responses. Seven-decimal token amounts; slippage0/providerfee0/maxdepth4. XDR is unsigned routing data, not a submitted transaction. Routes indicative, not firm/global-optimal/permission-simulated. |
| `v2-aqua-openapi.json` | [Aquarius schema](https://amm-api.aqua.network/api/schema/), captured for units/quote semantics. Current official guide also documents v2; these strict-send observations explicitly used v1. |
| `v2-xoxno-spokes.json`, `v2-xoxno-markets.json`, `v2-xoxno-oracle_feeds.json` | [XOXNO mainnet source config](https://github.com/XOXNO/rs-lending-xlm/tree/main/configs/mainnet). Configured assets/LTVs/feeds, not independently read live contracts/caps/liquidity. TreeSHA observed63de8f1d85eee7833919502158ef3dfdd9a5dc6e; blobs fetched sequentially frommain, not asserted pinned to that tree. |

Quote comparison uses marginal sampled pool spot1.13348723USDC/USDY, not official NAV. Shortfall =1−(USDC output ÷(USDY input×spot)). All outputs divided by10^7. Values can change immediately. SnapshotTVL, trade activity and quote output do not establish customers, access, safety or future execution.

## SHA-256 of preserved files

- `v2-aqua-openapi.json`: `384108eaf4da6f05a29f9e9674f6c6ef2c432befc955ce20c10989a2ccd9c07c`
- `v2-aqua-quotes.json`: `690150f53678b05f4add23735a25f7d7ac1c1d8d4cb4209505bab26286e59432`
- `v2-aqua-tickers.json`: `23c425e61796535451e96c50b05bd45e218e0e4b4dc92e64ea19c3b43387666f`
- `v2-benji-asset.json`: `3c3137adffa28c32adfe797bdb4eac5a2ee3a97050f880525279a8f99728114d`
- `v2-benji-book.json`: `78a37f6e3c1ab6707b31a071a15c46bd4a510dbf2c59272f33e28f69e9cb2d0f`
- `v2-usdy-asset.json`: `df20c504d7e91e090a936ffa01e050336f37f69d9656d3023c7e72266be605cc`
- `v2-usdy-book.json`: `b29f660edaea4ec60f5eeb6cf30d014692dd79bceac4f4fd25b018ef8200adef`
- `v2-usdy-trades.json`: `c97bd0db151739d08743dc5c80800feb2e64e0f83160a8f1dd4f0bd7bdc6c8bb`
- `v2-xoxno-markets.json`: `ea10776ae60643aa0e2e9b8bcfe76d07755b7add6416f32e097a6e50709717cc`
- `v2-xoxno-oracle_feeds.json`: `d29d72800eb5b12d88856709044db81d12e08bed0039863f6621cb9a8398772c`
- `v2-xoxno-spokes.json`: `193bf136c65124f00c9177720d5747d3c4d5d2e6eaf9fac1d14a0487ce84685a`


## Bell addendum — 21 October 2026

`bell-mainnet-root-2026-10-21.json`: read-only response from https://horizon.stellar.org/, observed before 03:53:18 UTC. Latest reported ledger 65,053,777 closed at 03:51:08 UTC; current protocol 29, connected Core 30.0.0, Core-supported protocol 30. One-node observation, not a validator-quorum audit. See [Bell addendum](../../research-03/report.md) for interpretation and scheduled votes.
