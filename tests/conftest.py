import os
import sys

  <<<<<<< codex/convert-unittest-to-pytest
  # Ensure the project root is on sys.path so `sss` can be imported when running pytest
  ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  if ROOT_DIR not in sys.path:
      sys.path.insert(0, ROOT_DIR)
  =======
  # Ensure project root is on sys.path for test imports
  sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
  >>>>>>> main
