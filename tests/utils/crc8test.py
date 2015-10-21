from rhum.utils.crc8 import CRC8Utils


print(CRC8Utils.check('test', 0xb9));
print(CRC8Utils.check('test', 0xb5));