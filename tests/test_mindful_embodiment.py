import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import unittest
from sss.zero_system import MindfulEmbodimentSkill


class TestMindfulEmbodimentSkill(unittest.TestCase):
    def setUp(self):
        self.skill = MindfulEmbodimentSkill()

    def test_support_context(self):
        result = self.skill.execute("انا احتاج دعم عاجل")
        self.assertEqual(result["mood"], "caring")
        self.assertEqual(result["voice_style"], "صوت دافئ ومتعاطف")


if __name__ == "__main__":
    unittest.main()
