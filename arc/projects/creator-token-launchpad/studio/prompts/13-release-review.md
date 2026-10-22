Prepare the complete dual-path project for export and independent review. Run the relevant
contract, integration, frontend and indexer tests. Produce an artifact manifest,
dependency versions/licenses, ABI hashes, compiler settings, configuration
schema, threat model and unresolved findings.

Prepare unsigned deployment and verification instructions for use outside
Studio, but do not execute them. Check that exported files contain no secrets
and that a clean environment can rebuild the project. Distinguish passing
tests from unavailable tests. Do not publish, deploy or claim production safety.
Release fails if either launch path is incomplete, mocked or disabled. Include independent review coverage for curve and hook code.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
