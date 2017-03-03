"""Created on 02.02.2017.

@author: gra8hi
"""
from abc import abstractmethod

from PySide import QtGui


class Window(QtGui.QMainWindow):
    def __init__(self, layout, parent=None):
        super(Window, self).__init__(parent)
        self._ui = layout
        self._ui.setupUi(self)

    @abstractmethod
    def init_ui(self):
        """Set initial state of window."""
        raise NotImplementedError("This is an abstract method.")
