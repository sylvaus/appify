"""
This module provides functions to get the parameters of a function/methods
"""
from __future__ import print_function

import sys
from collections import OrderedDict

from appify.common.parameter_info import ParameterInfo

if sys.version_info[0] > 2:
    from inspect import getfullargspec as getargspec
    from itertools import zip_longest as izip_longest
else:
    from inspect import getargspec
    from itertools import izip_longest


def get_parameter_default_annotations(func):
    result = OrderedDict()
    params = getargspec(func)

    if not params.args:
        return result

    if params.defaults is None:
        defaults = []
    else:
        defaults = params.defaults

    name_defaults = list(izip_longest(
        reversed(params.args), reversed(defaults), fillvalue=None))
    for name, default in reversed(name_defaults):
        result[name] = ParameterInfo(name, default=default)

    if hasattr(params, "annotations") and params.annotations:
        for name, type_ in params.annotations.items():
            result[name].type = str(type_.__name__)

    return result


