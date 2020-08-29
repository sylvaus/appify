from appify.common.get_parameters import get_parameter_infos
from appify.common.parameter_info import ParameterInfo


def test_get_parameter_info_should_return_empty_dict_for_a_func_with_no_parameters():
    def func():
        pass

    result = get_parameter_infos(func)
    assert result == {}, "Function with no parameter should no get any parameter info"

    def func():
        """
        :param a:
        :type a: str
        :param bool_flag:
        :type bool_flag: bool
        :return:
        """
        pass

    result = get_parameter_infos(func)
    assert result == {}, "Function with no parameter should no get any parameter info even with docstring"


def test_get_parameter_info_should_return_combine_information_from_signature_and_docstring():
    def func(a, bool_flag=False):
        """
        :param a:
        :type a: str
        :param bool_flag:
        :type bool_flag: bool
        :return:
        """
        pass

    result = get_parameter_infos(func)
    assert result["a"] == ParameterInfo("a", "str", required=True)
    assert result["bool_flag"] == ParameterInfo("bool_flag", "bool", default=False)
