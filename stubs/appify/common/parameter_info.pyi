from typing import Any, Optional


class NoDefaultType(object):
    pass


NoDefault = NoDefaultType()

ParameterName = str
ParameterType = str


class ParameterInfo(object):
    def __init__(self, name, type_=None, default=NoDefault, description=None, required=False) -> None:
        self.name: ParameterName = ...
        self.type: ParameterType = ...
        self.default: Any() = ...
        self.description: Optional[str] = ...
        self.required: bool = ...

    def is_positional(self) -> bool:
        ...

    def is_keyword(self) -> bool:
        ...

    def update(self, other):
        ...
