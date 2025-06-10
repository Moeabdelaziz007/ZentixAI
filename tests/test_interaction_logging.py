import os
import json
import unittest
import zero_system as zs

class TestInteractionLogging(unittest.TestCase):
    def test_interact_creates_log_file(self):
        log_path = os.path.join(os.path.dirname(zs.__file__), 'log.jsonl')
        if os.path.exists(log_path):
            os.remove(log_path)
        system = zs.ZeroSystem()
        system.interact('اختبار التسجيل')
        self.assertTrue(os.path.exists(log_path))
        with open(log_path, encoding='utf-8') as f:
            lines = f.readlines()
        self.assertGreaterEqual(len(lines), 1)
        entry = json.loads(lines[-1])
        self.assertEqual(entry['message'], 'اختبار التسجيل')
        self.assertIn('response', entry)

