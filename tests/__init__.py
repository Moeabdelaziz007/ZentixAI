"""Test package initialization."""
import os
import sys

  <<<<<<< codex/verify-readme-for-correctness
  =======
# Ensure project root is on the import path
 main
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
