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

    def show_tip(self, *args):
        if self._tip_window:
            return
        x, y, cx, cy = self._widget.bbox("insert")
        x = x + self._widget.winfo_rootx() + 57
        y = y + cy + self._widget.winfo_rooty() + 27
        self._tip_window = tk.Toplevel(self._widget)
        self._tip_window.wm_overrideredirect(1)
        self._tip_window.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            self._tip_window,
            text=self._text,
            justify=tk.LEFT,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            font=("tahoma", "8", "normal"),
        )
        label.pack(ipadx=1)

    def hide_tip(self, *args):
        if self._tip_window:
            self._tip_window.destroy()
        self._tip_window = None

    @staticmethod
    def add_tool_tip(widget, description):
        tool_tip = ToolTip(widget, description)
        widget.bind("<Enter>", tool_tip.show_tip)
        widget.bind("<Leave>", tool_tip.hide_tip)

        return tool_tip
