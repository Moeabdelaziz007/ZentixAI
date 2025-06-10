import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from zero_system import MindfulEmbodimentSkill

@pytest.fixture
def skill():
    return MindfulEmbodimentSkill()


def test_default_style(skill):
    result = skill.execute()
    assert result["output"] == "مرحباً بك، كيف يمكنني مساعدتك؟"
    assert result["voice_style"] == "صوت هادئ وواضح"


def test_fun_style(skill):
    result = skill.execute("شيء من المرح")
    assert result["output"] == "يا زعيم! جاهز لأي فكرة مجنونة \U0001F604"
    assert result["voice_style"] == "صوت حيوي وساخر"


def test_professional_style(skill):
    result = skill.execute("هذا سؤال تقني مهم")
    assert result["output"] == "تحية طيبة، أنا جاهز لاستفساراتك التقنية"
    assert result["voice_style"] == "صوت رسمي وتحليلي"


def test_caring_style(skill):
    result = skill.execute("أحتاج دعم معنوي")
    assert result["output"] == "أنا هنا من أجلك، كيف يمكنني مساعدتك اليوم؟"
    assert result["voice_style"] == "صوت دافئ ومتعاطف"
