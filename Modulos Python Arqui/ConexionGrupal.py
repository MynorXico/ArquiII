from pymongo import MongoClient
import datetime
client = MongoClient('mongodb://admin:1admin@ds263500.mlab.com:63500/arquitwo')

db = client['arquitwo']
collection = db['test']

def InsertarDato(modulo, posX, posY,value, description):
    collection.insert_one({
            "Grupo" : 1,
            "Date"  : datetime.datetime.now(),
            "Modulo" : modulo,
            "X": posX,
            "Y": posY,
            "valor": value,
            "descripcion": description
        })

    
InsertarDato("temperatura",10,15,72,"Mide la temperatura")
