import logging

logger = logging.getLogger('my_logger')

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('my_app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s -  %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug('Debug message from my_logger')
logger.info('Info message from my_logger')
logger.warning('Warning message from my_logger')
logger.error('Error message from my_logger')
logger.critical('Error message from my_logger')