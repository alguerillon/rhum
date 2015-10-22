import serial, logging
from rhum.rhumlogging import init_logging

from rhum.drivers.driver import Driver

class EnOceanDriver(Driver):
    
    _logger = init_logging(logging.DEBUG, 'rhum.driver.enocean.EnOceanDriver')
    
    def __init__(self, port='/dev/ttyAMA0', callback=None):
        super(EnOceanDriver, self).__init__(callback)
        # Initialize serial port
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