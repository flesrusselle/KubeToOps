# 🧰 kubectl Core Reference & Practical Usage

`kubectl` is the primary command-line tool for communicating with a Kubernetes cluster API server.

---

## 📚 Section Overview

| Guide | Description | Primary Topics |
| :--- | :--- | :--- |
| **[Productivity Patterns](productivity.md)** | Speed flags & output modifiers | `-A`, `-o wide`, `-w`, `--sort-by`, `--show-labels` |
| **[kubectl Explain](explain.md)** | Terminal API schema introspection | `kubectl explain deployment.spec.template` |
| **[Dry-Run & Manifest Generation](dry-run-yaml.md)** | Client/server dry-run & clean YAML | `--dry-run=client -o yaml`, manifest diffing |
| **[kubectl Cheatsheet](cheatsheet.md)** | Essential command reference | Quick copy-paste syntax for operational tasks |

---

## 🛡️ Operational Command Standards

When executing `kubectl` commands against remote or local clusters, adhere to these safety practices:

1. **Verify Context First**: `kubectl config current-context` before running state-altering operations.
2. **Explicit Namespaces**: Avoid relying on default namespace when targeting specific services; pass `-n <namespace>` or use `kubens`.
3. **Dry-Run Before Applying**: Validate complex resource mutations locally (`--dry-run=client`) before applying to API server.
