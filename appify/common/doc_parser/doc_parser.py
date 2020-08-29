"""
This module provides the abstract class for the docstring parser to
get the type and description of the parameters
"""
from abc import abstractmethod

from appify.common.six_abc import ABC


class DocParser(ABC):
    @abstractmethod
    def parse(self, docstring):
        """
        Parse the given docstring and returns a dictionary of ParameterInfos
        with the name as a key with the information parsed
        :param docstring: given docstring
        :return: dictionary of ParameterInfos with the name as a key with the information parsed
        """
        pass
