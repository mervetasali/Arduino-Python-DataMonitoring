
import serial

#Create a new serial port 
def openSerialPort(fdevice, fport, fbaud, ftimeout):

    fdevice = serial.Serial(
        port=fport,
        baudrate=fbaud,
        timeout=ftimeout
    )

    return fdevice

def readFromArduino(fdevice):
    
    incomingData = fdevice.readline().decode().strip()

    return incomingData

def writeToArduino():
    pass

