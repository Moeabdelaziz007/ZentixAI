import logging
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from zero_system import ZeroSystem, is_sibling_request


class TestZeroSystem(unittest.TestCase):
    def test_is_sibling_request_detects_true(self):
        self.assertTrue(is_sibling_request("اريد اخ صغير يساعدني"))

    def test_is_sibling_request_detects_false(self):
        self.assertFalse(is_sibling_request("مرحبا كيف الحال"))

    def test_system_status_contains_fields(self):
        system = ZeroSystem()
        status = system.system_status()
        self.assertIn("uptime", status)
        self.assertIn("interactions", status)
        self.assertIn("skills", status)
        self.assertIn("dna_backup", status)

    def test_create_sibling_increments_count(self):
        system = ZeroSystem()
        first = system.create_sibling()
        second = system.create_sibling()
        self.assertNotEqual(first["sibling_id"], second["sibling_id"])

    def test_interact_sibling(self):
        system = ZeroSystem()
        with self.assertLogs(level="INFO") as log:
            response = system.interact("أريد أخاً صغيراً")
        self.assertEqual(response["sibling_id"], "أخ رقمي #1")
        self.assertIn("Triggering sibling_genesis skill", "\n".join(log.output))

    def test_interact_default(self):
        system = ZeroSystem()
        with self.assertLogs(level="INFO") as log:
            response = system.interact("مرحبا")
        self.assertIn("أخوك الذكي", response["output"])
        self.assertTrue(any("AI response" in record for record in log.output))


if __name__ == "__main__":
    unittest.main()
