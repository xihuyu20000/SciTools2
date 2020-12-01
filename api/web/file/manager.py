import time

from api.util.utils import Logger
from api import dao


class FileManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao



fileManager = FileManager()