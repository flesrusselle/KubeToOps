"""
Unit tests for KubeToOps Command of the Day deterministic selection and history tracking.
"""
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from select_command import select_command


@pytest.fixture
def sample_catalog():
    return [
        {
            "id": "cmd-001",
            "title": "Watch Pods",
            "category": "productivity",
            "difficulty": "beginner",
            "command": "kubectl get pods -w",
            "description": "Watch pod state changes.",
            "why": "Avoid manual polling.",
            "safety": "safe",
            "official_docs": "https://kubernetes.io/docs/reference/kubectl/"
        },
        {
            "id": "cmd-002",
            "title": "Rollout Restart Deployment",
            "category": "workloads",
            "difficulty": "intermediate",
            "command": "kubectl rollout restart deployment/myapp",
            "description": "Rolling restart.",
            "why": "Safely restart pods.",
            "safety": "caution",
            "official_docs": "https://kubernetes.io/docs/reference/kubectl/"
        },
        {
            "id": "cmd-003",
            "title": "Sort Events",
            "category": "troubleshooting",
            "difficulty": "beginner",
            "command": "kubectl get events --sort-by=.lastTimestamp",
            "description": "Sort recent events.",
            "why": "Troubleshoot recent failures.",
            "safety": "safe",
            "official_docs": "https://kubernetes.io/docs/reference/kubectl/"
        }
    ]


def test_deterministic_date_selection(sample_catalog):
    date_str = "2026-08-09"
    history = []
    selected1 = select_command(sample_catalog, history, date_str)
    selected2 = select_command(sample_catalog, history, date_str)

    assert selected1["id"] == selected2["id"], "Selection on the same date must be deterministic!"


def test_explicit_command_id_override(sample_catalog):
    history = []
    selected = select_command(sample_catalog, history, "2026-08-09", target_id="cmd-002")
    assert selected["id"] == "cmd-002"
    assert selected["title"] == "Rollout Restart Deployment"


def test_recent_history_exclusion(sample_catalog):
    history = [
        {"id": "cmd-001", "date": "2026-08-07", "title": "Watch Pods"},
        {"id": "cmd-002", "date": "2026-08-08", "title": "Rollout Restart Deployment"}
    ]
    # Remaining eligible: cmd-003
    selected = select_command(sample_catalog, history, "2026-08-09")
    assert selected["id"] == "cmd-003"
