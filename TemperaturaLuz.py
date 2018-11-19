#!/usr/bin/python
import sys
import Adafruit_DHT

global humidity

def GetHumdadTemperatura
    global humidity
    global temperature
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)