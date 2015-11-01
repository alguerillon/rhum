from rhum.rhumlogging import get_logger

########################
# class used to encode a string, an int or a bytearray in CRC8
########################
# This class does not need to be instantiated.
# CRC8.calc([0xb0, 0xae]) : will return the CRC8 corresponding
# CRC8.check('test', 0xb5) : will return True if the CRC8 is equal to 0xb5
########################
class _CRC8:
    
    _logger = get_logger('rhum.utils.crc8')

    # CRC8 encode table will keep the calculated CRC8 of each byte to prevent multi calculation
    _crc8Encode = [
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
    def _calculCRC8(self,byte):
        self._logger.debug('no value in table for {0}'.format(byte))
        crc = byte;
        for j in range(0,8):
            self._logger.debug('run {0}'.format(j))
            crc = (crc << 1) ^ (0x07 if (crc & 0x80) else 0)
        self._crc8Encode[byte] = crc & 0xFF
        self._logger.debug('calculated value {0} for byte {1}'.format(self._crc8Encode[byte], byte))
    
    # #####
    # This method calculate the CRC8 of a byte array and return the result
    def calc(self, byte):
        crc = 0
        for c in byte:
            crcByte = crc & 0xFF ^ c & 0xFF
            if self._crc8Encode[crcByte] == -1:
                self._calculCRC8(crcByte)
            crc = self._crc8Encode[crcByte]
        self._logger.info('message : {0} ; crc : {1}'.format(byte, crc))
        return crc
    
    # #####
    # This method convert any type of message to a byte array and return the result of
    # CRC8.calc with this byte array
    def calcAllTypes(self,msg):
        byte = []
        
        if type(msg) is list:
            byte = bytearray(msg)
        elif type(msg) is int:
            byte = msg.to_bytes((msg.bit_length() + 7) // 8, "big")
        else:
            byte = bytearray(str(msg), 'utf-8')
        return self.calc(byte)
        
    # #####
    # This method calculate the CRC8 of the message and return the result of CRC(msg) = crc
    def check(self, msg, crc):
        self._logger.info('message to check : "{0}" against {1}'.format(msg, crc))
        test = self.calcAllTypes(msg)
        return (test == crc)

CRC8Utils = _CRC8()