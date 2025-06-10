import os
import json
import sss.zero_system as zs
import pytest

LOG_PATH = os.path.join(os.path.dirname(zs.__file__), "log.jsonl")


@pytest.fixture(autouse=True)
def cleanup_log():
    yield
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)


def test_interact_creates_log_file():
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)
    system = zs.ZeroSystem()
    system.interact('اختبار التسجيل')
    assert os.path.exists(LOG_PATH)
    with open(LOG_PATH, encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) >= 1
    entry = json.loads(lines[-1])
    assert entry['message'] == 'اختبار التسجيل'
    assert 'response' in entry

