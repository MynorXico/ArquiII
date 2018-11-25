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