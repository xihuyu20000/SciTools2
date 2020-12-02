import sys
from collections import defaultdict

from api.util.utils import Logger
from api import dao, config



class WordCloudManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao



wordCloudManager = WordCloudManager()