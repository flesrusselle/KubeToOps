# Contributing to KubeToOps

Thank you for your interest in contributing to **KubeToOps** — *Navigate Kubernetes. Operate with confidence.*

KubeToOps is a practical Kubernetes field guide for engineers who already know the basics and want to operate faster, safer, and with higher confidence.

---

## Core Principles for Contributions

Every command, tool, shortcut, plugin, or technique added to KubeToOps must adhere to our strict explanation standard:

1. **What it does**: Direct, concise summary of the command/tool function.
2. **Why it is useful**: Real-world operational context.
3. **When to use it**: Specific scenario triggering its application.
4. **How to use it & breakdown**: Explicit syntax with flag-by-flag breakdown.
5. **What could go wrong**: Edge cases, performance pitfalls, or data risks.
6. **How to verify**: Command to confirm successful execution.
7. **Official documentation**: Clickable reference link to official docs.
8. **Safety Classification**:
   - 🟢 **Safe**: Read-only operations, dry-run configurations, schema exploration.
   - 🟡 **Caution**: State-modifying operations, pod restarts, rollout pauses.
   - 🔴 **Destructive**: Resource deletion, pod eviction, namespace removal.

---

## Submitting New Commands

New commands should be submitted to `content/commands.yaml` using the structured format:

```yaml
- id: "cmd-XXX"
  title: "Descriptive Command Title"
  category: "productivity" # kubectl | contexts | namespaces | aliases | plugins | tools | troubleshooting | networking | workloads | security
  difficulty: "intermediate" # beginner | intermediate | advanced
  command: "kubectl <command> <flags>"
  description: "Clear description of action."
  why: "Why this helps."
  example: "kubectl get pods -n default"
  breakdown:
    - flag: "-n"
      meaning: "Specify target namespace."
  safety: "safe" # safe | caution | destructive
  test_environment: "safe-read"
  official_docs: "https://kubernetes.io/docs/reference/kubectl/"
  verified: true
  verification_notes: "Verified against v1.30 cluster."
  tags:
    - "kubectl"
    - "productivity"
```

---

## Local Validation Suite

Before opening a Pull Request, run the local validation suite:

```bash
make check-prerequisites
make lint
make test
```

All contributions must pass Markdown linting, YAML linting, Python unit tests (`pytest`), ShellCheck, and link verification.

---

## Pull Request Guidelines

- Branch naming: `feature/short-description` or `fix/short-description`.
- PR Title: Follow conventional commits format (e.g. `docs: add rollout undo guide`, `feat: add kubectl plugin`).
- PRs must pass all GitHub Actions automated workflows.
- PR summaries are automatically managed by KubeToOps PR Automation (`<!-- KUBE2OPS_PR_SUMMARY -->`).
