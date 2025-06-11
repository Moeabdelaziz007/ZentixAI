import io
import contextlib
import logging
import unittest

from sss.zero_system import ZeroSystem, is_sibling_request


class TestZeroSystem(unittest.TestCase):
    def test_is_sibling_request_true_cases(self):
        self.assertTrue(is_sibling_request("أريد أخاً صغيراً يساعدني"))
        self.assertTrue(is_sibling_request("اريد شقيق اصغر للمساعدة"))

    def test_is_sibling_request_false_cases(self):
        self.assertFalse(is_sibling_request("اريد اخ كبير"))
        self.assertFalse(is_sibling_request("مرحبا كيف الحال؟"))

    def test_create_sibling_increments_count(self):
        system = ZeroSystem()
        genesis_skill = system.skills["sibling_genesis"]
        before = genesis_skill.siblings_created
        system.create_sibling()
        after = genesis_skill.siblings_created
        self.assertEqual(after, before + 1)

    def test_interact_sibling(self):
        system = ZeroSystem()
        buf = io.StringIO()
        with self.assertLogs(level="INFO") as log, contextlib.redirect_stdout(buf):
            response = system.interact("أريد أخاً صغيراً")
        out = buf.getvalue()
        self.assertIn("المستخدم: أريد أخاً صغيراً", out)
        self.assertIn("تم إنشاء أخ رقمي", out)
        self.assertEqual(response["sibling_id"], "أخ رقمي #1")
        self.assertIn("Triggering sibling_genesis skill", "\n".join(log.output))
        self.assertEqual(system.interaction_count, 1)

    def test_interact_default(self):
        system = ZeroSystem()
        buf = io.StringIO()
        with self.assertLogs(level="INFO") as log, contextlib.redirect_stdout(buf):
            response = system.interact("مرحبا")
        out = buf.getvalue()
        self.assertIn("المستخدم: مرحبا", out)
        self.assertIn("أخوك الذكي", response["output"])
        self.assertTrue(any("AI response" in record for record in log.output))
        self.assertEqual(system.interaction_count, 1)

    def test_system_status_contains_fields(self):
        system = ZeroSystem()
        status = system.system_status()
        self.assertIn("uptime", status)
        self.assertIn("interactions", status)
        self.assertIn("skills", status)
        self.assertIn("dna_backup", status)


if __name__ == "__main__":
    unittest.main()
