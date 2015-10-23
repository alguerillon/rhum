from rhum.rhumlogging import init_logging
from threading import Thread, Event
import logging
import time

class DriverManager(Thread):
    
    ''' Driver Manager Class used to initiate the drivers '''
    _logger = init_logging(logging.DEBUG, 'rhum.drivers.DriverManager')
    
    def __init__(self):
        super(DriverManager, self).__init__()
        # Create an event to stop the thread
        self.__stop = Event()
        self.__drivers = []
        
    def stop(self):
        self.__stop.set()
    
    ''' driver Manager run '''    
    def run(self):
        
        self._logger.info('initialize driver manager')
        
        #init the drivers searching
        self.__search_driver()
        
        #while runing pause the manager in waiting command
        while not self.__stop.is_set():
            time.sleep(1)
        
        self._logger.info('stopping drivers')
        for driver in self.__drivers:
            driver.stop()
    
    '''search and initiate driver manager'''
    def __search_driver(self):
        return True