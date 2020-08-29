from appify.common.doc_parser.restructured_parser import RestructuredParser


def test_parse_same_line_docstring():
    def f(a, b, c):
        """
        :param a: documentation a
        :type a: int
        :param  b : documentation b
        :type b : str
        :param  c: documentation c
        :type c: bool
        :return:
        """
        pass

    parser = RestructuredParser()
    arguments = parser.parse(f.__doc__)
    assert list(arguments.keys()) == ["a", "b", "c"]
    assert arguments["a"].name == "a"
    assert arguments["a"].type == "int"
    assert arguments["a"].description.strip() == "documentation a"

    assert arguments["b"].name == "b"
    assert arguments["b"].type == "str"
    assert arguments["b"].description.strip() == "documentation b"

    assert arguments["c"].name == "c"
    assert arguments["c"].type == "bool"
    assert arguments["c"].description.strip() == "documentation c"
