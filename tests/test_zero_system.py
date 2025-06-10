import unittest

from sss.zero_system import ZeroSystem, is_sibling_request


class TestZeroSystem(unittest.TestCase):
    def test_is_sibling_request_true(self):
        self.assertTrue(is_sibling_request("اريد اخ صغير يساعدني"))

    def test_is_sibling_request_false(self):
        self.assertFalse(is_sibling_request("مرحبا كيف الحال"))

    def test_system_status_contains_fields(self):
        system = ZeroSystem()
        status = system.system_status()
        for field in ["uptime", "interactions", "skills", "dna_backup"]:
            self.assertIn(field, status)

    def test_create_sibling_increments_count(self):
        system = ZeroSystem()
        first = system.create_sibling()
        second = system.create_sibling()
        self.assertNotEqual(first["sibling_id"], second["sibling_id"])


if __name__ == "__main__":
    unittest.main()
