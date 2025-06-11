import os
import sys

  <<<<<<< codex/remove-conflict-markers-and-refactor-tests
  ROOT = os.path.dirname(os.path.dirname(__file__))
  =======
  ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  >>>>>>> main
  if ROOT not in sys.path:
      sys.path.insert(0, ROOT)
