import RPi.GPIO as GPIO
import time
import math
#import MainSensores as sensores
import Conexion

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
acceleration = 0

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

def retTime(meters):
    global acceleration
    return math.sqrt((2*meters)/acceleration)
    
def move(newX,newY):
    clean()

    global x
    global y

    yRange = y - newY
    for i in range(yRange):
        forward(2.76)
        stop(0.5)
    y = newY
    
    xRange = x - newX
    if xRange > 0:
        left(1.30)
        stop(0.5)
        for i in range(xRange):
            forward(2.76)
            stop(0.5)
        x = newX

    #sensores.Insertar2Minutos()

    if newX != 5 or newY !=5:
        left(1.3)
        stop(0.5)
        left(1.3)
        stop(0.5)
    clean()

def ret(newX,newY):
    clean()

    global x
    global y

    xRange = newX - x
    for i in range(xRange):
        forward(2.76)
        stop(0.5)
    x = newX
    
    yRange = newY - y
    if yRange > 0:
        if xRange > 0:
            right(1.05)
            stop(0.5)
        for i in range(yRange):
            forward(2.76)
            stop(0.5)
        y = newY

    if x != 5 or y !=5:
        if yRange == 0:
            left(1.3)
            stop(0.5)
        else:
            left(1.3)
            stop(0.5)
            left(1.3)
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

    #sensores.Insertar2Minutos()

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
	
	
matriz = getPosToMove()
print(matriz[0])
print(matriz[1])

#PREDEFINED TIME
move(Conexion.getPosToMove())
ret(5,5)

#CALCULATED TIME
#moveCalc(3,3)
#print(x)
#print(y)
#retCalc(5,5)

clean()
print("Ended")
GPIO.cleanup()
