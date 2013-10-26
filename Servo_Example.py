#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

angleMin = 0
angleMax = 180
angleRange = angleMax - angleMin

tickMinTower = 110
tickMaxTower = 650
tickRange = tickMaxTower - tickMinTower

tickMin = 140
tickMax = 690
tickRange = tickMax - tickMin

frequency = 60
pwm.setPWMFreq(frequency)

def angleToms(angle):
  ticksOut = ((angle * tickRange) / angleRange) + tickMin
  return float(ticksOut)

def setPulseDegree(channel, freq, angle):
  ticksOn = angleToms(angle)
  print "%.2f ticksOn for 90 angle" % float(ticksOn)
  pwm.setPWM(channel, 0, int(ticksOn))



def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse *2)

#pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

