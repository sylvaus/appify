from __future__ import print_function

from argparse import ArgumentParser
from typing import Callable, Dict, Any, Type

from appify.cli.inputs import IntInputParser
from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.common.parameter_info import ParameterType, ParameterInfo

DEFAULT_DOC_PARSER = RestructuredParser()

DEFAULT_INPUT_PARSERS: Dict[ParameterType, Type[IntInputParser]] = ...


class Clifier(object):
    def __init__(self, func, description=None, version=None, doc_parser=None, input_parsers=None):
        self._func: Callable = ...
        self._parameter_infos: Dict[ParameterType, ParameterInfo] = ...
        self._arg_parser: ArgumentParser = ...

    @property
    def arg_parser(self) -> ArgumentParser:
        ...

    def run(self) -> Any:
        """
        Run the given function as a command line
        :return: True if the cli could be created otherwise False
        """

        arguments = self._arg_parser.parse_args()
        params = [getattr(arguments, name) for name in self._parameter_infos]

        return self._func(*params)

    def _create_arg_parser(
            self, description: str, version: str, input_parsers: Dict[ParameterType, Type[IntInputParser]]
    ) -> ArgumentParser:
        ...


def _make_argument_parser(parser: IntInputParser) -> Callable[[str], Any]:
    ...
