from argparse import ArgumentTypeError
from unittest import TestCase

from appify.common.input_parser.input_parser import StrInputParser, IntInputParser, FloatInputParser, BoolInputParser


class TestStrInputParser(TestCase):
    def test_parse_nominal_case(self):
        parser = StrInputParser()
        self.assertEqual("a bit useless", parser.parse("a bit useless"))


class TestIntInputParser(TestCase):
    def test_parse_decimal(self):
        parser = IntInputParser()
        self.assertEqual(1234789, parser.parse("1234789"))
        self.assertEqual(0, parser.parse("0"))
        self.assertEqual(978456, parser.parse(" 978456 "))
        self.assertEqual(-978456, parser.parse(" -978456 "))

    def test_parse_hexadecimal(self):
        parser = IntInputParser()
        self.assertEqual(0x1234789, parser.parse("0x1234789"))
        self.assertEqual(0x0, parser.parse("0x0"))
        self.assertEqual(0x978456, parser.parse(" 0x978456 "))

    def test_parse_binary(self):
        parser = IntInputParser()
        self.assertEqual(0b001101101011010, parser.parse("0b001101101011010"))
        self.assertEqual(0b0, parser.parse("0b0"))
        self.assertEqual(0b11111, parser.parse(" 0b11111 "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        with self.assertRaises(ArgumentTypeError):
            parser.parse("invalid_number")


class TestFloatInputParser(TestCase):
    def test_parse_float(self):
        parser = FloatInputParser()
        self.assertEqual(0.4, parser.parse("0.4"))
        self.assertEqual(40, parser.parse("40"))
        self.assertEqual(-12.5, parser.parse(" -12.5 "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        with self.assertRaises(ArgumentTypeError):
            parser.parse("invalid_number")


class TestBoolInputParser(TestCase):
    def test_parse_bool(self):
        parser = BoolInputParser()
        self.assertEqual(True, parser.parse("true"))
        self.assertEqual(True, parser.parse(" 1"))
        self.assertEqual(True, parser.parse(" True "))
        self.assertEqual(False, parser.parse(" 0 "))
        self.assertEqual(False, parser.parse("false "))
        self.assertEqual(False, parser.parse(" False "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        with self.assertRaises(ArgumentTypeError):
            parser.parse("invalid_number")
