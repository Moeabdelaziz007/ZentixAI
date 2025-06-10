  <<<<<<< codex/create-tests-directory-and-add-test-cases
  import os
  import sys

  import pytest

  sys.path.append(os.path.dirname(os.path.dirname(__file__)))
  from zero_system import MindfulEmbodimentSkill

  @pytest.fixture
  def skill():
      return MindfulEmbodimentSkill()


  def test_default_style(skill):
      result = skill.execute()
      assert result["output"] == "مرحباً بك، كيف يمكنني مساعدتك؟"
      assert result["voice_style"] == "صوت هادئ وواضح"


  def test_fun_style(skill):
      result = skill.execute("شيء من المرح")
      assert result["output"] == "يا زعيم! جاهز لأي فكرة مجنونة \U0001F604"
      assert result["voice_style"] == "صوت حيوي وساخر"


  def test_professional_style(skill):
      result = skill.execute("هذا سؤال تقني مهم")
      assert result["output"] == "تحية طيبة، أنا جاهز لاستفساراتك التقنية"
      assert result["voice_style"] == "صوت رسمي وتحليلي"


  def test_caring_style(skill):
      result = skill.execute("أحتاج دعم معنوي")
      assert result["output"] == "أنا هنا من أجلك، كيف يمكنني مساعدتك اليوم؟"
      assert result["voice_style"] == "صوت دافئ ومتعاطف"
  =======
  import unittest

  from sss.zero_system import MindfulEmbodimentSkill


    <<<<<<< fmzv63-codex/rewrite-tests-to-use-unittest
    class TestMindfulEmbodimentSkill(unittest.TestCase):
    =======
    class TestMindfulEmbodiment(unittest.TestCase):
    >>>>>>> main
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


    <<<<<<< fmzv63-codex/rewrite-tests-to-use-unittest
    if __name__ == "__main__":
        unittest.main()
    =======
    >>>>>>> main
  >>>>>>> main
