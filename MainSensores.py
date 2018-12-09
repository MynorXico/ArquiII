#import SensorLuz
import TemperaturaHumedad
import TemperatureSensor
import SensorProx
import Conexion
import time
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)
#GPIO.setup(5, GPIO.OUT)
#GPIO.output(5, GPIO.LOW)
GPIOLuz = 27
GPIOHumedad = 23

dev_id = 1					# Id del grupo


sen_id_luz = 3	
sen_id_humedad = 2
sen_id_temperatura = 1
sen_id_distancia = 4

sensores = ["", "Temperatura", "Humedad", "Luz", "Distancia"]


xactual = -1
yactual = -1

print(Conexion.getPosToMove())

def ObtenerXY():
    global xactual
    global yactual
    xactual, yactual = Conexion.getPosToMove()
    print("Se obtuvieron las coordenadas ")

ObtenerXY()
def InsertarDato(sen_id, value):
    global xactual
    global yactual
    Conexion.InsertarXplorer(sen_id, xactual, yactual, value)
    print("Se inserta valor de " + str(value) + " para " + sensores[sen_id])


def Insertar2Minutos():
        ObtenerXY()
        startingTime = time.time()
        #GPIO.output(5, GPIO.HIGH)
        while(time.time()<=startingTime+120):
            inicia = time.time()
            #InsertarDato(sen_id_luz, round(SensorLuz.GetLight(GPIOLuz)))
            InsertarDato(sen_id_humedad, round(TemperaturaHumedad.GetHumedad(GPIOHumedad),2))
            InsertarDato(sen_id_temperatura, round(TemperatureSensor.getTemperatura(),2))
            InsertarDato(sen_id_distancia, SensorProx.getDistance())
            #print(round(SensorLuz.GetLight(GPIOLuz)))
            #print(round(TemperaturaHumedad.GetHumedad(GPIOHumedad),2))
            #print(round(TemperatureSensor.getTemperatura(),2))
            #print(round(SensorProx.getDistance()))
            while(time.time() <= inicia+2): 
                print("waiting")
        #GPIO.output(5, GPIO.LOW)

