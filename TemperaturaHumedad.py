#!/usr/bin/python
import sys
import Adafruit_DHT



def GetHumedadTemperatura():
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)
    return humidity, temperature

def GetHumedad(PiPin):
    humidity, temperature = Adafruit_DHT.read_retry(11,PiPin)
    return humidity
