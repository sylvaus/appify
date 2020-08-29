import pytest

from appify.cli.inputs import IntInputParser, BoolInputParser, InvalidArgumentFormat


def test_parse_valid_bool():
    parser = BoolInputParser()
    assert parser.parse("true")
    assert parser.parse(" 1")
    assert parser.parse(" True ")
    assert not parser.parse(" 0 ")
    assert not parser.parse("false ")
    assert not parser.parse(" False ")


def test_parse_invalid_string():
    parser = IntInputParser()
    with pytest.raises(InvalidArgumentFormat):
        parser.parse("invalid_number")
