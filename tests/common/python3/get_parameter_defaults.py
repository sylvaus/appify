import sys

import pytest

from appify.common.get_parameters import get_parameter_default_annotations
from appify.common.parameter_info import NoDefault


@pytest.mark.skipif(sys.version_info < (3,), reason="requires python3")
def test_get_parameters_single_param_str_annotation():
    def func(a: str):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].type == "str"
    assert parameter_infos["a"].required


@pytest.mark.skipif(sys.version_info < (3,), reason="requires python3")
def test_get_parameters_single_param_str_annotation_str_default():
    def func(a: str = "ab"):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].type == "str"
    assert parameter_infos["a"].default == "ab"
    assert not parameter_infos["a"].required


@pytest.mark.skipif(sys.version_info < (3,), reason="requires python3")
def test_get_parameters_multiple_params_defaults_annotations():
    def func(a, a_b=12.5, T_test_param: str = "abcd", underscore_: int = 123):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"].name == "a"
    assert parameter_infos["a"].default == NoDefault
    assert parameter_infos["a"].type is None
    assert parameter_infos["a"].required
    assert parameter_infos["a_b"].name == "a_b"
    assert parameter_infos["a_b"].default == 12.5
    assert parameter_infos["a_b"].type is None
    assert not parameter_infos["a_b"].required
    assert parameter_infos["T_test_param"].name == "T_test_param"
    assert parameter_infos["T_test_param"].default == "abcd"
    assert parameter_infos["T_test_param"].type == "str"
    assert not parameter_infos["T_test_param"].required
    assert parameter_infos["underscore_"].name == "underscore_"
    assert parameter_infos["underscore_"].default == 123
    assert parameter_infos["underscore_"].type == "int"
    assert not parameter_infos["underscore_"].required
