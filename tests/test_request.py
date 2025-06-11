import logging
import unittest
import io
import contextlib

from sss.zero_system import is_sibling_request, ZeroSystem


class TestRequest(unittest.TestCase):
    def test_is_sibling_request_true(self):
        self.assertTrue(is_sibling_request("اريد اخ صغير يساعدني"))

    def test_is_sibling_request_false(self):
        self.assertFalse(is_sibling_request("اريد صديق جديد"))

    def test_interact_logs_and_output(self):
        system = ZeroSystem()
        message = "مرحبا"
        user = {"id": "u", "name": "Test"}
        buf = io.StringIO()
        with self.assertLogs(level="INFO") as log, contextlib.redirect_stdout(buf):
            response = system.interact(message, user)
        captured = buf.getvalue()
        self.assertIn(f"\U0001F464 المستخدم: {message}", captured)
        self.assertIn("\U0001F916 الذكاء:", captured)
        self.assertEqual(response["status"], "success")
        log_text = "\n".join(log.output)
        self.assertIn(f"User message: {message}", log_text)
        self.assertTrue(any("AI response:" in record for record in log.output))
