  <<
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    import io
    import contextlib
    import logging
    import unittest
    =======
      import logging
      <<<<<<< codex/update-import-for-zero_system-module
      import pytest
      from zero_system import is_sibling_request, ZeroSystem
      =======
        <<<<<<< fmzv63-codex/rewrite-tests-to-use-unittest

        from sss.zero_system import is_sibling_request, ZeroSystem
        =======
        >>>>>>> main
    >>>>>>> main
  <<<<< codex/remove-merge-markers-and-refactor-logging-setup
  import os, sys


  from sss.zero_system import is_sibling_request, ZeroSystem
  >>>>>>> main


  class TestRequest(unittest.TestCase):
      def test_is_sibling_request_true(self):
          self.assertTrue(is_sibling_request("اريد اخ صغير يساعدني"))

  <<<<<<< codex/remove-merge-markers-and-refactor-logging-setup
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
          self.assertIn(f"\U0001f464 المستخدم: {message}", captured)
          self.assertIn("\U0001f916 الذكاء:", captured)
          self.assertEqual(response["status"], "success")
          log_text = "\n".join(log.output)
          self.assertIn(f"User message: {message}", log_text)
          self.assertTrue(any("AI response" in record for record in log.output))
  =======

        def test_is_sibling_request_false(self):
            self.assertFalse(is_sibling_request("اريد صديق جديد"))


        def test_interact_logs_and_output(self):
            system = ZeroSystem()
            message = "مرحبا"
            user = {"id": "u", "name": "Test"}
            buf = io.StringIO()
            with self.assertLogs(level="INFO") as log, \
                 contextlib.redirect_stdout(buf):
                response = system.interact(message, user)
            captured = buf.getvalue()
            self.assertIn(f"\U0001F464 المستخدم: {message}", captured)
            self.assertIn("\U0001F916 الذكاء:", captured)
            self.assertEqual(response["status"], "success")
            log_text = "\n".join(log.output)
            self.assertIn(f"User message: {message}", log_text)
            self.assertTrue(any("AI response:" in record for record in log.output))
  >>>>>>> main


  if __name__ == "__main__":
      unittest.main()
