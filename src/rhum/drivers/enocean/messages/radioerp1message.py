from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.message import EnOceanMessage
from rhum.drivers.enocean.constants import PacketType, RadioERP1Type

class RadioERP1Message(EnOceanMessage):
    
    _logger = get_logger('rhum.drivers.enocean.messages.RadioERP1Message')
    
    
    def __init__(self, __type, __datas, __opts):
        self.__rorg = __datas[0:1][0]
        self.__subtelnum=None
        self.__destID=None
        self.__dBm=None
        self.__securityLevel=None
        
        if len(__opts) > 0:
            self.__subtelnum=__opts[0:1][0]
            self.__destID=''.join( [ "%02X " % x for x in __opts[1:5] ] ).strip()
            self.__dBm=''.join( [ "%02X " % x for x in __opts[5:6] ] ).strip()
            self.__securityLevel=''.join( [ "%02X " % x for x in __opts[6:] ] ).strip()
            
        super(RadioERP1Message, self).__init__(__type, __datas, __opts)
        
        
    def isRadioERP1(self):
        return (self._get()[0] == PacketType.RADIO_ERP1.value)
    
    def getReturnType(self):
        return RadioERP1Type(self.__rorg)
    
    def __str__(self):
        strMsg  = super(RadioERP1Message, self).__str__()
        strMsg += "\nR-ORG                : {0}".format(RadioERP1Type(self.__rorg))
        strMsg += "\nSubTelNum            : {0}".format(self.__subtelnum)
        strMsg += "\nDestination ID       : {0}".format(self.__destID)
        strMsg += "\ndBm                  : {0}".format(self.__dBm)
        strMsg += "\nSecurity Level       : {0}".format(self.__securityLevel)
        return strMsg
