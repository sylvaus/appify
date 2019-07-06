"""
This module provides functions to get the parameters of a function/methods
"""
from __future__ import print_function

import sys
from collections import OrderedDict

from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.parameter_info import ParameterInfo, IncompatibleParameter

from inspect import ismethod
if sys.version_info[0] > 2:
    from inspect import getfullargspec as getargspec
else:
    from inspect import getargspec


def get_parameter_default_annotations(func, keepInstanceRef=False):
    """
    Get all the parameter names, default values, and types from the signature
    :param func: function to extract parameter from
    :param keepInstanceRef: boolean indication if self, cls should be kept as parameter
    :return A dictionary with the parameter names as key and a ParameterInfo instance as value
    :rtype Dict[str, ParameterInfo]
    """
    result = OrderedDict()
    params = getargspec(func)

    if not params.args:
        return result

    if not keepInstanceRef and ismethod(func):
        params.args.pop(0)

    if params.defaults is None:
        defaults = []
    else:
        defaults = params.defaults

    nb_defaults = len(defaults)
    # Trick to ensure that params.args[:-nb_defaults] returns the full array when
    # there is no default values
    if nb_defaults == 0:
        nb_defaults = -len(params.args)
    for name in params.args[:-nb_defaults]:
        result[name] = ParameterInfo(name, required=True)
    for name, default in zip(params.args[-nb_defaults:], defaults):
        result[name] = ParameterInfo(name, default=default)

    if hasattr(params, "annotations") and params.annotations:
        for name, type_ in params.annotations.items():
            result[name].type = str(type_.__name__)

    return result


def get_parameter_infos(func, doc_parser=RestructuredParser()):
    """
    Get all the ParameterInfos from the func declaration and docstring
    :param func:
        function to get the parameter infos from
    :param doc_parser:
        the docstring parser to use (default: RestructuredParser)
    :return: Dictionary containing the retrieved ParameterInfo, the parameter is used as key
    """
    func_param_infos = get_parameter_default_annotations(func)
    doc_param_infos = doc_parser.parse(func.__doc__) if func.__doc__ else []

    for name, info in func_param_infos.items():
        if name not in doc_param_infos:
            continue
        try:
            func_param_infos[name].update(doc_param_infos[name])
        except IncompatibleParameter as e:
            raise IncompatibleParameter("Information on parameter {} does not match between "
                                        "function declaration and docstring.\n{}"
                                        .format(name, str(e)))

    return func_param_infos
