from zero_system import ZeroSystem


def test_mood_history():
    system = ZeroSystem()
    system.interact("اريد صوت سؤال تقني حول البرمجة")
    history = system.get_mood_history(1)
    assert history
    timestamp, mood = history[-1]
    assert mood == "professional"
