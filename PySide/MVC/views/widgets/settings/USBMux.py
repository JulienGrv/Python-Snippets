"""Created on 02.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from layouts.Ui_USBMuxWidget import Ui_USBMuxWidget
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


class USBMux(Widget, Notifiable):
    """
    classdocs
    """

    # Properties for widget value

    # @property
    # def portNo(self):
    #     return self._ui.portLineEdit.getText()

    # Properties for widget enable state

    @property
    def inputs_enabled(self):
        return self._ui.inputGroupBox.isEnabled()

    @inputs_enabled.setter
    def inputs_enabled(self, value):
        self._ui.inputGroupBox.setEnabled(value)

    @property
    def outputs_enabled(self):
        return self._ui.outputGroupBox.isEnabled()

    @outputs_enabled.setter
    def outputs_enabled(self, value):
        self._ui.outputGroupBox.setEnabled(value)

    @property
    def default_connection_enabled(self):
        return self._ui.defaultFrame.isEnabled()

    @default_connection_enabled.setter
    def default_connection_enabled(self, value):
        self._ui.defaultFrame.setEnabled(value)

    def __init__(self, controller, parent=None):
        """Constructor."""
        Widget.__init__(self, Ui_USBMuxWidget(), parent)
        Notifiable.__init__(self)
        # Initialize controller
        self._controller = controller
        # Connect widget signals to controller or internal functions
        # self._ui.emailLineEdit.textChanged.connect(self._controller.set_email)
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
            for variant in sorted(constants.USB_MUX_TYPES, key=str.lower):
                self._ui.typeComboBox.addItem(variant)
            self.inputs_enabled = False
            self.outputs_enabled = False
            self.default_connection_enabled = False

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
