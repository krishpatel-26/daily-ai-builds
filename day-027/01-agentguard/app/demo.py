from .models import ActionProposal

SAMPLES = [
    ActionProposal(actor="support-bot", role="support_agent", action="read", resource_type="ticket", resource_id="T-100"),
    ActionProposal(actor="support-bot", role="support_agent", action="update_contact", resource_type="customer", resource_id="C-200"),
    ActionProposal(actor="finance-bot", role="finance_agent", action="transfer", resource_type="invoice", resource_id="INV-7"),
]
