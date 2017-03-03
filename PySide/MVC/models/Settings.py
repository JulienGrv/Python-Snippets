"""Created on 13.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import logging
import os.path
import configparser

# Import Modules for Test Environment Support
# ===========================================
from testenvironment.client.cfg import constants

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class Settings(object):

    # Properties

    @property
    def swbox_type(self):
        return self.__swbox_type

    @swbox_type.setter
    def swbox_type(self, value):
        if value in constants.SWITCH_BOX_TYPES:
            self.__swbox_type = value

    def __init__(self, config_file=None):
        self.__swbox_type = None
        self.config_file = config_file if config_file else 'TestEnvironment.cfg'
        self.config = None
        if os.path.isfile(self.config_file):
            self.__load_config(self.config_file)

    def __load_config(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        LOG.debug('File %s loaded', config_file)
