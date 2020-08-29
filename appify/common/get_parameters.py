"""
This module provides functions to get the parameters of a function/methods
"""
from __future__ import print_function

import sys
from collections import OrderedDict
from inspect import ismethod

from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.exceptions import IncompatibleParameter
from appify.common.parameter_info import ParameterInfo

if sys.version_info[0] > 2:
    from inspect import getfullargspec as getargspec
else:
    from inspect import getargspec


def get_parameter_default_annotations(func, keep_instance_ref=False):
    """
    Get all the parameter names, default values, and types from the signature
    :param func: function to extract parameter from
    :param keep_instance_ref: boolean indication if self, cls should be kept as parameter
    :return A dictionary with the parameter names as key and a ParameterInfo instance as value
    """
    params = getargspec(func)

    result = OrderedDict()
    if not params.args:
        return result

    if not keep_instance_ref and ismethod(func):
        params.args.pop(0)

    defaults = params.defaults or []

    nb_defaults = len(defaults)
    # Trick to ensure that params.args[:-nb_defaults] returns the full array when
    # there is no default values
    if nb_defaults == 0:
        nb_defaults = -len(params.args)
    for name in params.args[:-nb_defaults]:
        result[name] = ParameterInfo(name, required=True)
    for name, default in zip(params.args[-nb_defaults:], defaults):
        result[name] = ParameterInfo(name, default=default)

    # Gettattr has to be used because of the compability with 2.7
    for name, type_ in getattr(params, "annotations", {}).items():
        result[name].type = str(type_.__name__)

    return result


def get_parameter_infos(func, doc_parser=None):
    """
    Get all the ParameterInfos from the func declaration and docstring
    :param func: function to get the parameter infos from
    :param doc_parser: the docstring parser to use (default: RestructuredParser)
    :return: Dictionary containing the retrieved ParameterInfo, the parameter is used as key
    """
    if doc_parser is None:
        doc_parser = RestructuredParser()

    func_param_infos = get_parameter_default_annotations(func)
    doc_param_infos = doc_parser.parse(func.__doc__) if func.__doc__ else {}

    for name, info in func_param_infos.items():
        if name not in doc_param_infos:
            continue
        try:
            info.update(doc_param_infos[name])
        except IncompatibleParameter as e:
            raise IncompatibleParameter(
                "Information on parameter {} does not match between "
                "function declaration and docstring.\n{}".format(name, str(e))
            )

    return func_param_infos
