import unittest

from sss.zero_system import ZeroSystem, is_sibling_request


class TestZeroSystem(unittest.TestCase):
    def test_is_sibling_request_detects_true(self):
        self.assertTrue(is_sibling_request("اريد اخ صغير يساعدني"))

    def test_is_sibling_request_detects_false(self):
        self.assertFalse(is_sibling_request("مرحبا كيف الحال"))

    def test_zero_system_status_contains_fields(self):
        system = ZeroSystem()
        status = system.system_status()
        self.assertIn("uptime", status)
        self.assertIn("interactions", status)
        self.assertIn("skills", status)
        self.assertIn("dna_backup", status)

    def test_create_sibling_increments_count(self):
        system = ZeroSystem()
        genesis_skill = system.skills["sibling_genesis"]
        before = genesis_skill.siblings_created
        system.create_sibling()
        after = genesis_skill.siblings_created
        self.assertEqual(after, before + 1)


if __name__ == "__main__":
    unittest.main()
