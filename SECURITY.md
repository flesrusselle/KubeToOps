# Security Policy

## Supported Versions

Only the latest version of KubeToOps main branch is actively supported for security updates.

| Version | Supported          |
| ------- | ------------------ |
| Main    | :white_check_mark: |

## Safety Guarantee & Command Rules

KubeToOps maintains strict security standards for all documented commands, scripts, and workflows:

1. **No Destructive Automation**: Automated workflows never run destructive commands (`kubectl delete`, cluster reset, node drain) against external clusters.
2. **Defensive Operations**: All documented security commands focus on defensive hardening (RBAC minimum privileges, PodSecurityStandards, securityContext, network policies).
3. **No Secret Leakage**: All scripts and catalogs undergo secret scanning with Gitleaks before PR merge.

## Reporting a Vulnerability

If you discover a security vulnerability or unsafe command in KubeToOps, please do NOT create a public issue.

Instead, submit a security advisory report to the repository maintainers via GitHub Security Advisories or email the maintainers directly.

You will receive an initial response within 48 hours, and an update regarding remediation progress within 5 business days.
