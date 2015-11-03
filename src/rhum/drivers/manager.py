from rhum.rhumlogging import get_logger
from threading import Thread, Event
from rhum.drivers.enocean.driver import EnOceanDriver
import time, os

class DriverManager(Thread):
    
    ''' Driver Manager Class used to initiate the drivers '''
    _logger = get_logger('rhum.drivers.DriverManager')
    
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
        path = os.listdir(path='/dev/')
        tty = []
        for file in path:
            if file.find('AMA') != -1:
                tty.append(file)
            elif file.find('USB') != -1:
                tty.append(file)

        self._logger.debug('List tty')
        self._logger.debug(len(tty))
        
        '''test each tty port to connect with each driver'''
        for port_path in tty:
            path = '/dev/{0}'.format(port_path)
            self._logger.debug('test EnOcean Driver for {0}'.format(path))
            drive = EnOceanDriver(path)
            if drive.test():
                self._logger.info('EnOcean Driver selected for {0}'.format(path))
                self.__drivers.append(drive)
                continue
            
            self._logger.info('No Driver selected for {0}'.format(path))
        
        return True