"""Created on 13.02.2017.

@author: gra8hi
"""
# Import Standard Python Modules
# ==============================
import ConfigParser
import logging
import os

# Import Modules for Test Environment Support
# ===========================================

# Import Python Extensions
# ========================

# Define Module Logger
# ====================
LOG = logging.getLogger(__name__)

# Define Module Constants
# =======================


class TestEnvironment(object):
    def __init__(self, config_file=None):
        self.config_file = config_file if config_file else 'TestEnvironment.cfg'
        self.config = None
        if os.path.isfile(self.config_file):
            self.__load_config(self.config_file)

    def __load_config(self, config_file):
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)
        LOG.debug('File %s loaded', config_file)
