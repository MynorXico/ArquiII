import SensorLuz
import TemperaturaHumedad
import TemperatureSensor
#import SensorProx
import Conexion
import time


GPIOLuz = 17
GPIOHumedad = 23

dev_id = 1					# Id del grupo


sen_id_luz = 3	
sen_id_humedad = 2
sen_id_temperatura = 1
#sen_id_distancia = 4

sensores = ["", "Temperatura", "Humedad", "Luz"]


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
    print("Se insertó valor de " + str(value) + " para " + sensores[sen_id])


def Insertar2Minutos():
        ObtenerXY()
	startingTime = time.time()
	while(time.time()<=startingTime+120):
            inicia = time.time()
            InsertarDato(sen_id_luz, SensorLuz.GetLight(GPIOLuz))
            InsertarDato(sen_id_humedad, TemperaturaHumedad.GetHumedad(GPIOHumedad))
            InsertarDato(sen_id_temperatura, TemperatureSensor.getTemperatura())
            #InsertarDato(sen_id_distancia, SensorProx.getDistance())
            while(time.time() <= inicia+2): 
                print("waiting")


