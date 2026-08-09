# 💰 Zero-Cost Hosting & Automation Architecture

**KubeToOps** is designed from the ground up to operate at **$0 cost** under normal open-source usage.

---

## 1. Hosting & Infrastructure Breakdown ($0 Total)

| Component | Provider / Infrastructure | Cost |
| :--- | :--- | :--- |
| **Repository Hosting** | GitHub Public Repository | **$0** (Free unlimited public repos) |
| **Issue Tracking & PRs**| GitHub Issues & Pull Requests | **$0** (Included free) |
| **Release Management** | GitHub Releases | **$0** (Included free) |
| **CI/CD Automation** | GitHub Actions (Public Repositories) | **$0** (Free for public repositories) |
| **Command of the Day Engine**| Python Script (`scripts/generate_command_of_day.py`) | **$0** (Runs in GitHub Actions) |
| **Release Preview Engine** | Python Script (`scripts/generate_release_preview.py`) | **$0** (Runs in GitHub Actions) |
| **PR Automation & Summaries**| Python Script (`scripts/update_pr_summary.py`) | **$0** (Runs in GitHub Actions) |
| **AI / LLM Dependencies**| **None** (100% Deterministic Scripts) | **$0** (No API keys required) |

---

## 2. GitHub Actions Usage Optimization & Free Tier Guardrails

GitHub provides free GitHub Actions runner minutes for public repositories. To ensure the project remains sustainable and lightweight, the workflows are strictly optimized:

1. **Lightweight Runners**: All jobs run on standard `ubuntu-latest` runners (lowest resource allocation footprint).
2. **Minimal Execution Paths**: Workflows use `paths` filters to prevent running unnecessary jobs when non-relevant files change (e.g. documentation-only edits do not trigger Docker/Kind builds).
3. **No Heavy Ephemeral Infrastructure**: CI checks run static analysis, catalog schema verification, and unit tests in seconds. Disposable Kubernetes clusters (`kind`) are only spun up when explicit cluster testing is requested.
4. **No Recursive Automation Loops**: CotD generation creates a PR that targets only generated files (`command-of-the-day/README.md`, `history.json`), preventing workflow trigger loops.

---

## 3. What Has No Paid Dependency

- **Zero LLM / AI API Calls**: Unlike projects relying on OpenAI, Claude, or Gemini APIs for PR summaries or content generation, KubeToOps uses pure Python AST and Git diff parsing.
- **Zero Third-Party SaaS**: No external monitoring (Datadog, New Relic), no paid security scanners (Snyk paid tier), no paid status pages.
- **Zero Database Infrastructure**: All state (command catalog, history) is maintained in Git (`content/commands.yaml`, `command-of-the-day/history.json`).

---

## 4. What Future Additions Could Introduce Cost (And What to Avoid)

To maintain the $0 cost guarantee, maintainers must **AVOID**:
- ❌ Integrating paid AI API keys in GitHub Secrets for automated PR comments or docs generation.
- ❌ Purchasing custom domain names or paid static hosting if GitHub Pages is sufficient.
- ❌ Adding cloud provider test clusters (AWS EKS, GCP GKE, Azure AKS) to CI workflows.
- ❌ Using self-hosted GitHub runners on paid cloud VPS instances (AWS EC2, DigitalOcean).

---

## 5. Summary Guarantee

As long as KubeToOps remains a public GitHub repository using deterministic Python scripts and native GitHub Actions, **operational costs will remain strictly $0.00**.
