import unittest
from zero_system import ZeroSystem

class TestZeroSystem(unittest.TestCase):
    def test_create_sibling_increments(self):
        system = ZeroSystem()
        skill = system.skills["sibling_genesis"]
        self.assertEqual(skill.siblings_created, 0)

        system.create_sibling()
        self.assertEqual(skill.siblings_created, 1)

        system.create_sibling()
        self.assertEqual(skill.siblings_created, 2)

if __name__ == "__main__":
    unittest.main()
