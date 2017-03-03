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
from layouts.Ui_MainWindow import Ui_MainWindow
from SettingsWindow import SettingsWindow
from testenvironment.client.controllers.Event import Event
from testenvironment.client.patterns.observer.Notifiable import Notifiable
from Window import Window

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class MainWindow(Window, Notifiable):
    """
    classdocs
    """

    # @property
    # def screen(self):
    #     return self.centralWidget().currentWidget()

    # Properties for widget value
    @property
    def status_bar(self):
        return self.statusBar().currentMessage()

    @status_bar.setter
    def status_bar(self, value):
        self.statusBar().showMessage(value)

    # Properties for widget enabled state

    def __init__(self, app, controller=None):
        """
        Constructor
        """
        Window.__init__(self, Ui_MainWindow())
        Notifiable.__init__(self)
        self._application = app
        self._controller = controller
        self.__sub_windows = []
        # Subscribe to events of models
        self.subscribe_events()
        # Initialize UI
        self.init_ui()
        # Connect widget signals to controller
        self._ui.actionSettings.triggered.connect(
            self._controller.open_settings)

    def subscribe_events(self):
        """Subscribe to events of controllers."""
        self.subscribe(Event.OPEN_SETTINGS)

    def init_ui(self):
        self._controller.init_testenvironment()

    def _handle_notification(self, notification):
        """Handle notification for model events sends from controllers.

        @type: object
        @param notification: notification sends from a notifier
        """
        LOG.debug('Notification received with name %s and body %s',
                  notification.name, notification.body)
        if notification.name == Event.OPEN_SETTINGS:
            self.__on_open_settings(notification.body)

    def __on_open_settings(self, controller):
        self.open_sub_window(SettingsWindow(controller), True)

    def open_sub_window(self, window, modality=False):
        """Open a new window attached to this MainWindow.

        This method is usually to open a temporary QDialog-like window.
        To open a new independent MainWindow attached to the application,
        it is recommended to use the open_window method of the App class.

        @type: QWidget
        @param window: window to be opened
        @type: bool
        @param modality: block all the others windows from input if True
        """
        self.__sub_windows.append(window)
        if modality:
            window.setWindowModality(QtCore.Qt.ApplicationModal)
        window.show()
