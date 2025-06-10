  <<<<<<< codex/add-instructions-for-running-cli.py-and-pytest
    import os
  import sys
  import pytest

  sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

  from zero_system import ZeroSystem, is_sibling_request


  def test_is_sibling_request_detects_true():
      assert is_sibling_request("اريد اخ صغير يساعدني")


  def test_is_sibling_request_detects_false():
      assert not is_sibling_request("مرحبا كيف الحال")


  def test_zero_system_status_contains_fields():
      system = ZeroSystem()
      status = system.system_status()
      assert "uptime" in status
      assert "interactions" in status
      assert "skills" in status
      assert "dna_backup" in status


  def test_create_sibling_increments_count():
      system = ZeroSystem()
      first = system.create_sibling()
      second = system.create_sibling()
      assert first["sibling_id"] != second["sibling_id"]
  =======
    <<<<<<< codex/add-tests-for-is_sibling_request-and-zerosystem.interact
    import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    import logging

    import pytest

    import zero_system


    def test_is_sibling_request_true_cases():
        assert zero_system.is_sibling_request("أريد أخاً صغيراً يساعدني")
        assert zero_system.is_sibling_request("اريد شقيق اصغر للمساعدة")


    def test_is_sibling_request_false_cases():
        assert not zero_system.is_sibling_request("اريد اخ كبير")
        assert not zero_system.is_sibling_request("مرحبا كيف الحال؟")


    def test_zero_system_interact_sibling(capsys, caplog):
        caplog.set_level(logging.INFO)
        system = zero_system.ZeroSystem()
        response = system.interact("أريد أخاً صغيراً")
        out = capsys.readouterr().out
        assert "المستخدم: أريد أخاً صغيراً" in out
        assert "تم إنشاء أخ رقمي #1" in out
        assert response["sibling_id"] == "أخ رقمي #1"
        assert "Triggering sibling_genesis skill" in caplog.text
        assert system.interaction_count == 1


    def test_zero_system_interact_default(capsys, caplog):
        caplog.set_level(logging.INFO)
        system = zero_system.ZeroSystem()
        response = system.interact("مرحبا")
        out = capsys.readouterr().out
        assert "المستخدم: مرحبا" in out
        assert "أخوك الذكي" in response["output"]
        assert "AI response" in caplog.text
        assert system.interaction_count == 1
    =======
    import unittest

    from sss.zero_system import ZeroSystem

    class TestZeroSystem(unittest.TestCase):
        def test_create_sibling_increments_count(self):
            system = ZeroSystem()
            genesis_skill = system.skills["sibling_genesis"]
            before = genesis_skill.siblings_created
            system.create_sibling()
            after = genesis_skill.siblings_created
            self.assertEqual(after, before + 1)

    >>>>>>> main
  >>>>>>> main
