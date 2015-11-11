from rhum.rhumlogging import get_logger
from rhum.drivers.enocean.messages.responsemessage import ResponseMessage
from rhum.drivers.enocean.messages.radioerp1message import RadioERP1Message
from rhum.drivers.enocean.messages.message import EnOceanMessage
from rhum.drivers.enocean.constants import RadioERP1Type, PacketType
from rhum.drivers.enocean.messages.radiorep1.rps import RPSMessage

class TypingMessage:
    
    _logger = get_logger('rhum.drivers.enocean.messages.TypingMessage')
    
    @classmethod
    def transform(cls, _type, _datas, _opts):
        
        msg = None
        if (PacketType(_type) == PacketType.RESPONSE):
            cls._logger.debug('receiving Response')
            msg = ResponseMessage(_type, _datas, _opts)
        elif (PacketType(_type) == PacketType.RADIO_ERP1):
            cls._logger.debug('receiving Radio ERP 1')
            msg = cls.__transformRadioERP1(_type, _datas, _opts)
        else:
            cls._logger.debug('receiving Unknow {0}'.format(PacketType(_type)))
            msg = EnOceanMessage(_type, _datas, _opts)
            
        return msg
    
    @classmethod
    def __transformRadioERP1(cls, _type, _datas, _opts):
        
        msg = RadioERP1Message(_type, _datas, _opts)
        if(RadioERP1Type.RPS == msg.getReturnType()):
            cls._logger.debug('receiving Radio ERP 1 : RPS')
            msg = RPSMessage(_type, _datas, _opts)
        else:
            cls._logger.debug('receiving Radio ERP 1 : {0}'.format(RadioERP1Type(_datas[0:1][0])))
            
        return msg