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


class Guifier(object):
    def __init__(
        self,
        func,
        description=None,
        version=None,
        doc_parser=None,
        type_widget_map=None,
        name_widget_map=None,
        exit_on_success=False,
        success_message=None,
        success_callback=None,
        error_message=None,
        error_callback=None,
    ):
        self._func = ...
        self._description = ...
        self._version = ...
        self._result = ...
        self._exit_on_success = ...
        self._success_message = ...
        self._success_callback = ...
        self._error_message = ...
        self._error_callback = ...
        self._parameter_infos = ...
        self._name_widget_map = ...

    def get_all_input_frame(self, master, **kwargs):
        ...

    def run(self):
        ...

    def _run_function(self, input_frame, root):
        ...

    def _get_name_input_widgets(self, type_widget_map, name_widget_map):
        ...

    def _create_all_input_frame(self, master: tk.Widget, **kwargs):
        ...

    @staticmethod
    def _display_error_missing_inputs(inputs):
        ...

    def _display_error_exception(self, e):
        ...

    def _display_success(self, result):
        ...