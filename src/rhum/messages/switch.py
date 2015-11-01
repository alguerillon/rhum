from rhum.messages.item import Item, ItemType

class Switch(Item):
    
    def __init__(self, itemId, itemValue=None):
        super(Switch, ItemType.SWITCH, itemId, itemValue )