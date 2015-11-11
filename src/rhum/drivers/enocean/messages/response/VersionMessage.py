from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.responsemessage import ResponseMessage

class VersionMessage(ResponseMessage):
    
    _logger = get_logger('rhum.drivers.enocean.messages.VersionMessage')
    
    def __init__(self, __type, __datas, __opts):
        super(VersionMessage, self).__init__(__type, __datas, __opts)
        
        self.__appmain = __datas[1:2][0]
        self.__appbeta = __datas[2:3][0]
        self.__appalpha = __datas[3:4][0]
        self.__appbuild = __datas[4:5][0]
        
        self.__apimain = __datas[5:6][0]
        self.__apibeta = __datas[6:7][0]
        self.__apialpha = __datas[7:8][0]
        self.__apibuild = __datas[8:9][0]
        
        self.__chipid = ''.join( [ "%02X " % x for x in __datas[9:13] ] ).strip()
        self.__chipversion = ''.join( [ "%02X " % x for x in __datas[13:17] ] ).strip()
        self.__desc = __datas[17:-1].decode(encoding='ASCII').strip()
        
        
    
    def __str__(self):
        strMsg  = super(VersionMessage, self).__str__()
        strMsg += "\nApplication Version  : {0}.{1}.{2}.{3}".format(self.__appmain, self.__appbeta, self.__appalpha, self.__appbuild)
        strMsg += "\nAPI Version          : {0}.{1}.{2}.{3}".format(self.__apimain, self.__apibeta, self.__apialpha, self.__apibuild)
        strMsg += "\nChip ID              : {0}".format(self.__chipid)
        strMsg += "\nChip Version         : {0}".format(self.__chipversion)
        strMsg += "\nDescription          : {0}".format(self.__desc)
        return strMsg