import time
import RPi.GPIO as GPIO

workingLED = 11
fan = 13

M1_STEP = 31
M1_DIR = 29
M1_MS1 = 37
M1_MS2 = 35
M1_MS3 = 33

M2_STEP = 18
M2_DIR = 16
M2_MS1 = 36
M2_MS2 = 38
M2_MS3 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(workingLED, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(M1_STEP, GPIO.OUT)
GPIO.setup(M1_DIR, GPIO.OUT)
GPIO.setup(M1_MS1, GPIO.OUT)
GPIO.setup(M1_MS2, GPIO.OUT)
GPIO.setup(M1_MS3, GPIO.OUT)
GPIO.setup(M2_STEP, GPIO.OUT)
GPIO.setup(M2_DIR, GPIO.OUT)
GPIO.setup(M2_MS1, GPIO.OUT)
GPIO.setup(M2_MS2, GPIO.OUT)
GPIO.setup(M2_MS3, GPIO.OUT)

GPIO.output(workingLED, GPIO.LOW)
GPIO.output(fan, GPIO.LOW)
GPIO.output(M1_STEP, GPIO.LOW)
GPIO.output(M1_DIR, GPIO.LOW)
GPIO.output(M1_MS1, GPIO.LOW)
GPIO.output(M1_MS2, GPIO.LOW)
GPIO.output(M1_MS3, GPIO.LOW)
GPIO.output(M2_STEP, GPIO.LOW)
GPIO.output(M2_DIR, GPIO.LOW)
GPIO.output(M2_MS1, GPIO.LOW)
GPIO.output(M2_MS2, GPIO.LOW)
GPIO.output(M2_MS3, GPIO.LOW)



GPIO.output(M2_DIR, GPIO.LOW)
GPIO.output(M2_MS1, GPIO.HIGH)
GPIO.output(M2_MS2, GPIO.HIGH)
GPIO.output(M2_MS3, GPIO.LOW)

i = 0
print("Stepping")
while i < 100*8:
    GPIO.output(M2_STEP, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(M2_STEP, GPIO.LOW)
    time.sleep(0.0005)
    i += 1
##
GPIO.output(M1_DIR, GPIO.LOW)
GPIO.output(M1_MS1, GPIO.HIGH)
GPIO.output(M1_MS2, GPIO.HIGH)
GPIO.output(M1_MS3, GPIO.HIGH)
##
#i = 0
#print("Stepping")
#while i < 50*4:
#    GPIO.output(M1_STEP, GPIO.HIGH)
#    time.sleep(0.002)
#    GPIO.output(M1_STEP, GPIO.LOW)
#    time.sleep(0.002)
#    i += 1
##
##GPIO.output(M2_DIR, GPIO.LOW)
##i = 0
##print("Stepping")
##while i < 600:
##    GPIO.output(M2_STEP, GPIO.HIGH)
##    time.sleep(0.005)
##    GPIO.output(M2_STEP, GPIO.LOW)
##    time.sleep(0.005)
##    i += 1

print("Done")

