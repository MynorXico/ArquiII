from gpiozero import LightSensor, Buzzer
import RPi.GPIO as GPIO, time , os
#GPIO.setmode(GPIO.BOARD) 

def GetLight1 (PiPin): 
    measurement = 0 
    # Discharge capacitor 
    GPIO.setup(PiPin, GPIO.OUT) 
    GPIO.output(PiPin, GPIO.LOW) 
    time.sleep(0.1) 
    GPIO.setup(PiPin, GPIO.IN) 
    # Count loops until voltage across 
    # capacitor reads high on GPIO
    
    while (GPIO.input(PiPin) == GPIO.LOW):
        measurement += 1 
    return measurement

def GetLight(PiPin):
    ldr = LightSensor(PiPin)
    return (1-ldr.value)*4000
