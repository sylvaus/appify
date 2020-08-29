try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class ToolTip(object):
    def __init__(self, widget, text):
        self._widget = widget
        self._tip_window = None
        self._id = None
        self._text = text

    def show_tip(self, *args) -> None:
        ...

    def hide_tip(self, *args) -> None:
        ...

    @staticmethod
    def add_tool_tip(widget: tk.Widget, description: str) -> ToolTip:
        ...
