import json

from advanced_screenshot_agent.evidence import EvidenceEvent, EvidenceRun


def test_evidence_run_save(tmp_path):
    run = EvidenceRun()
    run.add(
        EvidenceEvent(
            event_id="evt-1",
            label="home",
            image_path="home.png",
            sha256="abc",
            timestamp_utc="2026-01-01T00:00:00Z",
        )
    )
    path = run.save(tmp_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["run_id"] == run.run_id
    assert payload["events"][0]["label"] == "home"
