"""Concrete demo: research -> qualify -> draft -> human approval -> outreach queue.

No real emails are sent. The workflow produces a reviewable action that must be
explicitly approved before it can be marked ready for an authorized connector.
"""
from dataclasses import asdict, dataclass
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class Prospect:
    company: str
    website: str
    industry: str
    employee_band: str
    signal: str
    contact_name: str
    contact_role: str


@dataclass(frozen=True)
class LeadAssessment:
    company: str
    score: int
    tier: str
    rationale: list[str]


@dataclass
class OutreachDraft:
    draft_id: str
    company: str
    recipient_role: str
    subject: str
    body: str
    status: str = "pending_approval"
    approved_by: str | None = None


def assess_prospect(prospect: Prospect) -> LeadAssessment:
    """Transparent, illustrative scoring from supplied demo signals (0-100)."""
    score = 0
    rationale: list[str] = []
    industry = prospect.industry.casefold()
    signal = prospect.signal.casefold()

    if any(term in industry for term in ("software", "technology", "saas")):
        score += 25
        rationale.append("Target technology sector (+25)")
    if any(term in signal for term in ("hiring", "expansion", "automation", "growth")):
        score += 30
        rationale.append("Relevant growth or automation signal (+30)")
    if prospect.employee_band in {"51-200", "201-500", "501-1000", "1000+"}:
        score += 20
        rationale.append("Team size may support repeatable workflows (+20)")
    if prospect.website.startswith("https://"):
        score += 10
        rationale.append("Website provided for further verification (+10)")
    if prospect.contact_role:
        score += 15
        rationale.append("Relevant contact role identified (+15)")

    score = min(score, 100)
    tier = "A" if score >= 75 else "B" if score >= 50 else "C"
    return LeadAssessment(prospect.company, score, tier, rationale)


def draft_outreach(prospect: Prospect, assessment: LeadAssessment) -> OutreachDraft:
    """Drafts a message for review; it never sends or contacts anyone."""
    subject = f"Ideas for scaling workflows at {prospect.company}"
    body = (
        f"Hi {prospect.contact_name},\n\n"
        f"I noticed {prospect.company} is showing a signal related to "
        f"{prospect.signal}. Teams in {prospect.industry} often explore ways "
        "to reduce repetitive research, coordination, and reporting work.\n\n"
        "UnifiedLane designs AI-powered workflows where specialized agents "
        "can coordinate tasks with scoped permissions and human approval for "
        "sensitive actions. If improving a workflow like this is relevant, "
        "would a short conversation be useful?\n\n"
        "Best,\nUnifiedLane"
    )
    return OutreachDraft(
        draft_id=str(uuid4()),
        company=prospect.company,
        recipient_role=prospect.contact_role,
        subject=subject,
        body=body,
    )


def run_lead_workflow(prospects: list[Prospect]) -> dict[str, Any]:
    """Score prospects and create drafts, all left pending human approval."""
    results = []
    for prospect in prospects:
        assessment = assess_prospect(prospect)
        draft = draft_outreach(prospect, assessment)
        results.append({
            "prospect": asdict(prospect),
            "assessment": asdict(assessment),
            "draft": asdict(draft),
            "next_step": "human_review",
        })
    results.sort(key=lambda item: item["assessment"]["score"], reverse=True)
    return {
        "workflow_id": str(uuid4()),
        "status": "awaiting_human_review",
        "prospects_processed": len(results),
        "messages_sent": 0,
        "results": results,
    }


def approve_draft(draft: OutreachDraft, approver: str) -> OutreachDraft:
    """Records an explicit approval decision; delivery remains a separate step."""
    if not approver.strip():
        raise ValueError("An approver identity is required")
    if draft.status != "pending_approval":
        raise ValueError("Only pending drafts can be approved")
    draft.status = "approved"
    draft.approved_by = approver.strip()
    return draft
