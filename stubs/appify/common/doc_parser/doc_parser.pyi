from abc import abstractmethod
from typing import Dict

from appify.common.parameter_info import ParameterInfo, ParameterName
from appify.common.six_abc import ABC


class DocParser(ABC):

    @abstractmethod
    def parse(self, docstring) -> Dict[ParameterName, ParameterInfo]:
        ...
