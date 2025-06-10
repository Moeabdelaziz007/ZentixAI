import os
import json
import tempfile
import unittest
import zero_system as zs

class TestInteractionLogging(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for logging."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_file = os.path.join(self.temp_dir.name, 'log.jsonl')

    def tearDown(self):
        """Clean up the temporary log directory."""
        self.temp_dir.cleanup()

    def test_interact_creates_log_file(self):
        system = zs.ZeroSystem(log_filename=self.log_file)
        system.interact('اختبار التسجيل')
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, encoding='utf-8') as f:
            lines = f.readlines()
        self.assertGreaterEqual(len(lines), 1)
        entry = json.loads(lines[-1])
        self.assertEqual(entry['message'], 'اختبار التسجيل')
        self.assertIn('response', entry)

