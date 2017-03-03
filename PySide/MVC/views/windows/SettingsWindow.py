"""Created on 03.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from layouts.Ui_SettingsWindow import Ui_SettingsWindow
from testenvironment.client.controllers.Event import Event
from testenvironment.client.patterns.observer.Notifiable import Notifiable
from testenvironment.client.views.widgets.settings.SwitchBox import SwitchBox
from testenvironment.client.views.widgets.settings.USBMux import USBMux
from Window import Window

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class SettingsWindow(Window, Notifiable):
    """
    classdocs
    """

    def __init__(self, controller, parent=None):
        """
        Constructor
        """
        Window.__init__(self, Ui_SettingsWindow())
        Notifiable.__init__(self)
        self._controller = controller
        # Subscribe to events of models
        self.subscribe_events()
        # Initialize UI
        self.init_ui()

    def subscribe_events(self):
        """Subscribe to events of controllers."""
        self.subscribe(Event.SWBOX_TYPE_SET)

    def init_ui(self):
        self._ui.tabWidget.addTab(SwitchBox(self._controller), 'Switch Box')
        self._ui.tabWidget.addTab(USBMux(self._controller), 'USB Multiplexer')

    def _handle_notification(self, notification):
        """Handle notification for model events sends from controllers.

        @type: object
        @param notification: notification sends from a notifier
        """
        LOG.debug('Notification received with name %s and body %s',
                  notification.name, notification.body)
        if notification.name == Event.SWBOX_TYPE_SET:
            pass
            # self.__on_open_settings(notification.body)
