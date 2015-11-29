from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.radioerp1message import RadioERP1Message

class BS4Message(RadioERP1Message):
    
    _logger = get_logger('rhum.drivers.enocean.messages.radioerp1.BS1Message')
    
    def __init__(self, __type, __datas, __opts):
        super(BS4Message, self).__init__(__type, __datas, __opts)
        self.__senderID=''.join( [ "%02X " % x for x in __datas[5:9] ] ).strip()
        self.__status=''.join( [ "%02X " % x for x in __datas[9:] ] ).strip()
        self.__data3=''.join( [ "%02X " % x for x in __datas[1:2] ] ).strip()
        self.__data2=''.join( [ "%02X " % x for x in __datas[2:3] ] ).strip()
        self.__data1=''.join( [ "%02X " % x for x in __datas[3:4] ] ).strip()
        self.__data0=''.join( [ "%02X " % x for x in __datas[4:5] ] ).strip()
        
    
    def __str__(self):
        strMsg  = super(BS4Message, self).__str__()
        strMsg += "\nSender ID            : {0}".format(self.__senderID)
        strMsg += "\nStatus               : {0}".format(self.__status)
        strMsg += "\nData 0               : {0}".format(self.__data0)
        strMsg += "\nData 1               : {0}".format(self.__data1)
        strMsg += "\nData 2               : {0}".format(self.__data2)
        strMsg += "\nData 3               : {0}".format(self.__data3)
        return strMsg