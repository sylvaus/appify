from abc import abstractmethod

from appify.common.six_abc import ABC
from appify.exceptions import AppifyException
from appify.ui.tooltip import ToolTip

try:
    import Tkinter as tk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk
    from tkinter import filedialog


class InvalidArgumentFormat(AppifyException):
    def __init__(self, message, help_=None):
        super(InvalidArgumentFormat, self).__init__(message)
        self.help = help_ if help_ else message


class InputWidget(tk.Frame, ABC):
    @abstractmethod
    def was_set(self):
        """
        :return: if the input value has been set
        """
        pass

    @abstractmethod
    def set(self, value):
        """
        Set the value of the widget

        :param value: given docstring
        """
        pass

    @abstractmethod
    def get(self):
        """
        Get the value of the widget

        :return: value of the widget
        :raises InvalidInput: if no value could be retrieved
        """
        pass

    @classmethod
    def create(cls, master, name, initial_value="", description=""):
        return cls(master, name, initial_value=initial_value, description=description)


class BaseInputWidget(InputWidget):
    def __init__(self, master, name, initial_value="", description="", **kwargs):
        super(BaseInputWidget, self).__init__(master, **kwargs)
        self._name = name
        self._was_set = False
        self._var = tk.StringVar()
        self._var.set(initial_value)
        self._var.trace("w", self._changed)
        self._label = tk.Label(self, text=name)
        self._label.pack(side=tk.LEFT)
        self._entry = tk.Entry(self, textvariable=self._var)
        self._entry.pack(side=tk.LEFT)
        if description:
            self._description = ToolTip.add_tool_tip(self._label, description)

    def was_set(self):
        return self._was_set

    def set(self, value):
        self._var.set(value)

    def get(self):
        return self._var.get()

    def _changed(self, *_):
        self._was_set = True


StrInputWidget = BaseInputWidget


class FilePathInputWidget(InputWidget):
    def __init__(
        self,
        master,
        name,
        initial_value="",
        description="",
        dialog_options=None,
        **kwargs
    ):
        super(FilePathInputWidget, self).__init__(master, **kwargs)
        self._name = name
        self._dialog_options = dialog_options if dialog_options else {}
        self._was_set = False
        self._var = tk.StringVar()
        self._var.set(initial_value)
        self._var.trace("w", self._changed)
        self._label = tk.Label(self, text=name)
        self._label.pack()
        self._entry = tk.Entry(self, textvariable=self._var)
        self._entry.pack(side=tk.LEFT)
        self._browse_button = tk.Button(self, text="browse", command=self._select_path)
        self._browse_button.pack(side=tk.LEFT)
        if description:
            self._description = ToolTip.add_tool_tip(self._label, description)

    def was_set(self):
        return self._was_set

    def set(self, value):
        self._var.set(value)

    def get(self):
        return self._var.get()

    def _changed(self, *_):
        self._was_set = True

    def _select_path(self):
        path = filedialog.askopenfilename(
            title="Select {0}".format(self._name), **self._dialog_options
        )
        if path:
            self._was_set = True
            self._var.set(path)


class FolderPathInputWidget(FilePathInputWidget):
    def _select_path(self):
        path = filedialog.askdirectory(
            title="Select {0}".format(self._name), **self._dialog_options
        )
        if path:
            self._was_set = True
            self._var.set(path)


class IntInputWidget(BaseInputWidget):
    def __init__(self, master, name, initial_value=0, description="", **kwargs):
        super(IntInputWidget, self).__init__(
            master, name, initial_value=initial_value, description=description, **kwargs
        )

    def get(self):
        value_str = self._var.get()
        try:
            value = int(value_str)
        except (TypeError, ValueError):
            raise InvalidArgumentFormat(
                'Failed to convert value "{0}" to int for parameter "{1}"'.format(
                    value_str, self._name
                )
            )

        return value


class FloatInputWidget(BaseInputWidget):
    def __init__(self, master, name, initial_value=0.0, description="", **kwargs):
        super(FloatInputWidget, self).__init__(
            master, name, initial_value=initial_value, description=description, **kwargs
        )

    def get(self):
        value_str = self._var.get()
        try:
            value = float(value_str)
        except (TypeError, ValueError):
            raise InvalidArgumentFormat(
                'Failed to convert value "{0}" to float for parameter "{1}"'.format(
                    value_str, self._name
                )
            )

        return value


class BoolInputWidget(InputWidget):
    def __init__(self, master, name, initial_value=False, description="", **kwargs):
        super(BoolInputWidget, self).__init__(self, master, **kwargs)
        self._name = name
        self._was_set = False
        self._var = tk.IntVar()
        self._var.set(initial_value)
        self._var.trace("w", self._changed)
        self._label = tk.Label(text=name)
        self._label.pack(side=tk.LEFT)
        self._entry = tk.Checkbutton(self, variable=self._var)
        self._entry.pack(side=tk.LEFT)
        if description:
            self._description = ToolTip.add_tool_tip(self._label, description)

    def _changed(self, *_):
        self._was_set = True

    def was_set(self):
        return self._was_set

    def set(self, value):
        self._var.set(value)

    def get(self):
        return self._var.get() == 1
