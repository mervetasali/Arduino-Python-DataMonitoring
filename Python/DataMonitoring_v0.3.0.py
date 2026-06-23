
# This programme watches the serial data came from Arduino through the serial communication

import serial 
import serialHelpers as sh
import config


#Create a new serial port
ArduinoNano = sh.openSerialPort(config.DEVICE_NAME, config.PORT, config.BAUDRATE, config.TIMEOUT)


try: #Read data through a loop
    while ArduinoNano is not None:

        TempData = sh.readFromArduino(ArduinoNano)

        if TempData == None : #if a connection error is occured, the program will be stopped
            break

        elif TempData == "": #if there is an empty value, the program will passed the value
            continue

        else:
            
            ParsedSensorData = sh.packetParsing(TempData)

            if ParsedSensorData[0] == False:
                SensorError = 4
                SensorWarning = 0
                StatusMessage = f"Error Code (E-{SensorError}): The incoming data is not valid!"

            elif ParsedSensorData[0] == True:
                ParsedSensorDataList = [ParsedSensorData[1], ParsedSensorData[2]]
                ValidatedSensorData = sh.validating_packet(ParsedSensorDataList, "TEMP", 10, 80)

                SensorError = ValidatedSensorData[0]
                SensorWarning = ValidatedSensorData[1]
                StatusMessage = ValidatedSensorData[2]

            if SensorError != 0:
                print(f"System status: Error, {StatusMessage}")

            elif SensorWarning != 0:
                print(f"System status: Warning, {StatusMessage}")
            
            else:
                print(f"System status: Running, {StatusMessage}")
            
except KeyboardInterrupt: #If the user wants to exit the programme, it will close the port

    print("Programme stopped by the user..")


finally:

    if ArduinoNano is not None:
        print("Program is closing..")
        ArduinoNano.close()
        print("The port is closed..")
        print("The programme is closed!")
    