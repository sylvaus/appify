import pytest

from appify.common.input_parser.input_parser import IntInputParser, BoolInputParser, InvalidArgumentFormat


def test_parse_bool():
    parser = BoolInputParser()
    assert parser.parse("true") == True
    assert parser.parse(" 1") == True
    assert parser.parse(" True ") == True
    assert parser.parse(" 0 ") == False
    assert parser.parse("false ") == False
    assert parser.parse(" False ") == False


def test_parse_invalid_string():
    parser = IntInputParser()
    with pytest.raises(InvalidArgumentFormat):
        parser.parse("invalid_number")
