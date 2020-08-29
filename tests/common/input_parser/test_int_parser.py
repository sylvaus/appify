import pytest

from appify.cli.inputs import IntInputParser, InvalidArgumentFormat


def test_parse_decimal():
    parser = IntInputParser()
    assert parser.parse("1234789") == 1234789
    assert parser.parse("0") == 0
    assert parser.parse(" 978456 ") == 978456
    assert parser.parse(" -978456 ") == -978456


def test_parse_hexadecimal():
    parser = IntInputParser()
    assert parser.parse("0x1234789") == 0x1234789
    assert parser.parse("0x0") == 0x0
    assert parser.parse(" 0x978456 ") == 0x978456


def test_parse_binary():
    parser = IntInputParser()
    assert parser.parse("0b001101101011010") == 0b001101101011010
    assert parser.parse("0b0") == 0b0
    assert parser.parse(" 0b11111 ") == 0b11111


def test_parse_invalid_string():
    parser = IntInputParser()
    with pytest.raises(InvalidArgumentFormat):
        parser.parse("invalid_number")
