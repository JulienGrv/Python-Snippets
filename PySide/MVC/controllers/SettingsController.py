"""Created on 13.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from testenvironment.client.cfg import constants
from testenvironment.client.controllers.Event import Event
from testenvironment.client.models.Settings import Settings
from testenvironment.client.patterns.observer.Notifier import Notifier

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class SettingsController(Notifier):
    def __init__(self, settings=None):
        Notifier.__init__(self)
        self.settings = settings if settings else Settings()

    def get_settings(self):
        LOG.debug('get_settings called')
        return self.settings.config

    def set_swbox_type(self, index):
        LOG.debug('set_swbox_type called with arg value: %s', index)
        if index > 0:
            self.settings.swbox_type = sorted(
                constants.SWITCH_BOX_TYPES, key=str.lower)[index - 1]
        self._send_notification(Event.SWBOX_TYPE_SET, self.settings.swbox_type)

    def set_swbox_port_no(self, number):
        LOG.debug('set_swbox_port_no called with arg value: %s', number)

    def set_swbox_port_1(self, value):
        LOG.debug('set_swbox_port_1 called with arg value: %s', value)
