from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.message import EnOceanMessage
from rhum.drivers.enocean.constants import PacketType, ResponseType

class ResponseMessage(EnOceanMessage):
    
    _logger = get_logger('rhum.drivers.enocean.messages.ResponseMessage')
    
    
    def __init__(self, __type, __datas, __opts):
        super(ResponseMessage, self).__init__(__type, __datas, __opts)
        self.__returnCode = __datas[0:1][0]
        
    def isResponse(self):
        return (self._get()[0] == PacketType.RESPONSE.value)
    
    def getReturnCode(self):
        return ResponseType(self.__returnCode)
    
    def __str__(self):
        strMsg  = super(ResponseMessage, self).__str__()
        strMsg += "\nResponse Return Code : {0}".format(ResponseType(self.__returnCode))
        return strMsg
        
    