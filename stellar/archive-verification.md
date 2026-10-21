# Archive verification — editorial record

- Three research entries: original prompts, complete report prose, final responses and user-facing exchanges.
- Every full report is compared with its source attachment after normalizing only link destinations; no research prose or conclusion is rewritten.
- Available original supporting notes, selected evidence, retained data and collection methods are included. Source artifact hashes are recorded separately.
- All local Markdown targets and anchors are checked. External research citations are preserved without new ecosystem research or a claim of permanent availability.
- Selected publication files are scanned for common PAT/API/private-key/Stellar-secret/JWT patterns, secret-bearing fields, email addresses and private workstation paths. No matching credentials or local details remain. Public source identifiers are retained.
- This is an archival hygiene check, not a guarantee that arbitrary unknown credential formats can always be recognized. Internal reasoning, authentication context and runtime configuration are not part of the archive.
- The index explicitly records unavailable historical page bodies, intermediate drafts and unexposed attachments. No Arc research is included.
- `archive-sha256.json` fingerprints the published files other than itself. These hashes are checked against the pushed Git tree before completion.
