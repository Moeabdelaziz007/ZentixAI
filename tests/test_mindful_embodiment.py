import pytest
from sss.zero_system import MindfulEmbodimentSkill


@pytest.fixture
def skill():
    return MindfulEmbodimentSkill()


def test_default_context(skill):
    result = skill.execute("اهلا")
    assert result["mood"] == "default"
    assert result["voice_style"] == "صوت هادئ وواضح"
    assert "مرحباً" in result["output"]


def test_tech_context(skill):
    result = skill.execute("لدي سؤال تقني حول البرمجة")
    assert result["mood"] == "professional"
    assert result["voice_style"] == "صوت رسمي وتحليلي"


def test_fun_context(skill):
    result = skill.execute("لنمرح ونضحك سويا")
    assert result["mood"] == "cheerful"
    assert result["voice_style"] == "صوت سعيد ومتفائل"


def test_support_context(skill):
    result = skill.execute("انا احتاج دعم عاجل")
    assert result["mood"] == "caring"
    assert result["voice_style"] == "صوت دافئ ومتعاطف"
