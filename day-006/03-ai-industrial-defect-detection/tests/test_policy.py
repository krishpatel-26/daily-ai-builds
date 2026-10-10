from app.policy import Detection, decide_inspection

def test_review_when_defect_is_above_threshold():
    result = decide_inspection([Detection("Scratch", .82), Detection("dent", .25)],
                               {"scratch", "crack", "dent"}, .5)
    assert result.status == "REVIEW"
    assert result.flagged_labels == ("scratch",)

def test_pass_when_no_configured_defect_is_detected():
    result = decide_inspection([Detection("bottle", .91), Detection("scratch", .2)],
                               {"scratch", "crack"}, .5)
    assert result.status == "PASS"
    assert result.flagged_labels == ()

def test_labels_are_case_insensitive():
    assert decide_inspection([Detection("CRACK", .7)], {"crack"}, .5).status == "REVIEW"
