from abc import ABCMeta, abstractmethod
from typing import Any

from appify.exceptions import AppifyException


class InvalidArgumentFormat(AppifyException):
    pass


class InputParser(object):
    __metaclass__ = ABCMeta

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
