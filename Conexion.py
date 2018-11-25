from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://admin:ladmin@ds263500.mlab.com:63500/arquitwo")
db = client['arquitwo']

#Metodo que todos los grupos deben usar para insertar a la base de datos

dev_id = 1

def InsertarXplorer(sen_id,posX,posY,value):
    collection = db['Xplorer']
    collection.insert_one({
        "Date":datetime.datetime.now(),
        "Device_ID":dev_id,
        "Sensor_ID":sen_id,
        "X": posX,
        "Y": posY,
        "Sensor_Value": value
    })

