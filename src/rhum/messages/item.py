from rhum.rhumlogging import get_logger

from enum import Enum

class ItemType(Enum):
    SWITCH=0x00
    PILOT_SWITCH=0x01
    
    TEMP_SENSOR=0x10
    SWITCH_SENSOR=0x11

class Item:
    '''Item representation of all type of items'''
    
    __logger = get_logger('rhum.messages.item.Item')
    
    __type = None
    __value = None
    __id = None

    def __init__(self, itemType, itemId, itemValue=None):
        self.__type = itemType
        self.__id = itemId
        self.__value = itemValue

class Message:
    
    def __init__(self):
        self.message = 'test'
        
    def build(self):
        return True