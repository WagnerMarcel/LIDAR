## Programm zur Steuerung des LIDAR Systems

# Bibliotheken
import time
import datetime
import math
import RPi.GPIO as GPIO

# Eigene Dateien
import Lidar
import Motor


# GPIO Nummerierung gleich der Pin Nummer
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pins & Definitionen
workingLED = 11
fan = 13
lightGate = 23 #SPI SCLK --> In Version 2 der Platine eigenen Pin zuweisen

# Motor 1, Nema 11
M1 = Motor.MOTOR(31,29,37,35,33)

# Motor 2, Nema 17
M2 = Motor.MOTOR(18,16,36,38,40)

# LIDAR Sensor
tfMini = Lidar.LIDAR()

# Funktion um GPIO's zu Initalisieren
def initGPIO():
    GPIO.setup(workingLED, GPIO.OUT)
    GPIO.output(workingLED, GPIO.LOW)
    GPIO.setup(fan, GPIO.OUT)
    GPIO.output(fan, GPIO.LOW)
    GPIO.setup(lightGate, GPIO.IN)

def homeAxis():
    while(GPIO.input(lightGate)!=GPIO.HIGH):
        M2.moveMotor(1,1,0.001)
    count = 0
    while(GPIO.input(lightGate)==GPIO.HIGH):
        M2.moveMotor(1,1,0.001)
        count += 1
    M2.moveMotor(1,36,0.001)

initGPIO()
tfMini.getData()
tfMini.recievedData = False
homeAxis()
time.sleep(1)

stepsFullRotM2 = 200*8*6
stepsQuartRotM1 = 50*4

M1dir = False
M2dir = True

print(tfMini.dist)
tfMini.getData()
tfMini.recievedData = False

data = open("data"+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+".csv", "w")
data.write("Nr;Distance;Azimuth;Elevation\n")
valueNr = 1

countM1 = 0
countM2 = 0
while(countM1 < stepsQuartRotM1):
    if(M2dir):
        while(countM2 < stepsFullRotM2):
            tfMini.getData()
            tfMini.recievedData = False
            data.write(str(valueNr) + ";" + str(tfMini.dist) + ";" + str(360.0*countM2/stepsFullRotM2) + ";" + str(90.0*countM1/stepsQuartRotM1) + "\n")
            M2.moveMotor(M2dir,4,0.00025)
            valueNr += 1
            countM2 += 4
    else:
        while(countM2 >= 0):
            tfMini.getData()
            tfMini.recievedData = False
            data.write(str(valueNr) + ";" + str(tfMini.dist) + ";" + str(360.0*countM2/stepsFullRotM2) + ";" + str(90.0*countM1/stepsQuartRotM1) + "\n")
            M2.moveMotor(M2dir,4,0.00025)
            valueNr += 1
            countM2 -= 4
    M1.moveMotor(M1dir,2,0.005)
    #M1.moveMotor(M1dir,4,0.0005)
    time.sleep(0.5)
    countM1 += 2
    M2dir = not M2dir

