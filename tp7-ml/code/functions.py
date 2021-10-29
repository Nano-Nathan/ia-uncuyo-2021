# MANEJADOR DE LOS DATOS
def getData (sPath):
    #Lee el archivo
    file = open(sPath, "r")
    content = file.read()
    #parsea la data
    oData = __parseData(content)
    #Cierra el archivo
    file.close()
    return oData
def __parseData (content):
    ##Divide las filas
    content = content.split("\n")
    ##Separa entre filas y titulos
    titles = content[0].split(",")
    rows = map(lambda x : x.split(","), content[1:len(content)])
    ##Guardara un vector con objetos que tendran la data de cada fila
    oData = []
    lenData = len(titles)
    for r in rows:
        newData = {}
        for i in range(lenData):
            newData[titles[i]] = r[i]
        oData.append(newData)
    return oData


# SELECCIONA EL MEJOR ATRIBUTO
def selectBest(attributes, examples):
    return
def __calcluleEntropy ():
    return
def __getAttributeValues (attributes, examples):
    #Guardara la data
    data = {}
    #Por cada atributo, selecciona los posibles valores
    for e in examples:
        for a in attributes:
            try:
                #Inicializa o aumenta en uno el contador del valor
                value = data[a]
                object = list(filter(lambda e: e['name'] == e[a], value))
                #No hay objeto para el valor seleccionado, se crea
                if(len(object) == 0):
                    data[a].append({
                        'name': e[a],
                        'count': 1
                    })
                else:
                    object[0]['count'] += 1
            except:
                #Inicializa el con un valor inicial
                data[a] = [{
                    'name': e[a],
                    'count': 1
                }]
    return data


#OBTIENE EL VALOR DE LA MAYORIA EN UN CONJUNTO DE DATOS PARA UN ATRIBUTO DADO
def getMajority (examples, attribute):
    #Inicializa los datos
    data = {
        examples[0][attribute]: 1,
        'heighter': {
            'name': examples[0][attribute],
            'value': 1
        }
    }
    for i in range(1, len(examples)):
        value = examples[i][attribute]
        #Aumenta en 1 o crea la variable en el objeto
        try:
            data[value] += 1
        except:
            data[value] = 1
        #Valida si el contador del posible valor actual es mayor que el anterior
        if(data['heighter']['value'] < data[value]):
            #Actualiza el mayor
            data['heighter']['name'] = value
            data['heighter']['value'] = data[value]
    #Devuelve el nombre del atributo con mas ocurrencias
    return data['heighter']['name']

#OBTIENE EJEMPLOS CON VALORES DADOS EN UN ATRIBUTO
def getExamplesWith(examples, attribute, value):
    return list(filter(lambda e: e[attribute] == value, examples))

#VALIDA SI TIENE MAS DE UNA CLASIFICACION
def isOneValue(examples):
    startClasiffier = examples[0]['play']
    for i in range(1, len(startClasiffier)):
        if(startClasiffier[i]['play'] != startClasiffier):
            return False
    return True
