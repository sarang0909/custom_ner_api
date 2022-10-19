"""
Utility module.

Contains methods and variables common to the code.
"""


import json
from pathlib import Path

from src.utility import constants

# Singleton class to read and hold config file
class _Config:
    __instance = None

    @staticmethod
    def get_instance():
        """Static Access Method

        Returns:
            _Config : config class instance
        """

        if _Config.__instance is None:
            _Config()
        return _Config.__instance

    def __init__(self):
        """Private constructor

        Raises:
            Exception: Raised when attempy made to initialise this singleton class.
        """

        if _Config.__instance is not None:
            raise Exception(
                "This class is a singleton class,you can not initialize it."
            )
        with open(
            Path(constants.CONFIG_FILE), "r+", encoding="UTF-8"
        ) as config_file:
            self.config = json.loads(config_file.read())
            _Config.__instance = self

    def get(self, name):
        """Returns config value when provided with config key.

        Args:
            name (str): Config property required

        Returns:
            str: Value of the config requested
        """

        return str(self.config[name])


# Config object can be accessed in other classes by _Config().get_instance static method or
# by importing below config object.
config = _Config.get_instance()
