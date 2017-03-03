"""Created on 10.11.2016.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Python Extensions
# ========================
from enum import Enum

# Import Modules for Test Environment Support
# ===========================================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class Event(Enum):
    """Enumeration of events for notifiers."""

    # MainController events
    INIT_TESTENVIRONMENT = 00
    OPEN_SETTINGS = 01

    # SettingsController events
    SWBOX_TYPE_SET = 10
