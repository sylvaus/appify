from unittest import TestCase

from appify.common.input_parser.input_parser import StrInputParser, IntInputParser, FloatInputParser, BoolInputParser


class TestStrInputParser(TestCase):
    def test_parse_nominal_case(self):
        parser = StrInputParser()
        self.assertTupleEqual((True, "a bit useless"), parser.parse("a bit useless"))


class TestIntInputParser(TestCase):
    def test_parse_decimal(self):
        parser = IntInputParser()
        self.assertTupleEqual((True, 1234789), parser.parse("1234789"))
        self.assertTupleEqual((True, 0), parser.parse("0"))
        self.assertTupleEqual((True, 978456), parser.parse(" 978456 "))
        self.assertTupleEqual((True, -978456), parser.parse(" -978456 "))

    def test_parse_hexadecimal(self):
        parser = IntInputParser()
        self.assertTupleEqual((True, 0x1234789), parser.parse("0x1234789"))
        self.assertTupleEqual((True, 0x0), parser.parse("0x0"))
        self.assertTupleEqual((True, 0x978456), parser.parse(" 0x978456 "))

    def test_parse_binary(self):
        parser = IntInputParser()
        self.assertTupleEqual((True, 0b001101101011010), parser.parse("0b001101101011010"))
        self.assertTupleEqual((True, 0b0), parser.parse("0b0"))
        self.assertTupleEqual((True, 0b11111), parser.parse(" 0b11111 "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        success, error = parser.parse("invalid_number")
        self.assertFalse(success)
        self.assertIn("Could not convert", error)


class TestFloatInputParser(TestCase):
    def test_parse_float(self):
        parser = FloatInputParser()
        self.assertTupleEqual((True, 0.4), parser.parse("0.4"))
        self.assertTupleEqual((True, 40), parser.parse("40"))
        self.assertTupleEqual((True, -12.5), parser.parse(" -12.5 "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        success, error = parser.parse("invalid_number")
        self.assertFalse(success)
        self.assertIn("Could not convert", error)


class TestBoolInputParser(TestCase):
    def test_parse_float(self):
        parser = BoolInputParser()
        self.assertTupleEqual((True, True), parser.parse("true"))
        self.assertTupleEqual((True, True), parser.parse(" 1"))
        self.assertTupleEqual((True, True), parser.parse(" True "))
        self.assertTupleEqual((True, False), parser.parse(" 0 "))
        self.assertTupleEqual((True, False), parser.parse("false "))
        self.assertTupleEqual((True, False), parser.parse(" False "))

    def test_parse_invalid_string(self):
        parser = IntInputParser()
        success, error = parser.parse("invalid_number")
        self.assertFalse(success)
        self.assertIn("Could not convert", error)

