import unittest

from amrikyyai import MindfulEmbodimentSkill


class TestMindfulEmbodiment(unittest.TestCase):
    def setUp(self):
        self.skill = MindfulEmbodimentSkill()

    def test_default_context(self):
        result = self.skill.execute("اهلا")
        self.assertEqual(result["mood"], "default")
        self.assertEqual(result["voice_style"], "صوت هادئ وواضح")
        self.assertIn("مرحباً بك", result["output"])

    def test_tech_context(self):
        result = self.skill.execute("لدي سؤال تقني حول البرمجة")
        self.assertEqual(result["mood"], "professional")
        self.assertEqual(result["voice_style"], "صوت رسمي وتحليلي")
        self.assertIn("استفساراتك التقنية", result["output"])

    def test_fun_context(self):
        result = self.skill.execute("لنمرح ونضحك سويا")
        self.assertEqual(result["mood"], "cheerful")
        self.assertEqual(result["voice_style"], "صوت سعيد ومتفائل")

    def test_support_context(self):
        result = self.skill.execute("انا احتاج دعم عاجل")
        self.assertEqual(result["mood"], "caring")
        self.assertEqual(result["voice_style"], "صوت دافئ ومتعاطف")


