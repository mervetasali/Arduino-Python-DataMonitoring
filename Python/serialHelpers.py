
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

    

def readFromArduino(fdevice):
    
    try:

        incomingData = fdevice.readline().decode().strip()

        return incomingData
    except Exception:
        print("Communication lost! Please check the USB cable and serial connection.")

        return None
    
    except KeyboardInterrupt:
        raise



def writeToArduino():
    pass

