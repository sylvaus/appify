import copy
from argparse import ArgumentParser

from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.get_parameters import get_parameter_infos
from appify.common.input_parser.input_parser import IntInputParser, StrInputParser, FloatInputParser, BoolInputParser

DEFAULT_DOC_PARSER = RestructuredParser

DEFAULT_INPUT_PARSERS = {
    "int": IntInputParser,
    "str": StrInputParser,
    "float": FloatInputParser,
    "bool": BoolInputParser,
}


class Clifier(object):
    def __init__(self, func, doc_parser=None, input_parsers=None):
        self._func = func
        self._doc_parser = doc_parser if doc_parser else DEFAULT_DOC_PARSER
        self._input_parsers = input_parsers if input_parsers else copy.deepcopy(DEFAULT_INPUT_PARSERS)

    def run(self, description=None, version=None):
        parameter_infos = get_parameter_infos(self._func)

        if description:
            argparser = ArgumentParser(description=description)
        else:
            argparser = ArgumentParser()

        if version:
            argparser.add_argument('--version', action='version', version='%(prog)s ' + version)

        for _, parameter_info in parameter_infos.items():
            if parameter_info.required:
                help_ = "Required " + parameter_info.description
            else:
                help_ = parameter_info.description + ' (default: %(default)s)'

            argparser.add_argument(
                "--{}".format(parameter_info.name), default=parameter_info.default,
                required=parameter_info.required, help=help_
            )

        arguments = argparser.parse_args()
        params = [arguments.__dict__[name] for name in parameter_infos.keys()]
        
        self._func(*params)
