# system
import os
import sys
import yaml
import asyncio
import traceback
from dotenv import load_dotenv

# configure release level
release_level = os.environ.get("RELEASE_LEVEL")

# logging
import logging
import logging.config

# colors
import coloredlogs

# logo
import neotermcolor as neo
from neotermcolor import cprint, set_style
from pyfiglet import Figlet

try:
    if release_level == "RELEASE":
        Client_Name = os.getenv("CLIENT_NAME")
        logo = Figlet(font="chunky")
        cprint(logo.renderText(Client_Name), color=208, attrs=["bold"])

except:
    pass

# configure logging
with open("./Utilities/log/configuration.yaml",  "r") as file:
    configuration = yaml.safe_load(file.read())
    logging.config.dictConfig(configuration)

class Logger:
    """
    Logger class.
    """

    def __init__(self, name):
        """
        Initialize a logger instance.
        """
        self.logger = logging.getLogger(name)
        
        # install colored log output for our logger instances
        coloredlogs.install(level="INFO", logger=self.logger)

        # install colored log output for external 'root' instances such as pycord
        coloredlogs.install(level=None)
        
    async def debug(self, message):
        """
        Log a debug message.
        """
        self.logger.debug(message)

    async def info(self, message):
        """
        Log an info message.
        """
        self.logger.info(message)

    async def warning(self, message):
        """
        Log a warning message.
        """
        self.logger.warning(message)

    async def error(self, message):
        """
        Log an error message.
        """
        self.logger.error(message)

    async def critical(self, message):
        """
        Log a critical message.
        """
        self.logger.critical(message)