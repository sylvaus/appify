from collections import OrderedDict

try:
    import Tkinter as tk
    import tkMessageBox as messagebox
except ImportError:
    import tkinter as tk
    from tkinter import messagebox

from appify.common.checks import check_parameter_info
from appify.common.exceptions import InvalidArgument
from appify.common.get_parameters import get_parameter_infos
from appify.common.parameter_info import NoDefault
from appify.common.doc_parser.restructured_parser import RestructuredParser
from appify.ui.inputs import (
    StrInputWidget,
    BoolInputWidget,
    FloatInputWidget,
    IntInputWidget,
    InvalidInput,
)

DEFAULT_DOC_PARSER = RestructuredParser()

DEFAULT_TYPE_WIDGET_MAP = {
    "str": StrInputWidget,
    "int": IntInputWidget,
    "float": FloatInputWidget,
    "bool": BoolInputWidget,
}


class Inputs:
    def __init__(self, args, kwargs, missings, errors):
        self.args = args
        self.kwargs = kwargs
        self.missings = missings
        self.errors = errors

    def are_all_available(self):
        return not (self.missings or self.errors)


class AllInputsFrame(tk.Frame):
    def __init__(self, master, parameter_infos, name_widget_map, **kwargs):
        """
        :param parameter_infos: Name Parameter info dictionary
        :param name_widgets: Name Input Widget dictionary
        :param kwargs: Frame arguments
        """
        tk.Frame.__init__(self, master, **kwargs)
        self._default_map = {}
        self._name_widget_map = OrderedDict()
        for name, parameter_info in parameter_infos.items():
            widget = name_widget_map[name]
            if parameter_info.default != NoDefault:
                self._default_map[name] = parameter_info.default
                self._name_widget_map[name] = widget.create(
                    master,
                    name,
                    initial_value=parameter_info.default,
                    description=parameter_info.description,
                )
            else:
                self._name_widget_map[name] = widget.create(
                    master, name, description=parameter_info.description
                )

            self._name_widget_map[name].pack()

    def get_inputs(self):
        """
        Returns a tuple(args, kwargs, missings) where
            * args is the list of available positional arguments
            * kwargs is the dictionary of available keyword arguments
            * missings is the list of missing arguments

        :return: a tuple(args, kwargs, missings)
        """

        inputs = Inputs([], OrderedDict(), [], OrderedDict())
        for name, widget in self._name_widget_map.items():
            if not widget.was_set():
                self._handle_input_not_set(name, inputs)
            else:
                self._handle_input_set(name, widget, inputs)

        return inputs

    def _handle_input_not_set(self, name, inputs):
        if name in self._default_map:
            inputs.kwargs[name] = self._default_map[name]
        else:
            inputs.missings.append(name)

    def _handle_input_set(self, name, widget, inputs):
        try:
            value = widget.get()
        except InvalidInput as e:
            inputs.errors[name] = str(e)
            return

        if name in self._default_map:
            inputs.kwargs[name] = value
        else:
            inputs.args.append(value)


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
        self._func = func
        self._description = description
        self._version = version if version else ""
        if doc_parser is None:
            doc_parser = DEFAULT_DOC_PARSER
        if type_widget_map is None:
            type_widget_map = DEFAULT_TYPE_WIDGET_MAP
        if name_widget_map is None:
            name_widget_map = {}
        if success_message is None:
            success_message = "Successfully executed {0}".format(func.__name__)
        if success_callback is None:
            success_callback = self._display_success
        if error_message is None:
            error_message = "Error happened during execution {0}".format(func.__name__)
        if error_callback is None:
            error_callback = self._display_error_exception

        self._result = None
        self._exit_on_success = exit_on_success
        self._success_message = success_message
        self._success_callback = success_callback
        self._error_message = error_message
        self._error_callback = error_callback
        self._parameter_infos = get_parameter_infos(func, doc_parser)
        self._name_widget_map = self._get_name_input_widgets(
            type_widget_map, name_widget_map
        )

    def get_all_input_frame(self, master, **kwargs):
        return self._create_all_input_frame(master, **kwargs)

    def run(self):
        root = tk.Tk()
        input_frame = self.get_all_input_frame(root)
        input_frame.pack()

        button = tk.Button(
            root, text="run", command=lambda: self._run_function(input_frame, root)
        )
        button.pack()

        tk.mainloop()

        return self._result

    def _run_function(self, input_frame, root):
        inputs = input_frame.get_inputs()
        if not inputs.are_all_available():
            self._display_error_missing_inputs(inputs)
            return

        # noinspection PyBroadException
        # Any exception will be handled as an execution error
        try:
            self._result = self._func(*inputs.args, **inputs.kwargs)
        except Exception as e:
            self._error_callback(e)
        else:
            self._success_callback(self._result)
            if self._exit_on_success:
                root.destroy()

    def _get_name_input_widgets(self, type_widget_map, name_widget_map):
        name_input_widgets = OrderedDict()
        for name, parameter_info in self._parameter_infos.items():
            if parameter_info.name in name_widget_map:
                name_input_widgets[name] = name_widget_map[name]

            check_parameter_info(parameter_info)
            if parameter_info.type not in type_widget_map:
                raise InvalidArgument(
                    'Parameter {0} has a type ("{1}") which is not handled.'
                    "Either add a specific Input widget for the parameter "
                    "to name_widget_map or an Input Widget for the type in type_widget_map".format(
                        parameter_info.name, parameter_info.type
                    )
                )

            name_input_widgets[parameter_info.name] = type_widget_map[
                parameter_info.type
            ]

        return name_input_widgets

    def _create_all_input_frame(self, master: tk.Widget, **kwargs):
        return AllInputsFrame(
            master, self._parameter_infos, self._name_widget_map, **kwargs
        )

    @staticmethod
    def _display_error_missing_inputs(inputs):
        missing = "  - " + "\n  - ".join(inputs.missings)
        invalid = "  - " + "\n  - ".join(
            "{0}: {1}".format(name, error) for name, error in inputs.errors.items()
        )

        messagebox.showinfo(
            "Invalid Inputs",
            "Some values were missing or invalid."
            "\nMissing:\n{0}\nInvalid:\n{1}".format(missing, invalid),
        )

    def _display_error_exception(self, e):
        messagebox.showinfo("Error", "{0}. Error {1}:".format(self._error_message, e))

    def _display_success(self, result):
        messagebox.showinfo("Success", self._success_message)
