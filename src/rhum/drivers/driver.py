import threading
import queue
from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.message import EnOceanMessage

class Driver(threading.Thread):
    
    ''' driver class not used directly to standardize any type of protocol '''
    _logger = get_logger('rhum.drivers.Driver')
    
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
        if not isinstance(message, EnOceanMessage):
            self._logger.error('Cannot send others objects than Message')
            return False
        self.transmit.put(message)
        return True

    def stop(self):
        self._stop.set()
        
    def test(self):
        return True

    def parse(self):
        ''' Parses messages and puts them to receive queue '''
        #while True:
        #    self._logger.debug('parse')