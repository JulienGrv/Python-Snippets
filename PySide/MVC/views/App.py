"""Created on 23.09.2016.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Python Extensions
# ========================
from PySide import QtCore, QtGui

# Import Modules for Test Environment Support
# ===========================================
from testenvironment.client.views.resources import qrc_resources
from testenvironment.client.views.windows.MainWindow import MainWindow

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class App(QtGui.QApplication):
    """
    classdocs
    """

    def __init__(self, controller, args):
        """
        Constructor
        """
        super(App, self).__init__(args)
        self.__windows = []
        self.__init_main_window(controller)

    def __init_main_window(self, controller):
        """Initialize the main window of the application.

        @type: User
        @param user: User object
        @type: UserController
        @param controller: UserController object
        """
        main_window = MainWindow(self, controller)
        self.open_window(main_window)

    def open_window(self, window, modality=False):
        """Open a new window attached to this application.

        @type: QWidget
        @param window: window to be opened
        @type: bool
        @param modality: block all the others windows from input if True
        """
        self.__windows.append(window)
        if modality:
            window.setWindowModality(QtCore.Qt.ApplicationModal)
        window.show()

    # def close_window(self, window):
    #     """Close an opened window.
    #
    #     @type: QWidget
    #     @param window: window to be closed
    #     """
    #     self.__windows.remove(window)
