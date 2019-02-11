##import VL53L1X
##
##tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
##tof.open()
##tof.start_ranging(3) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
##dist = tof.get_distance() # Grab the range in mm
##dist = dist/10.0
##print(dist)
##tof.stop_ranging() # Stop ranging

import Lidar

#lidar = Lidar.LIDAR('/dev/ttyAMA0',None)
lidar = Lidar.LIDAR(None, 0x29)
lidar.getData()

print(lidar.dist)