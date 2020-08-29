from abc import ABCMeta, abstractmethod
from typing import Any, Optional, Union

from appify.exceptions import AppifyException

try:
    import Tkinter as tk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk
    from tkinter import filedialog


class InvalidInput(AppifyException):
    def __init__(self, message: str, help_: Optional[str] = None):
        ...


class InputWidget(tk.Frame):
    __metaclass__ = ABCMeta

    @abstractmethod
    def was_set(self) -> bool:
        ...

    @abstractmethod
    def set(self, value: Any):
        ...

    @abstractmethod
    def get(self) -> Any:
        ...

    @classmethod
    def create(cls, master: tk.Widget, name: str, initial_value: str = "", description: str = "") -> InputWidget:
        return cls(master, name, initial_value=initial_value, description=description)


class BaseInputWidget(InputWidget):
    def __init__(self, master: tk.Widget, name: str, initial_value: str = "", description: str = "", **kwargs) -> None:
        super(BaseInputWidget, self).__init__(master, **kwargs)
        self._was_set: bool = ...
        self._var: tk.StringVar = ...

    def was_set(self) -> bool:
        ...

    def set(self, value: str):
        ...

    def get(self) -> str:
        ...

    def _changed(self, *args) -> None:
        ...


StrInputWidget = BaseInputWidget


class FilePathInputWidget(InputWidget):
    def __init__(
            self, master: tk.Widget, name: str, initial_value: str = "", description: str = ""
            , dialog_options=None, **kwargs
    ):
        super(FilePathInputWidget, self).__init__(master, **kwargs)
        self._was_set: bool = ...
        self._var: tk.StringVar = ...
        self._dialog_options: dict = ...

    def was_set(self) -> bool:
        ...

    def set(self, value: str):
        ...

    def get(self) -> str:
        ...

    def _changed(self, *args) -> None:
        ...

    def _select_path(self):
        ...


class FolderPathInputWidget(FilePathInputWidget):
    ...


class IntInputWidget(BaseInputWidget):
    def __init__(self, master, name, initial_value=0, description="", **kwargs):
        super(IntInputWidget, self).__init__(
            master, name, initial_value=initial_value, description=description, **kwargs
        )

    def was_set(self) -> bool:
        ...

    def set(self, value: Union[int, str]):
        ...

    def get(self) -> int:
        ...


class FloatInputWidget(BaseInputWidget):
    def __init__(self, master, name, initial_value=0.0, description="", **kwargs):
        super(FloatInputWidget, self).__init__(
            master, name, initial_value=initial_value, description=description, **kwargs
        )

    def was_set(self) -> bool:
        ...

    def set(self, value: Union[float, str]):
        ...

    def get(self) -> float:
        ...


class BoolInputWidget(InputWidget):
    def __init__(self, master, name, initial_value=False, description="", **kwargs):
        super(BoolInputWidget, self).__init__(self, master, **kwargs)
        self._was_set: bool = ...
        self._var: tk.StringVar = ...

    def was_set(self) -> bool:
        ...

    def set(self, value: bool):
        ...

    def get(self) -> bool:
        ...

    def _changed(self, *args) -> None:
        ...
