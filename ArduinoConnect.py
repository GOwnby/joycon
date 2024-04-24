import serial.tools.list_ports

# Define a function to determine which COM port the Arduino is connected to
def findArduino():
    ports = serial.tools.list_ports.comports()

    commPort = 'None'
    numConnection = len(ports)

    for i in range(0, numConnection):
        port = ports[i]
        strPort = str(port)

        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])

    # Create a Serial instance using the COM port found above
    if commPort != 'None': 
        serialInst = serial.Serial(commPort, baudrate=38400, timeout = 1)
        print('Connected to ' + commPort)
    else:
        print('Connection Issue!')
    
    return serialInst