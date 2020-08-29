from abc import abstractmethod
from typing import Dict

from appify.common.abc import ABC
from appify.common.parameter_info import ParameterInfo, ParameterName


class DocParser(ABC):

    @abstractmethod
    def parse(self, docstring) -> Dict[ParameterName, ParameterInfo]:
        ...
