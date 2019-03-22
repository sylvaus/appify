"""
This module provides the abstract class for the docstring parser to
get the type and description of the parameters
"""
from abc import ABCMeta, abstractmethod


class DocParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, docstring):
        """
        Parse the given docstring and returns a dictionary of ParameterInfos
        with the name as a key with the information parsed
        :param docstring: given docstring
        :return: dictionary of ParameterInfos
        with the name as a key with the information parsed
        """
        pass
