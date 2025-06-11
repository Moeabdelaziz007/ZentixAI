from zero_system import ZeroSystem


def test_create_sibling_default_traits():
    system = ZeroSystem()
    sibling = system.create_sibling()
    assert sibling["status"] == "success"
    assert "أخ رقمي #1" == sibling["sibling_id"]
    assert sibling["traits"] == {"شخصية": "فضولي", "تخصص": "مساعد عام"}


def test_create_sibling_custom_traits():
    system = ZeroSystem()
    traits = {"تخصص": "مساعد برمجة"}
    sibling = system.create_sibling(traits)
    assert sibling["traits"] == traits


def test_create_multiple_siblings_unique_ids():
    system = ZeroSystem()
    ids = [system.create_sibling()["sibling_id"] for _ in range(3)]
    assert ids == ["أخ رقمي #1", "أخ رقمي #2", "أخ رقمي #3"]
