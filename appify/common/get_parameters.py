"""
This module provides functions to get the parameters of a function/methods
"""
from __future__ import print_function

import sys

if sys.version_info[0] > 2:
    from inspect import getfullargspec as getargspec
else:
    from inspect import getargspec


def get_parameters(func):
    def f(text: str, text2, text3, text4=4, *args, **kwargs):
        pass

    params = getargspec(f)
    pass
