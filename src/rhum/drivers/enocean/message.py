import logging
from rhum.rhumlogging import init_logging
from rhum.drivers.message import Message

class EnOceanMessage(Message):
    
    _logger = init_logging(logging.DEBUG, 'rhum.drivers.enocean.EnOceanMessage')