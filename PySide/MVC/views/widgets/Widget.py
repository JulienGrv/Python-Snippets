"""Created on 02.02.2017.

@author: gra8hi
"""
from abc import abstractmethod

from PySide import QtGui


class Widget(QtGui.QWidget):
    def __init__(self, layout, parent=None):
        super(Widget, self).__init__(parent)
        self._ui = layout
        self._ui.setupUi(self)

    @abstractmethod
    def init_ui(self):
        """Set initial state of widgets."""
        raise NotImplementedError("This is an abstract class.")

    @staticmethod
    def _update_border_color(widget, condition):
        """Update border color of a widget.

        @type: UI element
        @param widget: element to update border color
        @type: bool
        @param boolean: green color if True, red if False
        """
        # TODO Use better way of changing border color
        if condition:
            widget.setStyleSheet("border:1px solid rgb(0, 255, 0);")
        else:
            widget.setStyleSheet("border:1px solid rgb(255, 0, 0);")

    def _update_status_bar(self, message):
        """Update status bar message of the window."""
        self.window().status_bar = message
