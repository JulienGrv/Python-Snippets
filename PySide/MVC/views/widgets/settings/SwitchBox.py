"""Created on 02.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from layouts.Ui_SwitchBoxWidget import Ui_switchBoxWidget
from testenvironment.client.cfg import constants
from testenvironment.client.patterns.observer.Notifiable import Notifiable
from testenvironment.client.views.widgets.Widget import Widget

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class SwitchBox(Widget, Notifiable):
    """
    classdocs
    """

    # Properties for widget value

    @property
    def type(self):
        return self._ui.typeComboBox.currentIndex()

    # Properties for widget enable state

    @property
    def portNo_enabled(self):
        return self._ui.portLineEdit.isEnabled()

    @portNo_enabled.setter
    def portNo_enabled(self, value):
        self._ui.portLineEdit.setEnabled(value)

    @property
    def ports_enabled(self):
        return self._ui.portsGroupBox.isEnabled()

    @ports_enabled.setter
    def ports_enabled(self, value):
        self._ui.portsGroupBox.setEnabled(value)

    @property
    def aliases_enabled(self):
        return self._ui.aliasesGroupBox.isEnabled()

    @aliases_enabled.setter
    def aliases_enabled(self, value):
        self._ui.aliasesGroupBox.setEnabled(value)

    def __init__(self, controller, parent=None):
        """Constructor."""
        Widget.__init__(self, Ui_switchBoxWidget(), parent)
        Notifiable.__init__(self)
        # Initialize controller
        self._controller = controller
        # Connect widget signals to controller or internal functions
        self._ui.typeComboBox.currentIndexChanged.connect(
            self._controller.set_swbox_type)
        self._ui.portLineEdit.textEdited.connect(
            self._controller.set_swbox_port_no)
        self._ui.port1LineEdit.textEdited.connect(
            self._controller.set_swbox_port_1)
        # self._ui.port2LineEdit.textEdited.connect(self._controller.set_port_2)
        # self._ui.port3LineEdit.textEdited.connect(self._controller.set_port_3)
        # self._ui.port4LineEdit.textEdited.connect(self._controller.set_port_4)
        # self._ui.port4LineEdit.textEdited.connect(self._controller.set_port_4)
        # self._ui.port4LineEdit.textEdited.connect(self._controller.set_port_4)
        # self._ui.port5LineEdit.textEdited.connect(self._controller.set_port_5)
        # self._ui.port6LineEdit.textEdited.connect(self._controller.set_port_6)
        # self._ui.port7LineEdit.textEdited.connect(self._controller.set_port_7)
        # self._ui.port8LineEdit.textEdited.connect(self._controller.set_port_8)

        # Subscribe to events of models
        self.subscribe_events()
        # Initialize UI
        self.init_ui()

    def init_ui(self):
        """Set initial state of widgets."""
        config = self._controller.get_settings()
        if config:
            # TODO Load current settings
            pass
        else:
            self._ui.typeComboBox.addItem('Select a device type')
            for variant in sorted(constants.SWITCH_BOX_TYPES, key=str.lower):
                self._ui.typeComboBox.addItem(variant)
            self.portNo_enabled = False
            self.ports_enabled = False
            self.aliases_enabled = False

    def subscribe_events(self):
        """Subscribe to events of models."""
        # self.subscribe(Event.USER_EMAIL_SET)
        pass

    def _handle_notification(self, notification):
        """Handle notification for model events sends from controllers.

        @type: object
        @param notification: notification sends from a notifier
        """
        LOG.debug('Notification received with name %s and body %s',
                  notification.name, notification.body)
        # if notification.name == Event.USER_EMAIL_SET:
        #     self.__on_email(notification.body)
