
import serial

#Create a new serial port 
def openSerialPort(fdeviceName, fport, fbaud, ftimeout):

    try:

        device = serial.Serial(
            port=fport,
            baudrate=fbaud,
            timeout=ftimeout
        )

        return device
    
    except:
        print(f"Unable to connect to the {fdeviceName}.. \n Check the com-port settings and connection cable state!")

        return None

    
#Read data from the device with error handling
def readFromArduino(fdevice):
    
    try:

        incomingData = fdevice.readline().decode().strip()

        return incomingData
    except Exception:
        print("Communication lost! Please check the USB cable and serial connection.")

        return None
    
    except KeyboardInterrupt:
        raise


#Parse the incoming data
def packetParsing(fincomingData):
    
    dataList = fincomingData.split(":")
    fsensorName = dataList[0]
    fsensorValue = int(dataList[1]) #convert the string value to an integer value

    return fsensorName, fsensorValue



def writeToArduino():
    pass

