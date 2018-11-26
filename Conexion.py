from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://admin:1admin@ds263500.mlab.com:63500/arquitwo')
db = client['arquitwo']

#Metodo que todos lo grupos deben usar para insertar a la base de datos
def InsertarXplorer(sen_id, posX, posY, value):
    collection = db['XPlorer']
    collection.insert_one({
        "Date": datetime.datetime.now(),
        "Device_ID": 1,
        "Sensor_ID": sen_id,
        "X": posX,
        "Y": posY,
        "Sensor_Value": value
    })

def getPosToMove():
    collection = db["Pic"]
    listx = []
    listxpos = []
    listy = []
    listypos = []
    result = []
    print(collection.find())
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
    return posX, posY
	
	
matriz = getPosToMove()
print(matriz[0])
print(matriz[1])
