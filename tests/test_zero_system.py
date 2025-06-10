from sss.zero_system import ZeroSystem


def test_create_sibling_increments_count():
    system = ZeroSystem()
    genesis_skill = system.skills["sibling_genesis"]
    before = genesis_skill.siblings_created
    system.create_sibling()
    after = genesis_skill.siblings_created
    assert after == before + 1

