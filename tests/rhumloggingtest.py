import logging
from rhum.rhumlogging import init_logging

log = init_logging()
log.debug('debug')
log.info('info')
log.error('error')
log.critical('fatal')

log = init_logging(logging.CRITICAL, 'rhum-crit')
log.debug('debug')
log.info('info')
log.error('error')
log.critical('fatal')