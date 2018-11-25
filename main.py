import SensorLuz
#import TemperaturaHumedad
#try:
#    import TemperatureSensor
#except:
#    print("No se encuentra el sensor de temperatura")
#    exit()
import SensorProx
import Conexion

GPIOLuz = 17
GPIOHumedad = 23

Conexion.InsertarXplorer(1,1,1,1,1)

while True:
    print("Luz: " + str(SensorLuz.GetLight(GPIOLuz)))
 #   print("Humedad: " + str(TemperaturaHumedad.GetHumedad(GPIOHumedad)))
    print("Temperatura: "+str(TemperatureSensor.getTemperatura()))
    print("Distancia: " + str(SensorProx.getDistance()))

