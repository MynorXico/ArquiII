import RPi.GPIO as GPIO
import time
import math
import MainSensores as sensores
import Conexion
import atexit



GPIO.setmode(GPIO.BCM)

#RIGHT
#MOTOR 1 DF
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#MOTOR 2 DT
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

#LEFT
#MOTOR 3 IF
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

#MOTOR 4 IT
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

x = 5
y = 5
acceleration = 0.23
timeD=3.15
timeG=1.4
def clean():
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)

def right(seconds):
    #Forward_Left_Motor
    print('Right')
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    time.sleep(seconds)

def left(seconds):
    #Forward_Right_Motor
    print('Left')
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(seconds)
    
def backwards(seconds):
    print('Backwards')
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(seconds)
    
def forward(seconds):
    print('Forward')
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    time.sleep(seconds)
    
def stop(seconds):
    print('Stop')
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(seconds)

def retTime(meters):
    global acceleration
    return math.sqrt((2*meters)/acceleration)
    
def move(newX,newY):
    clean()

    global x
    global y
    global timeD
    global timeG

    yRange = y - newY
    for i in range(yRange):
        forward(timeD)
        stop(0.5)
    y = newY
    
    xRange = x - newX
    if xRange > 0:
        left(timeG)
        stop(0.5)
        for i in range(xRange):
            forward(timeD)
            stop(0.5)
        x = newX

    sensores.Insertar2Minutos()

    if newX != 5 or newY !=5:
        left(timeG)
        stop(0.5)
        left(timeG)
        stop(0.5)
    clean()

def ret(newX,newY):
    clean()

    global x
    global y
    global timeD
    global timeG
    tempX = x
    tempY = y

    xRange = newX - x
    for i in range(xRange):
        forward(timeD)
        stop(0.5)
    x = newX
    
    yRange = newY - y
    if yRange > 0:
        if xRange > 0:
            right(timeG)
            stop(0.5)
        for i in range(yRange):
            forward(timeD)
            stop(0.5)
        y = newY

    if tempX != 5 or tempY !=5:
        if yRange == 0:
            left(timeG)
            stop(0.5)
        else:
            left(timeG)
            stop(0.5)
            left(timeG)
            stop(0.5)

    clean()

def moveCalc(newX,newY):
    clean()

    global x
    global y

    yRange = y - newY
    forward(retTime(yRange))
    stop(0.5)
    y = newY
    
    xRange = x - newX
    if xRange > 0:
        left(1.30)
        stop(0.5)
        forward(retTime(xRange))
        stop(0.5)
        x = newX
    sensores.Insertar2Minutos()

    if newX != 5 or newY !=5:
        left(1.3)
        stop(0.5)
        left(1.3)
        stop(0.5)
    clean()

def retCalc(newX,newY):
    clean()

    global x
    global y

    xRange = newX - x
    forward(retTime(xRange))
    stop(0.5)
    x = newX
    
    yRange = newY - y
    if yRange > 0:
        if xRange > 0:
            right(1.05)
            stop(0.5)
        forward(retTime(yRange))
        stop(0.5)
        y = newY

    if newX != 5 or newY !=5:
        if yRange == 0:
            left(1.3)
            stop(0.5)
        else:
            left(1.3)
            stop(0.5)
            left(1.3)
            stop(0.5)

    clean()

def getPosToMove():
    collection = db["Pic"]
    listx = []
    listxpos = []
    listy = []
    listypos = []
    result = []

    for i in collection.find():
        if(i['X'] == 0):
            listy.append(i['Escala'])
            listypos.append(i['Y'])

        if (i['Y'] == 0):
            listx.append(i['Escala'])
            listxpos.append(i['X'])

    posX = listxpos[listx.index(max(listx))]
    posY = listypos[listy.index(max(listy))]
    result.append(posX)
    result.append(posY)
    return result
	
	
#matriz = getPosToMove()
#print(matriz[0])
#print(matriz[1])

#PREDEFINED TIME

moveToX, moveToY = Conexion.getPosToMove()
print("X: " + str(moveToX) + "Y: " + str(moveToY))
move(moveToX, moveToY)
ret(5,5)
#print(retTime(5))
#forward(retTime(5))

#CALCULATED TIME
#moveCalc(5,4)
#print(x)
#print(y)
#retCalc(5,5)

def exit_handler():
    clean()
    print("Ended")
    GPIO.cleanup()

clean()
print("Ended")
GPIO.cleanup()
