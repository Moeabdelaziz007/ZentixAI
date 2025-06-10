  <<<<<<< codex/edit-sys.path-in-tests/__init__.py
  import os, sys
  ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
  if ROOT_DIR not in sys.path:
      sys.path.insert(0, ROOT_DIR)
  =======
  """Test package initialization."""
  import os
  import sys

  # Ensure project root is on the import path
  ROOT = os.path.dirname(os.path.dirname(__file__))
  if ROOT not in sys.path:
      sys.path.insert(0, ROOT)
  >>>>>>> main
