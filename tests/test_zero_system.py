import io
import contextlib
import unittest

from sss.zero_system import ZeroSystem, is_sibling_request


class TestZeroSystem(unittest.TestCase):
    def setUp(self):
        self.system = ZeroSystem()

    def test_is_sibling_request_true_cases(self):
        self.assertTrue(is_sibling_request("أريد أخاً صغيراً يساعدني"))
        self.assertTrue(is_sibling_request("اريد شقيق اصغر للمساعدة"))

    def test_is_sibling_request_false_cases(self):
        self.assertFalse(is_sibling_request("اريد اخ كبير"))
        self.assertFalse(is_sibling_request("مرحبا كيف الحال؟"))

    def test_interact_sibling(self):
        buf = io.StringIO()
        with self.assertLogs(level="INFO") as log, contextlib.redirect_stdout(buf):
            response = self.system.interact("أريد أخاً صغيراً")
        output = buf.getvalue()
        self.assertIn("المستخدم: أريد أخاً صغيراً", output)
        self.assertIn("تم إنشاء أخ رقمي #1", output)
        self.assertEqual(response["sibling_id"], "أخ رقمي #1")
        self.assertIn("Triggering sibling_genesis skill", "\n".join(log.output))
        self.assertEqual(self.system.interaction_count, 1)

    def test_interact_default(self):
        buf = io.StringIO()
        with self.assertLogs(level="INFO") as log, contextlib.redirect_stdout(buf):
            response = self.system.interact("مرحبا")
        output = buf.getvalue()
        self.assertIn("المستخدم: مرحبا", output)
        self.assertIn("أخوك الذكي", response["output"])
        self.assertIn("AI response", "\n".join(log.output))
        self.assertEqual(self.system.interaction_count, 1)

    def test_create_sibling_increments_count(self):
        genesis_skill = self.system.skills["sibling_genesis"]
        before = genesis_skill.siblings_created
        self.system.create_sibling()
        after = genesis_skill.siblings_created
        self.assertEqual(after, before + 1)


if __name__ == "__main__":
    unittest.main()

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
