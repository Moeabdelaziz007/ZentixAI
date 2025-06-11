import sss.zero_system as zs


def test_is_sibling_request_detects_true():
    assert zs.is_sibling_request("اريد اخ صغير يساعدني")


def test_is_sibling_request_detects_false():
    assert not zs.is_sibling_request("مرحبا كيف الحال")


def test_zero_system_status_contains_fields(tmp_path):
    system = zs.ZeroSystem(log_filename=str(tmp_path / "log.jsonl"))
    status = system.system_status()
    assert {"uptime", "interactions", "skills", "dna_backup"} <= status.keys()


def test_create_sibling_increments_count():
    system = zs.ZeroSystem()
    skill = system.skills["sibling_genesis"]
    before = skill.siblings_created
    system.create_sibling()
    assert skill.siblings_created == before + 1


def test_interact_triggers_sibling_skill():
    system = zs.ZeroSystem()
    result = system.interact("اريد اخ صغير يساعدني")
    assert result["sibling_id"] == "أخ رقمي #1"
    assert system.brother_ai.q_table["sibling_genesis"] == 1


def test_mood_history_and_q_table_update():
    system = zs.ZeroSystem()
    system.interact("صوت لنمرح ونضحك سويا")
    system.interact("صوت انا احتاج دعم عاجل")
    assert system.brother_ai.mood_history[-2:] == ["cheerful", "caring"]
    assert system.brother_ai.q_table["mindful_embodiment"] == 2
