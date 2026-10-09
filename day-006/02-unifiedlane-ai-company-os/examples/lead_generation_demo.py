"""Run a safe, local lead-generation workflow demo using fictional companies."""
import json

from company_os.lead_workflow import Prospect, run_lead_workflow

prospects = [
    Prospect(
        company="Northstar Software (fictional)",
        website="https://northstar.example",
        industry="B2B SaaS technology",
        employee_band="201-500",
        signal="expanding its customer success team and exploring automation",
        contact_name="Jordan",
        contact_role="VP of Operations",
    ),
    Prospect(
        company="Cedar Labs (fictional)",
        website="https://cedarlabs.example",
        industry="Technology",
        employee_band="51-200",
        signal="hiring operations analysts",
        contact_name="Taylor",
        contact_role="Head of Operations",
    ),
    Prospect(
        company="Harbor Retail (fictional)",
        website="https://harbor.example",
        industry="Retail",
        employee_band="11-50",
        signal="opening a new location",
        contact_name="Morgan",
        contact_role="Operations Manager",
    ),
]

result = run_lead_workflow(prospects)
print(json.dumps(result, indent=2))
print("\nSafety: this demo uses fictional data and sends zero messages.")
print("Review the drafts; do not connect a sending integration without authorization.")
