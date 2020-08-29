from typing import Union, Dict, Tuple, List, Any

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from appify.common.parameter_info import ParameterInfo
from appify.ui.inputs import InputWidget


class Inputs:
    def __init__(self, args: List[Any], kwargs: Dict[str, Any], missings: List[str], errors: Dict[str, str]):
        self.args = args
        self.kwargs = kwargs
        self.missings = missings
        self.errors = errors


class AllInputsFrame(tk.Frame):
    def __init__(
            self, master: Union[tk.Widget, tk.Tk]
            , parameter_infos: Dict[str, ParameterInfo]
            , name_widget_map: Dict[str, InputWidget]
            , **kwargs
    ) -> None:
        tk.Frame.__init__(self, master, **kwargs)
        self._default_map: Dict[str, Any]
        self._name_widget_map: Dict[str, InputWidget]

    def get_parameters(self) -> Tuple[List[Any], Dict[str, Any], List[Any]]:
        ...
