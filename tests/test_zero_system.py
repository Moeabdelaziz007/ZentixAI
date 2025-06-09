import pytest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from zero_system import TrueDigitalFriendshipSkill, MindfulEmbodimentSkill


def test_friendship_multiple_users():
    skill = TrueDigitalFriendshipSkill()
    user1 = {"id": "u1", "name": "Ali"}
    user2 = {"id": "u2", "name": "Sara"}

    resp1 = skill.execute(user1)
    assert resp1["friendship_level"] == 1

    resp2 = skill.execute(user1)
    assert resp2["friendship_level"] == 2

    resp3 = skill.execute(user2)
    assert resp3["friendship_level"] == 1


def test_mindful_embodiment_contexts():
    skill = MindfulEmbodimentSkill()
    cheerful = skill.execute("هذا يوم مليء بالمرح")
    assert cheerful["mood"] == "cheerful"

    professional = skill.execute("لدي سؤال تقني بخصوص الكود")
    assert professional["mood"] == "professional"
