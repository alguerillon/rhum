from rhum.rhumlogging import get_logger
from rhum.utils.crc8 import CRC8Utils

class EnOceanMessage:
    
    _logger = get_logger('rhum.drivers.enocean.EnOceanMessage')
    __syncByte = 0x55
    
    def __init__(self, msgType=0xFF, datas=None, optDatas=None):
        #Message.__init__(self)
        self.__type=msgType
        self.__datas=[]
        self.__optDatas=[]
        
        if datas != None:
            self.__datas=datas
            
        if optDatas != None:
            self.__optDatas = optDatas
            
    def build(self):
        buffer=[]
        data_length = len(self.__data)
        opt_length = len(self.__optDatas)
        
        #sync byte
        buffer.append(self.__syncByte) # adding sync byte
        
        #header
        buffer.append((data_length >> 8) & 0xFF) #first byte length data
        buffer.append(data_length & 0xFF) #second byte length data
        buffer.append(opt_length & 0xFF) #optionnal data length
        buffer.append(self.__type & 0xFF) #packet type byte
        #CRC Header
        buffer.append(CRC8Utils.calc(buffer[1:5]))
        
        #data
        buffer.append(self.__datas)
        buffer.append(self.__optDatas)
        #CRC Data
        buffer.append(CRC8Utils.calc(buffer[6:]))
        
        return buffer
        
        