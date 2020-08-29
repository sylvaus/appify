from __future__ import print_function

import copy
from argparse import ArgumentParser, ArgumentTypeError

from appify.cli.inputs import IntInputParser, StrInputParser, FloatInputParser, BoolInputParser
from appify.common.checks import check_parameter_info
from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.exceptions import InvalidArgument
from appify.common.get_parameters import get_parameter_infos

DEFAULT_DOC_PARSER = RestructuredParser()

DEFAULT_INPUT_PARSERS = {
    "int": IntInputParser,
    "str": StrInputParser,
    "float": FloatInputParser,
    "bool": BoolInputParser,
}


class Clifier(object):
    def __init__(self, func, description=None, version=None, doc_parser=None, input_parsers=None):
        self._func = func
        description = description
        version = version if version else ""
        doc_parser = doc_parser if doc_parser else DEFAULT_DOC_PARSER
        input_parsers = input_parsers if input_parsers else copy.deepcopy(DEFAULT_INPUT_PARSERS)
        self._parameter_infos = get_parameter_infos(func, doc_parser)
        self._arg_parser = self._create_arg_parser(description, version, input_parsers)

    @property
    def arg_parser(self):
        return self._arg_parser

    def run(self):
        """
        Run the given function as a command line
        :return: True if the cli could be created otherwise False
        """

        arguments = self._arg_parser.parse_args()
        params = [getattr(arguments, name) for name in self._parameter_infos]

        return self._func(*params)

    def _create_arg_parser(self, description, version, input_parsers):
        """
        Creates the argument parser based on the given parameter infos,
        description and version

        :param description: Description of the function
        :param version: version of the function
        :param input_parsers: Input Parsers to use
        :return: ArgumentParser
        """
        arg_parser = ArgumentParser(description=description)

        if version:
            arg_parser.add_argument('--version', action='version', version='%(prog)s ' + version)

        for name, parameter_info in self._parameter_infos.items():
            check_parameter_info(parameter_info)
            arg_name = "--{}".format(name)
            if parameter_info.type not in input_parsers.keys():
                raise InvalidArgument(
                    "Parameter {0} has an unknown type: {1}".format(parameter_info.name, parameter_info.type)
                )
            type_parser = input_parsers[parameter_info.type]()
            type_parse_func = _make_argument_parser(type_parser)

            if parameter_info.required:
                help_ = "Required {0}, type {1}".format(parameter_info.description, type_parser.value_format)
                arg_parser.add_argument(arg_name, required=True, help=help_, type=type_parse_func)
            else:
                help_ = "{0}, type {1}, (default: %(default)s)" \
                    .format(parameter_info.description, type_parser.value_format)
                arg_parser.add_argument(
                    arg_name, default=parameter_info.default, required=False, help=help_, type=type_parse_func
                )

        return arg_parser


def _make_argument_parser(parser):
    """
    Make an argument parser for the ArgumentParser from an InputParser
    :param parser: Parser to decorate for the ArgumentParser
    :type parser: InputParser
    :return: Function that will raise ArgumentTypeError if the str argument cannot be parsed
    """

    def parse(text):
        success, result = parser.parse(text)
        if not success:
            raise ArgumentTypeError(result)

        return result

    return parse
