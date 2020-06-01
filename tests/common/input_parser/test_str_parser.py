from appify.common.input_parser.input_parser import StrInputParser


def test_parse_nominal_case():
    parser = StrInputParser()
    assert parser.parse("a bit useless") == "a bit useless"
