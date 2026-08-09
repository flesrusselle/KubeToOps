# Changelog

All notable changes to the **KubeToOps** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-09

### Added
- Initial standalone release of **KubeToOps** (*Navigate Kubernetes. Operate with confidence.*).
- Structured command catalog (`content/commands.yaml`) with detailed breakdowns, safety levels, and official docs.
- Curated Kubernetes tools catalog (`content/tools.yaml`) covering K9s, kubectx/kubens, Krew, Stern, Helm, Popeye, Kube-linter, and kubectl-neat.
- Automated Command of the Day engine with deterministic date hashing, history tracking, and manual `workflow_dispatch` trigger.
- Automated Pull Request validation and summary comment update with `Asia/Manila` (`PHT`) timestamps and timestamp preservation (`<!-- KUBE2OPS_PR_SUMMARY -->`).
- Diff-based deterministic Release Preview engine (`scripts/generate_release_preview.py`).
- $0-Cost hosting architecture specification (`docs/COST.md`).
- Troubleshooting playbooks for `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, `OOMKilled`, and `Service Unreachable`.
- Context & Namespace productivity guides and multi-cluster safety guardrails (`dont-accidentally-break-production.md`).
- Automated test suite (`pytest`) validating command catalog schema, CotD selection, release preview, and PR summary formatting.
