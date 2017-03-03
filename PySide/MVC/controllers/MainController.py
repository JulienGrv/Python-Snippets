"""Created on 13.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from testenvironment.client.controllers.Event import Event
from testenvironment.client.controllers.SettingsController import \
    SettingsController
from testenvironment.client.models.Settings import Settings
from testenvironment.client.patterns.observer.Notifier import Notifier

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class MainController(Notifier):
    def __init__(self, testenvironment):
        Notifier.__init__(self)
        self.testenvironment = testenvironment

    def init_testenvironment(self):
        if self.testenvironment.config:
            # self._send_notification(Event.INIT_TESTENVIRONMENT, None)
            # TODO Load test Environment
            pass
        else:
            self._send_notification(Event.OPEN_SETTINGS, SettingsController())

    def open_settings(self):
        LOG.debug('open_settings called')
        self._send_notification(
            Event.OPEN_SETTINGS,
            SettingsController(Settings(self.testenvironment.config)))
