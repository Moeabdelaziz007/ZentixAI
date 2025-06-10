import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from zero_system import ZeroSystem


class TestDynamicSkill(unittest.TestCase):
    def test_dynamic_skill_registration(self):
        system = ZeroSystem()
        message = system.brother_ai.grow("test_skill")
        self.assertEqual(message, "تم تطوير مهارة جديدة: test_skill")
        self.assertIn("test_skill", system.brother_ai.skills)
        self.assertTrue(callable(system.brother_ai.skills["test_skill"]))
        self.assertEqual(system.brother_ai.skills["test_skill"](), {"status": "under_development"})
