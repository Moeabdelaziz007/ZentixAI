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
