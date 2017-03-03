# Import Standard Python Modules
# ==============================
import logging

# Import Python Extensions
# ========================
from blinker import signal

# Import Modules for Test Environment Support
# ===========================================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class Notifier(object):
    def __init__(self):
        pass

    def _send_notification(self, event, body=None):
        signal(event).send(self.Notification(event, body))

    class Notification(object):
        def __init__(self, name, body=None):
            self.name = name
            self.body = body
