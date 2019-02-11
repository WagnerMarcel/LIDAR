import time
import RPi.GPIO as GPIO

class MOTOR:
    def __init__(self, Step, Dir, MS1, MS2, MS3):
        self.step = Step
        self.dir = Dir
        self.MS1 = MS1
        self.MS2 = MS2
        self.MS3 = MS3
        GPIO.setup(self.step, GPIO.OUT)
        GPIO.setup(self.dir, GPIO.OUT)
        GPIO.setup(self.MS1, GPIO.OUT)
        GPIO.setup(self.MS2, GPIO.OUT)
        GPIO.setup(self.MS3, GPIO.OUT)
        GPIO.output(self.step, GPIO.LOW)
        GPIO.output(self.dir, GPIO.LOW)
        GPIO.output(self.MS1, GPIO.HIGH)
        GPIO.output(self.MS2, GPIO.HIGH)
        GPIO.output(self.MS3, GPIO.LOW)

    # Funktion um Motor zu bewegen
    def moveMotor(self, dir, step, sleepTime):
        if(dir):
            GPIO.output(self.dir, GPIO.HIGH)
        else:
            GPIO.output(self.dir, GPIO.LOW)

        i = 0
        while i < step:
            GPIO.output(self.step, GPIO.HIGH)
            time.sleep(sleepTime)
            GPIO.output(self.step, GPIO.LOW)
            time.sleep(sleepTime)
            i += 1

