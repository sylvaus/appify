import pytest

from appify.common.exceptions import IncompatibleParameter
from appify.common.get_parameters import get_parameter_infos


def test_get_parameter_info_raise_incompatible_parameter_when_docstring_and_hinting_conflict():
    def func(a: int, bool_flag=False):
        """
        :param a:
        :type a: str
        :param bool_flag:
        :type bool_flag: bool
        :return:
        """
        pass

    with pytest.raises(IncompatibleParameter):
        get_parameter_infos(func)
