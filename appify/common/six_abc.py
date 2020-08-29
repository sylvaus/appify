"""
Hack to have a uniform way of defining Abstract Base Classes
"""

import sys

if sys.version_info >= (3, 4):
    pass
else:
    from abc import ABCMeta

    ABC = ABCMeta("ABC", (), {})
