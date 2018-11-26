import SensorLuz
import TemperaturaHumedad
import TemperatureSensor
import SensorProx
import Conexion
import time


GPIOLuz = 17
GPIOHumedad = 23

dev_id = 1					# Id del grupo

sen_id_luz = -1	
sen_id_humedad = -1
sen_id_temperatura = -1
sen_id_distancia = -1

xactual = -1
yactual = -1

print(Conexion.getPosToMove())

def ObtenerXY():
    global xactual
    global yactual
    xactual, yactual = Conexion.getPosToMove()
    print("Se obtuvieron las coordenadas ")

def InsertarDato(sen_id, value):
    global xactual
    global yactual
    InsertarXplorer(sen_id, xactual, yactual, value)
    print("Se insertó valor de sensores ")

	
	
def Insertar2Minutos():
	while True:
		InsertarDato(sen_id_luz, SensorLuz.GetLight(GPIOLuz))
		InsertarDato(sen_id_humedad, TemperaturaHumedad.GetHumedad(GPIOHumedad))
		InsertarDato(sen_id_temperatura, TemperatureSensor.getTemperatura())
		InsertarDato(sen_id_distancia, SensorProx.getDistance())
		time.sleep(2)
