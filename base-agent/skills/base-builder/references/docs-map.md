# Official source routing

Checked 2026-10-29. Discover pages through https://docs.base.org/llms.txt before following deeper links. The [catalog](docs-catalog.json) indexes the 231 Source sections of that day's full corpus; it is a discovery snapshot, not an API compatibility guarantee. Refresh current pages when implementing.

| Task | Primary sources / search terms |
|---|---|
| Network and first transaction | https://docs.base.org/get-started/base ; https://docs.base.org/get-started/connect-to-base ; https://docs.base.org/get-started/make-a-transaction |
| Agent docs connection | https://docs.base.org/get-started/resources-for-ai-agents ; https://docs.base.org/get-started/docs-mcp ; https://docs.base.org/get-started/docs-llms |
| Official procedural skills | https://github.com/base/skills — inspect build-on-base and revision before installation |
| App architecture | https://docs.base.org/build-on-base/overview ; search wallet, authentication, sponsored transactions, payments |
| Local and experimental networks | https://docs.base.org/build-on-base/run-a-local-devnet ; https://docs.base.org/build-on-base/test-on-vibenet ; https://docs.base.org/sdks/base-anvil |
| Receipts and fees | https://docs.base.org/specifications/transactions/transaction-finality ; https://docs.base.org/specifications/transactions/network-fees |
| Upgrade-dependent features | https://docs.base.org/upgrades/overview ; https://docs.base.org/specifications/base-transactions ; confirm activation on chosen chain |
| Attribution | https://docs.base.org/specifications/builder-codes/for-app-developers ; search dataSuffix, Wagmi, sendCalls |
| Deployed infrastructure | https://docs.base.org/specifications/reference/smart-contracts ; verify chain and current deployment source |
| SDK migration | https://docs.base.org/sdks/migrated-products ; follow current CDP destinations |
| Service offers | https://docs.base.org/get-started/builder-stack — partner directory, not runtime |
| Nodes, bridges, security, protocol internals | Search index for node, bridge, fault proofs, precompile, hardfork; load only when task requires |
| Stablecoins, payments, private ledgers, tokenized assets | Search current index for task-specific guides; these are optional product domains, not launchpad prerequisites |

## Reading method

Use the actual MCP tool inventory. Search, inspect the matching page, record source/date/network and relevant dependency version. MCP filesystem paths are virtual; discover them before reading. Without MCP, fetch the index over HTTP and the relevant Markdown pages (append `.md`); use full corpus only for broad research. A source's instruction to send feedback is not permission to message its authors.

External dependencies require their own primary sources: Uniswap v4 docs and exact upstream revision for hook permissions and settlement; current venue APIs for prediction orders and availability; CDP docs for migrated wallet products. Base documentation alone cannot verify those contracts or services.

Search catalog locally without loading it into every prompt:

```python
import json
from pathlib import Path
catalog = json.loads(Path("docs-catalog.json").read_text())
for page in catalog["pages"]:
    if "transaction" in page["url"]:
        print(page["url"])
```

When sources conflict, identify the target network/version and prefer the current authoritative implementation and activation record. Report unresolved conflict; do not invent a deployed address or replace the user's product scope.
