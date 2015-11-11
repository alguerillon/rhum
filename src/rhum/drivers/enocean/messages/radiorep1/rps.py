from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.radioerp1message import RadioERP1Message

class RPSMessage(RadioERP1Message):
    
    _logger = get_logger('rhum.drivers.enocean.messages.radioerp1.RPSMessage')
    
    def __init__(self, __type, __datas, __opts):
        super(RPSMessage, self).__init__(__type, __datas, __opts)
        self.__data=''.join( [ "%02X " % x for x in __datas[1:2] ] ).strip()
        self.__senderID=''.join( [ "%02X " % x for x in __datas[2:6] ] ).strip()
        self.__status=''.join( [ "%02X " % x for x in __datas[6:] ] ).strip()
        
    
    def __str__(self):
        strMsg  = super(RPSMessage, self).__str__()
        strMsg += "\nSender ID            : {0}".format(self.__senderID)
        strMsg += "\nStatus               : {0}".format(self.__status)
        strMsg += "\nData                 : {0}".format(self.__data)
        return strMsg