import os
from core.tenant_registry import list_tenants

BASE = "/opt/aicore/tenants"


def scan_tenant(path):

    findings = []

    if not os.path.exists(path + "/state"):
        findings.append("STATE_SYSTEM_MISSING")

    if not os.path.exists(path + "/ui"):
        findings.append("UI_SYSTEM_MISSING")

    return findings


def run():

    print("\n=== DISTRIBUTED SCAN ===")

    tenants = list_tenants()

    all_findings = []

    for t in tenants:

        path = os.path.join(BASE, t)

        findings = scan_tenant(path)

        for f in findings:
            all_findings.append({
                "tenant": t,
                "finding": f
            })

    return all_findings
