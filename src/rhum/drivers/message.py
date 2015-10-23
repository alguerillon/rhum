import logging
from rhum.rhumlogging import init_logging

class Message:
    
    _logger = init_logging(logging.DEBUG, 'rhum.drivers.Packet')
    
    def __init__(self):
        self.message = 'test'
        
    def build(self):
        return True