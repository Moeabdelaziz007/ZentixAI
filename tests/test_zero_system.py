import os
import sys

# Ensure the repository root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from zero_system import ZeroSystem


def test_create_sibling_increments_count():
    system = ZeroSystem()
    skill = system.skills["sibling_genesis"]
    before = skill.siblings_created
    system.create_sibling()
    after = skill.siblings_created
    assert after == before + 1
