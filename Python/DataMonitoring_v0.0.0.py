# This programme watches the serial data came from Arduino through the serial communication

import serial 
import serialHelpers as sh
import config


#Create a new serial port
ArduinoNano = sh.openSerialPort(config.DEVICE_NAME, config.PORT, config.BAUDRATE, config.TIMEOUT)

while True:

    TempData = sh.readFromArduino(ArduinoNano)

    print(TempData)

