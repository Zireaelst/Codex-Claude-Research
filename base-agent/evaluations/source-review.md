# Source review — 2026-10-29

The complete Base `llms-full.txt` was downloaded and split into 231 Source sections. The index was also downloaded. Corpus digest, size and per-page inventory are in [docs-catalog.json](../skills/base-builder/references/docs-catalog.json). This is full-corpus retrieval/indexing plus targeted review, not execution or semantic verification of every example.

Targeted review covered Base network configuration, AI resources, Docs MCP, official skills, local devnet/Vibenet, fees/finality, upgrades/native precompiles, Base Transactions, builder attribution, SDK migration and app development. External client setup was checked against official Codex/Claude skill and MCP guidance. Source launchpad specs and already-published project roadmaps informed the product profiles.

Material findings incorporated:

- Vibenet experimentation does not establish mainnet availability; native features need chain activation checks.
- Native precompiles may have empty bytecode; code existence is not the universal validity test.
- Base Transactions documented phased execution requires feature activation and per-phase outcome checks.
- Wagmi attribution needs supported transaction-level suffix handling; outer AA success is not each operation's success.
- Base Account/Wallet MCP product migrations require current CDP references. Docs MCP is a separate documentation service.
- Consumer prediction accepted orders are not fills; ambiguous submission requires reconciliation before retry.

## Observed connection evidence

Direct HTTP JSON-RPC to https://docs.base.org/mcp succeeded for initialize (protocol 2024-11-05), tools/list, and tools/call using search_base_documentation with query `Builder Codes Wagmi dataSuffix createConfig`. Server identified itself as Base Documentation 1.0.0. Search returned the documentation warning about Wagmi configuration and dataSuffix.

Tool discovery returned search_base_documentation, query_docs_filesystem_base_documentation and submit_feedback. Feedback was not called. Local Codex CLI MCP add/help syntax was inspected. No global MCP or skill installation was performed. This transport smoke test does not validate client trust, authentication policies, or end-to-end Codex/Claude activation on another machine.

Primary entry points: [Base index](https://docs.base.org/llms.txt), [full corpus](https://docs.base.org/llms-full.txt), [official skills](https://github.com/base/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills), [Claude MCP](https://code.claude.com/docs/en/mcp).
