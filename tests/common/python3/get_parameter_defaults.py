from appify.common.get_parameters import get_parameter_default_annotations
from appify.common.parameter_info import NoDefault, ParameterInfo


def test_get_parameters_single_param_str_annotation():
    def func(a: str):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a"]
    assert parameter_infos["a"] == ParameterInfo(
        "a", type_="str", default=NoDefault, required=True
    )


def test_get_parameters_single_param_str_annotation_str_default():
    def func(a: str = "ab"):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert parameter_infos["a"] == ParameterInfo(
        "a", type_="str", default="ab", required=False
    )


def test_get_parameters_multiple_params_defaults_annotations():
    def func(a, a_b=12.5, T_test_param: str = "abcd", underscore_: int = 123):
        pass

    parameter_infos = get_parameter_default_annotations(func)
    assert list(parameter_infos.keys()) == ["a", "a_b", "T_test_param", "underscore_"]
    assert parameter_infos["a"] == ParameterInfo("a", default=NoDefault, required=True)
    assert parameter_infos["a_b"] == ParameterInfo("a_b", default=12.5, required=False)
    assert parameter_infos["T_test_param"] == ParameterInfo(
        "T_test_param", type_="str", default="abcd", required=False
    )
    assert parameter_infos["underscore_"] == ParameterInfo(
        "underscore_", type_="int", default=123, required=False
    )
