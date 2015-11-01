import time

from rhum.utils.daemon import Daemon
from rhum.rhumlogging import get_logger

class RhumDaemon(Daemon):
    __logger = get_logger('rhum.RhumDaemon')
    
    def run(self):
        self.__load()
        while True:
            time.sleep(1)

    '''stop the daemon service'''        
    def stop(self):
        self.__unload()
        return Daemon.stop(self)
    
    '''reload service method for deamon'''
    def reload(self):
        self.__unload()
        self.__load()
    
    '''Load driver manager to search and initiate drivers'''
    def __load(self):
        self.__logger.debug('Loading service managers')
        return True
    
    '''unloading threads correctly corresponding to drivers'''
    def __unload(self):
        self.__logger.debug('Unloading service managers')
        return True