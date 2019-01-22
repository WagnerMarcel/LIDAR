import serial

class LIDAR:
    dist = 0
    i2c = None
    spi = None
    uart = '/dev/ttyAMA0'
    recievedData = False

    def __init__(self):
        self.ser = serial.Serial(self.uart, 115200, timeout=1)

    # Funktion um frische Daten vom LIDAR zu erhalten
    def getData(self):
        self.ser.reset_input_buffer()
#        print("flushed buffer")
        while(self.recievedData != True):
#            print("waiting for data")
            while(self.ser.in_waiting <= 9):
#                print("getting data")
                if((b'Y' == self.ser.read()) and (b'Y' == self.ser.read())):
#                    print("if")
                    Dist_L = self.ser.read()
                    Dist_H = self.ser.read()
                    self.dist = (ord(Dist_H) * 256) + (ord(Dist_L))
                    #print(self.dist)
                    for i in range (0,5):
                        self.ser.read()
                    self.recievedData = True
                    break


