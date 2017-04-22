#!/usr/bin/env python

import time
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
luz = 0
tempo = 0

start_time = time.time()

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.01)
        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
while True:
        f = open('Results.txt', 'a')
        luz = RCtime(18)
        tempo = time.time() - start_time
        print ('\t' + str(luz) + '\t' + str(tempo) + '\n')
        f.write('\t' + str(luz) + '\t' + str(tempo) + '\n')
        f.close()

