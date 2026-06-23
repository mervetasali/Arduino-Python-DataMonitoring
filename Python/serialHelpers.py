
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

    if len(dataList) == 2:        
        fsensorName = dataList[0].strip()
        fsensorValue = dataList[1].strip()

        return True, fsensorName, fsensorValue
    else:
        fsensorName = ""
        fsensorValue = ""

        return False, fsensorName, fsensorValue
    

def validating_packet(fincomingDataList, tag, minVal, maxVal): #check the tag and the value of the incoming packet

    #if len(fincomingDataList) == 2:
    ftag = fincomingDataList[0].strip().lower()

    if ftag == tag.strip().lower():

        try: 
            fvalue = int(fincomingDataList[1])            
            ferrorCode = 0

            if fvalue < minVal:
                fwarningCode = 1                
                fresultMessage = f"Warning Code (W-{fwarningCode}): The sensor value is too low. Run the heater unit!"                
            
            elif fvalue > maxVal:
                fwarningCode = 2
                fresultMessage = f"Warning Code (W-{fwarningCode}): The sensor value is too high. Stop the heater unit!"

            else:
                fwarningCode = 0                    
                fresultMessage = f"Current {ftag.upper()} value = {fvalue}"

            return ferrorCode, fwarningCode, fresultMessage
        
        except ValueError:
            ferrorCode = 3
            fwarningCode = 0
            fresultMessage = f"Error Code (E-{ferrorCode}): The incoming data value is not valid!"
        
            return ferrorCode, fwarningCode, fresultMessage
        
    else:
        ferrorCode = 2
        fwarningCode = 0
        fresultMessage = f"Error Code (E-{ferrorCode}): The incoming data tag is not {tag.strip().upper()}!"
        
        return ferrorCode, fwarningCode, fresultMessage
    
    # else:
    #     ferrorCode = 1
    #     fwarningCode = 0
    #     fresultMessage = f"Error Code (E-{ferrorCode}): The incoming data lenght is wrong!"        

    #     return ferrorCode, fwarningCode, fresultMessage

    
    

def writeToArduino():
    pass

