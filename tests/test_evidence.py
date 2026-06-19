from agentsight.evidence import EvidenceEvent, EvidenceStore, hash_file


def test_evidence_store_appends_lists_and_loads_events(tmp_path):
    store = EvidenceStore(tmp_path)
    event = EvidenceEvent(
        event_id="evt-1",
        label="home",
        scope="region",
        backend="mock",
        image_path="home.png",
        redacted_image_path=None,
        sha256="abc",
        timestamp_utc="2026-01-01T00:00:00Z",
    )

    store.append_event(event)
    store.write_manifest()

    events = store.list_events()
    assert events[0]["event_id"] == "evt-1"
    assert store.load_event("evt-1")["label"] == "home"
    assert store.manifest_path.exists()


def test_hash_file_is_stable(tmp_path):
    path = tmp_path / "payload.txt"
    path.write_text("same", encoding="utf-8")

    assert hash_file(path) == hash_file(path)
