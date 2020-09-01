# noinspection PyUnresolvedReferences
from appify.common.get_parameters import get_parameter_default_annotations

# noinspection PyUnresolvedReferences
from appify.common.parameter_info import NoDefault, ParameterInfo
from ..utils import PYTHON3

if PYTHON3:
    from .python3.get_parameter_defaults import *  # noqa: F403 F401


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
    assert parameter_infos["a"] == ParameterInfo("a", default=NoDefault, required=True)


def test_get_parameters_single_param_str_default():
    def func(a="ab"):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"] == ParameterInfo("a", default="ab", required=False)


def test_get_parameters_multiple_params_no_default():
    def func(a, a_b, T_test_param, underscore_):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"] == ParameterInfo("a", default=NoDefault, required=True)
    assert parameter_infos["a_b"] == ParameterInfo(
        "a_b", default=NoDefault, required=True
    )
    assert parameter_infos["T_test_param"] == ParameterInfo(
        "T_test_param", default=NoDefault, required=True
    )
    assert parameter_infos["underscore_"] == ParameterInfo(
        "underscore_", default=NoDefault, required=True
    )


def test_get_parameters_multiple_params_defaults():
    def func(a, a_b=12.5, T_test_param="abcd", underscore_=123):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"] == ParameterInfo("a", default=NoDefault, required=True)
    assert parameter_infos["a_b"] == ParameterInfo("a_b", default=12.5, required=False)
    assert parameter_infos["T_test_param"] == ParameterInfo(
        "T_test_param", default="abcd", required=False
    )
    assert parameter_infos["underscore_"] == ParameterInfo(
        "underscore_", default=123, required=False
    )


def test_get_parameters_multiple_params_no_default_method():
    class TmpClass:
        def tmp(self, a, a_b, T_test_param, underscore_):
            pass

    inst = TmpClass()
    func = inst.tmp

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"] == ParameterInfo("a", default=NoDefault, required=True)
    assert parameter_infos["a_b"] == ParameterInfo(
        "a_b", default=NoDefault, required=True
    )
    assert parameter_infos["T_test_param"] == ParameterInfo(
        "T_test_param", default=NoDefault, required=True
    )
    assert parameter_infos["underscore_"] == ParameterInfo(
        "underscore_", default=NoDefault, required=True
    )
