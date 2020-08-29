"""
Hack to have a uniform way of defining Abstract Base Classes
"""

import sys


if sys.version_info >= (3, 4):
    # noinspection PyUnresolvedReferences
    from abc import ABC
else:
    from abc import ABCMeta

    ABC = ABCMeta("ABC", (), {})
