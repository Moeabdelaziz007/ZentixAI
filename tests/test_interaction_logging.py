import os
import json
import pytest
import sss.zero_system as zs

LOG_PATH = os.path.join(os.path.dirname(zs.__file__), "log.jsonl")
MOOD_PATH = os.path.join(os.path.dirname(zs.__file__), "mood.jsonl")

@pytest.fixture(autouse=True)
def cleanup_logs():
    for path in (LOG_PATH, MOOD_PATH):
        if os.path.exists(path):
            os.remove(path)
    yield
    for path in (LOG_PATH, MOOD_PATH):
        if os.path.exists(path):
            os.remove(path)

def test_interact_creates_log_file():
    system = zs.ZeroSystem()
    system.interact("اختبار التسجيل")
    assert os.path.exists(LOG_PATH)
    with open(LOG_PATH, encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) >= 1
    entry = json.loads(lines[-1])
    assert entry["message"] == "اختبار التسجيل"
    assert "response" in entry

def test_interact_logs_mood():
    system = zs.ZeroSystem()
    system.interact("مرحبا")
    assert os.path.exists(MOOD_PATH)
    with open(MOOD_PATH, encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) >= 1
    entry = json.loads(lines[-1])
    assert "mood" in entry
