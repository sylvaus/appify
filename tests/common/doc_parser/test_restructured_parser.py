from unittest import TestCase

from appify.common.doc_parser.restructured_parser import RestructuredParser


class TestRestructuredParser(TestCase):
    def test_parse_same_line_docstring(self):
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
        self.assertListEqual(["a", "b", "c"], list(arguments.keys()))
        self.assertEqual("a", arguments["a"].name)
        self.assertEqual("int", arguments["a"].type)
        self.assertEqual("documentation a", arguments["a"].description.strip())

        self.assertEqual("b", arguments["b"].name)
        self.assertEqual("str", arguments["b"].type)
        self.assertEqual("documentation b", arguments["b"].description.strip())

        self.assertEqual("c", arguments["c"].name)
        self.assertEqual("bool", arguments["c"].type)
        self.assertEqual("documentation c", arguments["c"].description.strip())

