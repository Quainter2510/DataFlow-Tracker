import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
file_handler = TimedRotatingFileHandler('logs/log.log', when="midnight", interval=1, backupCount=3)
formater = logging.Formatter(fmt="%(levelname)s - %(asctime)s - %(name)s: %(message)s")
file_handler.setFormatter(formater)
logger.addHandler(file_handler)