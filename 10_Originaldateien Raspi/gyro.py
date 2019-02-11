import smbus
import math
import time

power_mgmt_1 = 0x6b

bus = smbus.SMBus(1)
adress = 0x68

bus.write_byte_data(adress, power_mgmt_1, 0)

def read_data(reg):
    h = bus.read_byte_data(adress, reg)
    l = bus.read_byte_data(adress, reg+1)
    value = (h << 8) + l
    return value

def read_data_2c(reg):
    val = read_data(reg)
    if(val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
    
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_x(x,y,z):
    radians = math.atan2(x,dist(y,z))
    return math.degrees(radians)

def get_y(x,y,z):
    radians = math.atan2(y,dist(x,z))
    return -math.degrees(radians)

while(True):
    g_x = read_data_2c(0x43)
    g_y = read_data_2c(0x45)
    g_z = read_data_2c(0x47)

    print("Werte:")
    print ("x: %5f" % (g_x/131.0))
    print ("y: %5f" % (g_y/131.0))
    print ("z: %5f" % (g_z/131.0))
    print ("%5f" % get_x(g_x,g_y,g_z))
    print ("%5f" % get_y(g_x,g_y,g_z))
    time.sleep(3)
