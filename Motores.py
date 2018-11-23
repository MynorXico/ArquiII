import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#RIGHT
#MOTOR 1 DF
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

#MOTOR 2 DT
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

#LEFT
#MOTOR 3 IF
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

#MOTOR 4 IT
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

x = 5
y = 5

def clean():
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)

def right(seconds):
    #Forward_Left_Motor
    print('Right')
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(38,GPIO.HIGH)
    GPIO.output(40,GPIO.LOW)
    time.sleep(seconds)

def left(seconds):
    #Forward_Right_Motor
    print('Left')
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.HIGH)
    time.sleep(seconds)
    
def backwards(seconds):
    print('Backwards')
    GPIO.output(31,GPIO.HIGH)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(32,GPIO.HIGH)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.HIGH)
    time.sleep(seconds)
    
def forward(seconds):
    print('Forward')
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(38,GPIO.HIGH)
    GPIO.output(40,GPIO.LOW)
    time.sleep(seconds)
    
def stop(seconds):
    print('Stop')
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(32,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)
    time.sleep(seconds)
    
def move(newX,newY):
    clean()
    stack = []
    xRange = x - newX
    for i in range(xRange):
        forward(2.76)
        stop(0.5)
    x = newX
    
    yRange = y - newY
    if yRange > 0:
        left(1.05)
        for i in range(yRange):
            forward(2.76)
            stop(0.5)
        y = newY

    #HERE IT GOES THE SENSOR'S CODE

    left(2.10)
    clean()

def ret(newX,newY):
    clean()
    stack = []
    xRange = x - newX
    for i in range(xRange):
        forward(2.76)
        stop(0.5)
    x = newX
    
    yRange = y - newY
    if yRange > 0:
        left(1.05)
        for i in range(yRange):
            forward(2.76)
            stop(0.5)
        y = newY

    if xRange == 0:
        left(1.05)
    else:
        left(2.10)

    clean()

move(3,3)
ret(5,5)
clean()
print("Ended")
GPIO.cleanup()
