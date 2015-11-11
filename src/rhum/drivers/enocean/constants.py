from enum import Enum

class PacketType(Enum):
    RESERVED=0x00
    RADIO_ERP1=0x01
    RESPONSE=0x02
    RADIO_SUB_TEL=0x03
    EVENT=0x04
    COMMON_COMMAND=0x05
    SMART_ACK_COMMAND=0x06
    REMOTE_MAN_COMMAND=0x07
    RESERVED_ENOCEAN=0x08
    RADIO_MESSAGE=0x09
    RADIO_ERP2=0x0a
    
class ResponseType(Enum):
    RET_OK=0x00
    RET_ERROR=0x01
    RET_NOT_SUPPORTED=0x02
    RET_WRONG_PARAM=0x03
    RET_OPERATION_DENIED=0x04
    
class RadioERP1Type(Enum):
    VLD=0xD2
    ADT=0xA6
    BS4=0xA5
    BS1=0xD5
    RPS=0xF6
    
class CommonCommandType(Enum):
    CD_R_VERSION=0x03