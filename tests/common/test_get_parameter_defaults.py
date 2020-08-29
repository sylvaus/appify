# noinspection PyUnresolvedReferences
from appify.common.get_parameters import get_parameter_default_annotations
# noinspection PyUnresolvedReferences
from appify.common.parameter_info import NoDefault

from .. import PYTHON3

if PYTHON3:
    from .python3.get_parameter_defaults import *


def test_get_parameters_no_param():
    def func():
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == []


def test_get_parameters_single_param_no_default():
    def func(a):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].required


def test_get_parameters_single_param_str_default():
    def func(a="ab"):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].default == "ab"
    assert not parameter_infos["a"].required


def test_get_parameters_multiple_params_no_default():
    def func(a, a_b, T_test_param, underscore_):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].required == True
    assert parameter_infos["a_b"].name == "a_b"
    assert parameter_infos["a_b"].required == True
    assert parameter_infos["T_test_param"].name == "T_test_param"
    assert parameter_infos["T_test_param"].required == True
    assert parameter_infos["underscore_"].name == "underscore_"
    assert parameter_infos["underscore_"].required == True


def test_get_parameters_multiple_params_defaults():
    def func(a, a_b=12.5, T_test_param="abcd", underscore_=123):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].default == NoDefault
    assert parameter_infos["a"].required == True
    assert parameter_infos["a_b"].name == "a_b"
    assert parameter_infos["a_b"].default == 12.5
    assert parameter_infos["a_b"].required == False
    assert parameter_infos["T_test_param"].name == "T_test_param"
    assert parameter_infos["T_test_param"].default == "abcd"
    assert parameter_infos["T_test_param"].required == False
    assert parameter_infos["underscore_"].name == "underscore_"
    assert parameter_infos["underscore_"].default == 123
    assert parameter_infos["underscore_"].required == False


def test_get_parameters_multiple_params_no_default_method():
    class TmpClass:
        def tmp(self, a, a_b, T_test_param, underscore_):
            pass

    inst = TmpClass()
    func = inst.tmp

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].required == True
    assert parameter_infos["a_b"].name == "a_b"
    assert parameter_infos["a_b"].required == True
    assert parameter_infos["T_test_param"].name == "T_test_param"
    assert parameter_infos["T_test_param"].required == True
    assert parameter_infos["underscore_"].name == "underscore_"
    assert parameter_infos["underscore_"].required == True
