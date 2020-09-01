from appify.common.doc_parser.restructured_parser import RestructuredParser


def test_parse_same_line_docstring():
    def f(a, b, c):
        """
        f does this

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


def test_parse_multiple_lines_docstring():
    def f(a, b, c):
        """
        f does this

        :param a: documentation a
            and some more
        :type a: int
        :param  b : documentation b
            and some more again
        :type b : str
        should not be considered
        :param  c:
            documentation c
        :type c: bool
        :return:
        """
        pass

    parser = RestructuredParser()
    arguments = parser.parse(f.__doc__)
    assert list(arguments.keys()) == ["a", "b", "c"]
    assert arguments["a"].name == "a"
    assert arguments["a"].type == "int"
    assert arguments["a"].description.strip() == "documentation a and some more"

    assert arguments["b"].name == "b"
    assert arguments["b"].type == "str"
    assert arguments["b"].description.strip() == "documentation b and some more again"

    assert arguments["c"].name == "c"
    assert arguments["c"].type == "bool"
    assert arguments["c"].description.strip() == "documentation c"


def test_parse_only_types_docstring():
    def f(a, b):
        """
        f does this

        :type a: int
        :type b : str
        :return:
        """
        pass

    parser = RestructuredParser()
    arguments = parser.parse(f.__doc__)
    assert list(arguments.keys()) == ["a", "b"]
    assert arguments["a"].name == "a"
    assert arguments["a"].type == "int"
    assert arguments["a"].description is None

    assert arguments["b"].name == "b"
    assert arguments["b"].type == "str"
    assert arguments["b"].description is None
