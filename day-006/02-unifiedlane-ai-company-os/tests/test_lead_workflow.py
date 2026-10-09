from company_os.lead_workflow import (
    OutreachDraft,
    Prospect,
    approve_draft,
    assess_prospect,
    draft_outreach,
    run_lead_workflow,
)


def sample_prospect():
    return Prospect(
        company="Example SaaS (fictional)",
        website="https://example.test",
        industry="B2B SaaS technology",
        employee_band="201-500",
        signal="hiring and automation expansion",
        contact_name="Alex",
        contact_role="VP of Operations",
    )


def test_assessment_is_bounded_and_explains_score():
    result = assess_prospect(sample_prospect())
    assert 0 <= result.score <= 100
    assert result.tier == "A"
    assert result.rationale


def test_workflow_never_sends_messages():
    result = run_lead_workflow([sample_prospect()])
    assert result["status"] == "awaiting_human_review"
    assert result["messages_sent"] == 0
    assert result["results"][0]["draft"]["status"] == "pending_approval"
    assert result["results"][0]["next_step"] == "human_review"


def test_approval_requires_identity_and_pending_state():
    draft = draft_outreach(sample_prospect(), assess_prospect(sample_prospect()))
    try:
        approve_draft(draft, " ")
        assert False, "blank approver should fail"
    except ValueError:
        pass

    approved = approve_draft(draft, "reviewer@example.test")
    assert approved.status == "approved"
    assert approved.approved_by == "reviewer@example.test"


def test_already_approved_draft_cannot_be_approved_again():
    draft = OutreachDraft("d1", "Example", "Ops", "Subject", "Body")
    approve_draft(draft, "reviewer")
    try:
        approve_draft(draft, "reviewer2")
        assert False, "non-pending draft should fail"
    except ValueError:
        pass
