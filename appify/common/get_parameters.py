"""
This module provides functions to get the parameters of a function/methods
"""
from __future__ import print_function

import sys

if sys.version_info[0] > 2:
    from inspect import getfullargspec as getargspec
else:
    from inspect import getargspec


# TODO: to be done by the end of the week(20-03-2019) + UT
def get_parameters_and_defaults(func):
    params = getargspec(func)

