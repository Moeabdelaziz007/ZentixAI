import sss.zero_system as zs


def test_dynamic_skill_registration():
    system = zs.ZeroSystem()
    message = system.brother_ai.grow("test_skill")
    assert message == "تم تطوير مهارة جديدة: test_skill"
    assert "test_skill" in system.brother_ai.skills
    assert callable(system.brother_ai.skills["test_skill"])
    assert system.brother_ai.skills["test_skill"]() == {"status": "under_development"}
