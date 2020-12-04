import logging
from utils import singleton


@singleton.Singleton
class Logger():
    def __init__(self):
        self.logger = logging.getLogger('app')
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('log/app.log')
        self.fh.setLevel(logging.DEBUG)
        # self.logger.addHandler(self.fh)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

    def appdebug(self, message):
        self.logger.debug(message)

    def appinfo(self, message):
        self.logger.info(message)
