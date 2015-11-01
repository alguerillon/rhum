import serial
from rhum.rhumlogging import get_logger

from rhum.drivers.driver import Driver
from rhum.drivers.enocean.message import EnOceanMessage
from rhum.drivers.enocean.constants import PacketType, CommonCommandType

class EnOceanDriver(Driver):
    
    _logger = get_logger('rhum.driver.enocean.EnOceanDriver')
    
    def __init__(self, port='/dev/ttyAMA0', callback=None):
        super(EnOceanDriver, self).__init__(callback)
        # Initialize serial port
        self.__buffer = []
        self.__port = port
        self.__connection = serial.Serial(self.__port, 57600, timeout=0.1)
        
    def run(self):
        self._logger.info('EnOcean Driver started on {0}'.format(self.__port))
        while not self._stop.is_set():
            # Read chars from serial port as hex numbers
            try:
                bytearray(self.__ser.read(16))
            except serial.SerialException:
                self._logger.error('Serial port exception! (device disconnected or multiple access on port?)')
                break
            self.parse()

        self.__ser.close()
        self._logger.info('EnOcean Driver on {0} stopped'.format(self.__port))
        
    def test(self):
        msg = EnOceanMessage(PacketType.COMMON_COMMAND, [CommonCommandType.CD_R_VERSION])
        buffer = msg.build()
        
        for index in range(len(buffer)):
            #byte by byte tx
            self.__connection.write(buffer[index])
        
        try:
            self.parse()
        except:
            return False
        
        return True