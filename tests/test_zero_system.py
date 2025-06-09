import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest

from zero_system import ZeroSystem

class TestZeroSystem(unittest.TestCase):
    def test_create_sibling_increments_count(self):
        system = ZeroSystem()
        genesis_skill = system.skills["sibling_genesis"]
        before = genesis_skill.siblings_created
        system.create_sibling()
        after = genesis_skill.siblings_created
        self.assertEqual(after, before + 1)
