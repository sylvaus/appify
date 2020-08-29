from appify.cli.inputs import StrInputParser


def test_parse_nominal_case():
    parser = StrInputParser()
    assert parser.parse("a bit useless") == "a bit useless"
