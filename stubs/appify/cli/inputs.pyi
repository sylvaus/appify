from abc import abstractmethod
from typing import Any

from appify.common.six_abc import ABC
from appify.exceptions import AppifyException


class InvalidArgumentFormat(AppifyException):
    pass


class InputParser(ABC):

    @abstractmethod
    def parse(self, string) -> Any:
        ...

    @property
    @abstractmethod
    def value_format(self) -> str:
        ...


class StrInputParser(InputParser):
    @abstractmethod
    def parse(self, string) -> str:
        ...

    @property
    @abstractmethod
    def value_format(self) -> str:
        ...


class IntInputParser(InputParser):
    @abstractmethod
    def parse(self, string) -> int:
        ...

    @property
    @abstractmethod
    def value_format(self) -> str:
        ...


class FloatInputParser(InputParser):
    @abstractmethod
    def parse(self, string) -> float:
        ...

    @property
    @abstractmethod
    def value_format(self) -> str:
        ...


class BoolInputParser(InputParser):
    @abstractmethod
    def parse(self, string) -> bool:
        ...

    @property
    @abstractmethod
    def value_format(self) -> str:
        ...
