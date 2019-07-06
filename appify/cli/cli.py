from __future__ import print_function

import copy
from argparse import ArgumentParser, ArgumentTypeError

from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.get_parameters import get_parameter_infos
from appify.common.input_parser.input_parser import IntInputParser, StrInputParser, FloatInputParser, BoolInputParser
from appify.common.parameter_info import NoDefault
from appify.common.parameter_parsing_exception import ParameterParsingException

DEFAULT_DOC_PARSER = RestructuredParser()

DEFAULT_INPUT_PARSERS = {
    "int": IntInputParser,
    "str": StrInputParser,
    "float": FloatInputParser,
    "bool": BoolInputParser,
}


def make_argument_parser(parser):
    """
    Make an argument parser for the ArgumentParser from an InputParser
    :param parser:
        Parser to decorate for the ArgumentParser
    :type parser: InputParser
    :return: Function that will raise ArgumentTypeError if the str argument cannot be parsed
    """

    def parse(text):
        success, result = parser.parse(text)
        if not success:
            raise ArgumentTypeError(result)

        return result

    return parse


class Clifier(object):
    def __init__(self, func, description=None, version=None, doc_parser=None, input_parsers=None):
        self._func = func
        self._description = description
        self._version = version if version else ""
        self._doc_parser = doc_parser if doc_parser else DEFAULT_DOC_PARSER
        self._input_parsers = input_parsers if input_parsers else copy.deepcopy(DEFAULT_INPUT_PARSERS)

    def run(self):
        """
        Run the given function as a command line
        :return: True if the cli could be created otherwise False
        """
        try:
            parameter_infos = get_parameter_infos(self._func, self._doc_parser)
            arg_parser = self._create_arg_parser(parameter_infos)
        except (ParameterParsingException, InvalidArgument, UnknownTypeArgument) as e:
            print("Could not create a CLI from the function {0}:".format(self._func.__name__))
            print("Exception:\n{0}".format(e))
            return False

        arguments = arg_parser.parse_args()
        params = [arguments.__dict__[name] for name in parameter_infos.keys()]

        self._func(*params)
        return True

    def _create_arg_parser(self, parameter_infos):
        """
        Creates the argument parser based on the given parameter infos,
        description and version
        :param parameter_infos:
            ParameterInfos Dictionary
        :type parameter_infos: Dict[str, ParameterInfo]
        :return: ArgumentParser
        """
        if self._description:
            arg_parser = ArgumentParser(description=self._description)
        else:
            arg_parser = ArgumentParser()

        if self._version:
            arg_parser.add_argument('--version', action='version', version='%(prog)s ' + self._version)

        for name, parameter_info in parameter_infos.items():
            self._check_parameter_info(parameter_info)
            arg_name = "--{}".format(name)
            type_parser = self._input_parsers[parameter_info.type]()
            type_parse = make_argument_parser(type_parser)

            if parameter_info.required:
                help_ = "Required {0}, type {1}".format(parameter_info.description, type_parser.get_value_format())
                arg_parser.add_argument(arg_name, required=True, help=help_, type=type_parse)
            else:
                help_ = "{0}, type {1}, (default: %(default)s)" \
                    .format(parameter_info.description, type_parser.get_value_format())
                arg_parser.add_argument(
                    arg_name, default=parameter_info.default, required=False, help=help_, type=type_parse
                )

        return arg_parser

    def _check_parameter_info(self, parameter_info):
        """
        Check if the parameter info describe a valid parameter
        Checks are:
            - A parameter cannot be not required and without a default
            - A parameter should have a type
            - The type should be a know type, i.e, is a key of the input_parsers dictionary
        :param parameter_info:
            ParameterInfo to check
        :type parameter_info: ParameterInfo
        :raise: InvalidArgument if a check is false
        :return: None
        """
        if not parameter_info.required and parameter_info.default == NoDefault:
            raise InvalidArgument("Parameter {0} is not required but does not have a default value\n"
                                  "Either add a default value or make the parameter".format(parameter_info.name))

        if not parameter_info.type:
            raise InvalidArgument("Parameter {0} must have a type".format(parameter_info.name))

        if parameter_info.type not in self._input_parsers:
            raise InvalidArgument("Parameter {0} has an unknown type: {1}"
                                  .format(parameter_info.name, parameter_info.type))


class InvalidArgument(Exception):
    pass


class UnknownTypeArgument(Exception):
    pass
