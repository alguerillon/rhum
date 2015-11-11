import serial, struct, traceback, sys
from rhum.rhumlogging import get_logger

from rhum.drivers.driver import Driver
from rhum.drivers.enocean.messages.message import EnOceanMessage
from rhum.drivers.enocean.messages.response.VersionMessage import VersionMessage

from rhum.drivers.enocean.constants import PacketType, CommonCommandType, ResponseType
from rhum.utils.crc8 import CRC8Utils

import logging
from rhum.drivers.enocean.messages.typingmessage import TypingMessage

class EnOceanDriver(Driver):
    
    _logger = get_logger('rhum.driver.enocean.EnOceanDriver')
    
    def __init__(self, port='/dev/ttyAMA0', callback=None):
        super(EnOceanDriver, self).__init__(callback)
        # Initialize serial port
        self.__buffer = []
        self.__port = port
        self._logger.debug('initialize connection to '.format(port))
        self.__connection = serial.Serial(self.__port, 57600, timeout=0)
        
    def stop(self):
        Driver.stop(self)
        self.__connection.close()
        self._logger.info('EnOcean Driver on {0} stopped'.format(self.__port))
        
    def run(self):
        self._logger.info('EnOcean Driver started on {0}'.format(self.__port))
        while not self._stop.is_set():
            # Read chars from serial port as hex numbers
            try:
                msg = self.parse()
                __type, __datas, __opts = msg._get()
                
                msg = TypingMessage.transform(__type, __datas, __opts)
                
                self._logger.info(msg)
            except serial.SerialException:
                self._logger.error('Serial port exception! (device disconnected or multiple access on port?)')
                break
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                for line in lines:
                    self._logger.error(line)
            
        
    def test(self):
        msg = EnOceanMessage(PacketType.COMMON_COMMAND.value, [CommonCommandType.CD_R_VERSION.value])
        buffer = msg.build()
        self._logger.debug('EnOcean Driver message {0}'.format(buffer))
        self._logger.debug(self.__connection.isOpen())
        
        #for index in range(len(buffer)):
            #byte by byte tx
        buffer = bytes(buffer)
        self._logger.debug('writing byte {0}'.format(buffer))
        self.__connection.write(buffer)
            
        try:
            self._logger.debug('ask for parsing data')
            msg = self.parse()
            msg = VersionMessage(msg._get()[0], msg._get()[1], msg._get()[2])
            self._logger.info('EnOcean Test Message (Version)')
            self._logger.info(msg)
            
            if msg.isResponse() and msg.getReturnCode() == ResponseType.RET_OK:
                return True
            
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            for line in lines:
                self._logger.error(line)
        
        self.__connection.close()
        return False
    
    def parse(self):
        Driver.parse(self)
        self._logger.debug('parsing data')
        msg = self._getSerialData()
        
        if isinstance(msg, EnOceanMessage):
            return msg
        
        raise Exception('No message parsed')
        
 
    def _getSerialData(self):
        
        self._logger.debug('searching for sync byte') 
        s = 0
        while s != b'\x55':
            if self.__connection.inWaiting() != 0:
                s = self.__connection.read(1)
     
        self._logger.debug('sync byte found')
        while self.__connection.inWaiting() < 5:  
            ()
            
        header = self.__connection.read(4) #read header fields
        headerCRC = self.__connection.read(1)[0] #read header crc field
        
        self._logger.debug('header reading : {0} and crc : {1}'.format(header, headerCRC))
         
 
        if (CRC8Utils.calc(header) == headerCRC):
            
            self._logger.debug('header CRC OK')
            data_length, opt_length, msgType = struct.unpack("!HBB", header)
            
            self._logger.debug('data_length {0}; opt_length {1}; msg_type {2}'.format( data_length, opt_length, msgType ))    
            totalDataLength = data_length + opt_length

            while self.__connection.inWaiting() < totalDataLength+1:  
                ()
            
            datas = self.__connection.read(data_length)                
            opts = self.__connection.read(opt_length)
            dataCRC = self.__connection.read(1)
            
            self._logger.debug('datas {0}; opts {1}; dataCRC {2}'.format( datas, opts, dataCRC ))
            
            if(self._logger.isEnabledFor(logging.DEBUG)):
                msg = header
                msg += bytes({headerCRC})
                msg += datas
                msg += opts
                msg += dataCRC
                self._logger.debug(msg) 
            
                
            if (CRC8Utils.calc(datas+opts) == dataCRC[0]): 
                return EnOceanMessage(msgType, datas, opts)    
            return "Data CRC Failed"
        return "Header CRC Failed"