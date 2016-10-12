"""Provide context to the test runner.

Allows for running the tests without requiring the package to be installed. See
http://docs.python-guide.org/en/latest/writing/structure/#test-suite
for more information.
"""
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import src.delver.delve as delve
