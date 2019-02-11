import serial
import VL53L1X

class LIDAR():
    dist = 0
    recievedData = False

    def __init__(self, uart, i2c):
        self.uart = uart
        self.i2c = i2c
        if(self.uart != None and self.i2c == None):
            self.ser = serial.Serial(self.uart, 115200, timeout=1)
        else:
            self.tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=i2c)
            self.tof.open()
            self.tof.start_ranging(3)

    # Funktion um frische Daten vom LIDAR zu erhalten
    def getData(self):
        if(self.uart != None and self.i2c == None):
            self.ser.reset_input_buffer()
            while(self.recievedData != True):
                while(self.ser.in_waiting <= 9):
                    if((b'Y' == self.ser.read()) and (b'Y' == self.ser.read())):
                        Dist_L = self.ser.read()
                        Dist_H = self.ser.read()
                        self.dist = (ord(Dist_H) * 256) + (ord(Dist_L))
                        for i in range (0,5):
                            self.ser.read()
                        self.recievedData = True
                        break
        else:
            self.dist = self.tof.get_distance() # Entfernung in mm
            self.dist = self.dist/10.0
