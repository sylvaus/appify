from abc import ABCMeta, abstractmethod
from typing import Dict

from appify.common.parameter_info import ParameterInfo, ParameterName


class DocParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, docstring) -> Dict[ParameterName, ParameterInfo]:
        ...
