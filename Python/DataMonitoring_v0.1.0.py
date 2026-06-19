
# This programme watches the serial data came from Arduino through the serial communication

import serial 
import serialHelpers as sh
import config


#Create a new serial port
ArduinoNano = sh.openSerialPort(config.DEVICE_NAME, config.PORT, config.BAUDRATE, config.TIMEOUT)


try: #Read data through a loop
    while ArduinoNano is not None:

        TempData = sh.readFromArduino(ArduinoNano)

        if TempData == None :
            break
        else:
            print(TempData)

except KeyboardInterrupt: #If the user wants to exit the programme, it will close the port

    print("Programme stopped by the user..")


finally:

    if ArduinoNano is not None:
        print("Program is closing..")
        ArduinoNano.close()
        print("The port is closed..")
        print("The programme is closed!")
    