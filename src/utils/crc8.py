########################
# class used to encode a string, an int or a bytearray in CRC8
########################
# This class does not need to be instantiated.
# CRC8.calc([0xb0, 0xae]) : will return the CRC8 corresponding
# CRC8.check('test', 0xb5) : will return True if the CRC8 is equal to 0xb5
########################

class CRC8:

    # CRC8 encode table will keep the calculated CRC8 of each byte to prevent multi calculation
    crc8Encode = [
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1,
        ]
    
    # #####
    # Internal method used to calculate the CRC8 for one byte
    #  and keep it in the corresponding entry of "crc8Encode"
    # ex: calculCRC8(0) will keep 0x00 in crc8Encode[0]
    def _calculCRC8(byte):
        crc = byte;
        for j in range(0,8):
            crc = (crc << 1) ^ (0x07 if (crc & 0x80) else 0)
        CRC8.crc8Encode[byte] = crc & 0xFF
    
    # #####
    # This method calculate the CRC8 of a byte array and return the result
    def calc(bytes):
        crc = 0
        for c in bytes:
            crcByte = crc & 0xFF ^ c & 0xFF
            if CRC8.crc8Encode[crcByte] == -1:
                CRC8._calculCRC8(crcByte)
            crc = CRC8.crc8Encode[crcByte]
        return crc
    
    # #####
    # This method convert any type of message to a byte array and return the result of
    # CRC8.calc with this byte array
    def calcAllTypes(msg):
        bytes = []
        
        if type(msg) is list:
            bytes = bytearray(msg)
        elif type(msg) is int:
            bytes = msg.to_bytes((msg.bit_length() + 7) // 8, "big")
        else:
            bytes = bytearray(str(msg), 'utf-8')
        return CRC8.calc(bytes)
        
    # #####
    # This method calculate the CRC8 of the message and return the result of CRC(msg) = crc
    def check(msg, crc):
        test = CRC8.calcAllTypes(msg)
        return (test == crc)
