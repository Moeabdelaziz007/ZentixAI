import os
import sys

# Ensure the project root is on the path so 'sss' imports work when running tests
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
