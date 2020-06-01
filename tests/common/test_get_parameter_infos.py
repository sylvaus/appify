from appify.common.doc_parser.doc_parser import DocParser
from appify.common.get_parameters import get_parameter_infos
from appify.common.parameter_info import ParameterInfo


class MockDockParser(DocParser):
    def __init__(self, output):
        self.output = output

    def parse(self, docstring):
        return self.output


def test_get_parameter_info_no_param():
    """
    get_parameter_infos should always return an empty dict independently of the
    information provided in the docstring
    """

    def func():
        pass

    result = get_parameter_infos(func, doc_parser=MockDockParser({}))
    assert result == {}

    result = get_parameter_infos(
        func, doc_parser=MockDockParser(
            {"a": ParameterInfo("a", "str"), "bool_flag": ParameterInfo("bool_flag", default=False)}
        )
    )
    assert result == {}
