import logging.config

logging.config.fileConfig('logging.conf')

    
def get_logger(log='rhum'):
    return logging.getLogger(log)