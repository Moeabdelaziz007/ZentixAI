from sss.zero_system import ZeroSystem


def test_echo_plugin_loaded():
    system = ZeroSystem()
    assert "echo" in system.brother_ai.skills
    result = system.brother_ai.skills["echo"].execute(message="hello")
    assert result["output"] == "hello"
