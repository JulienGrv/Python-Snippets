"""Created on 07.10.2016.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging

# Import Modules for Test Environment Support
# ===========================================
from common.Singleton import Singleton
from testenvironment.client.controllers.MainController import MainController
from testenvironment.client.models.TestEnvironment import TestEnvironment
from testenvironment.client.views.App import App

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class Client(Singleton):
    """Client for the testenvironment."""

    # Class static members
    __start = False
    __app = None

    def __init__(self):
        """Constructor of a Client instance."""
        super(Client, self).__init__()

    @classmethod
    def start(cls, config_file=None, *args):
        """Start the Client."""
        if not cls.__start:
            cls.__start = True
            cls.__app = App(MainController(TestEnvironment(config_file)), args)
            return cls.__app.exec_()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    import sys
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        config_file = None
    client = Client()
    client.start(config_file)
