  <<<<<<< codex/remove-import-logging-from-test_request.py
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
=======
"""Test package initialization."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
 main
