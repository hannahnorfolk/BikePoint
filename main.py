from datetime import datetime

from Modules.log_initialise import setup_logging

logger = setup_logging('log', timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
logger.info('Logger successfully initialised.')