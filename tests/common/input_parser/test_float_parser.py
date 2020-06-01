import pytest

from appify.common.input_parser.input_parser import FloatInputParser, IntInputParser, InvalidArgumentFormat


def test_parse_float():
    parser = FloatInputParser()
    assert parser.parse("0.4") == 0.4
    assert parser.parse("40") == 40
    assert parser.parse(" -12.5 ") == -12.5


def test_parse_invalid_string():
    parser = IntInputParser()
    with pytest.raises(InvalidArgumentFormat):
        parser.parse("invalid_number")
