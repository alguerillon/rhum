import threading
import logging
import queue
from rhum.rhumlogging import init_logging
from rhum.drivers.message import Message

class Driver(threading.Thread):
    
    ''' driver class not used directly to standardize any type of protocol '''
    _logger = init_logging(logging.DEBUG, 'rhum.drivers.Driver')
    
    def __init__(self, callback=None):
        super(Driver, self).__init__()
        # Create an event to stop the thread
        self._stop = threading.Event()
        
        # Setup messages queues
        self.transmit = queue.Queue()
        self.receive = queue.Queue()
        
        # Set the callback method
        self.__callback = callback
        
    def send(self, message):
        if not isinstance(message, Message):
            self._logger.error('Cannot send others objects than Message')
            return False
        self.transmit.put(message)
        return True

    def stop(self):
        self._stop.set()

    def parse(self):
        ''' Parses messages and puts them to receive queue '''
        # Loop while we get new messages
        while True:
            self._logger.debug('parse')