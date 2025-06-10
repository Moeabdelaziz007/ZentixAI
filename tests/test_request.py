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
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            response = system.interact(message)
        captured = buf.getvalue()
        self.assertIn("المستخدم: مرحبا", captured)
        self.assertIn("الذكاء:", captured)
        self.assertEqual(response["status"], "success")


if __name__ == "__main__":
    unittest.main()
