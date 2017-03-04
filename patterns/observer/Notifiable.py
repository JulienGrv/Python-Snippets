# Import Standard Python Modules
# ==============================
import logging
from abc import abstractmethod

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


class Notifiable(object):
    def __init__(self):
        self._events = []

    def subscribe(self, event):
        if event not in self._events:
            signal(event).connect(self._handle_notification)
            self._events.append(event)

    def unsubscribe(self, event):
        if event in self._events:
            signal(event).disconnect(self._handle_notification)
            self._events.remove(event)

    def unsubscribe_all(self):
        for event in self._events:
            signal(event).disconnect(self._handle_notification)
        del self._events[:]

    @abstractmethod
    def _handle_notification(self, notification):
        raise NotImplementedError("This is an abstract method.")
