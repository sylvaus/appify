"""
Hack to have a uniform way of defining Abstract Base Classes
"""

import abc
import sys

if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta("ABC", (), {})
