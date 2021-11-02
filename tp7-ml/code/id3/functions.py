import math
columnResult = "play"
columnResultPositive = "yes"

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
    ##Separa entre filas y atributos
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
    return (oData, titles)


# SELECCIONA EL MEJOR ATRIBUTO
def selectBest(attributes, examples):
    #Parsea la data
    oData = __getAttributeValues(attributes, examples)
    #Obtiene el mejor atributo
    best = 0
    for v in oData:
        if(v != 'positives' and v != "negatives"):
            #Calcula la ganancia
            g = __Ganancia(oData, v)
            #Si la ganancia obtenida es mayor a la actual, guarda el atributo
            if(g > best):
                attribute = v
                best = g
    #Devuelve el mejor atributo y una list con los valores que puede tomar
    return (attribute, list(map(lambda e: e['name'], oData[attribute])))

def __getAttributeValues (attributes, examples):
    global columnResult
    global columnResultPositive
    """
        Devuelve un objeto de la forma
        {
            nombreAtributo: [
                {
                    'name': posibleValor,
                    'count': vecesQueSeRepite,
                    'positives': vecesQueSeJuega,
                    'negatives': vecesQueNoSeJuega
                }
            ],
            'positives': positivosTotales,
            'negatives': negativosTotales
        }
    """
    #Guardara la data
    data = {
        'positives': 0,
        'negatives': 0
    }
    #Agrega los atributos
    for a in attributes:
        data[a] = []
    #Selecciona los posibles valores, la cantidad de veces que se repite y las decisiones positivas y negativas
    for e in examples:
        #Avisa si tiene respuesta positiva o negativa
        bPlay = e[columnResult] == columnResultPositive
        for a in attributes:
            if(a != columnResult):
                try:
                    #Inicializa o aumenta en uno el contador del valor
                    posiblesValues = data[a]
                    object = [x for x in posiblesValues if x['name'] == e[a]]
                    ##object = filter(lambda e: e['name'] == e[a], posiblesValues)
                    #No hay objeto para el valor seleccionado, se crea
                    if(len(object) == 0):
                        data[a].append({
                            'name': e[a],
                            'count': 1,
                            'positives': 1 if bPlay else 0,
                            'negatives': 0 if bPlay else 1
                        })
                    else:
                        sProperty = 'positives' if bPlay else 'negatives'
                        object[0]['count'] += 1
                        object[0][sProperty] += 1
                except:
                    #Inicializa el valor de la variable
                    data[a] = [{
                        'name': e[a],
                        'count': 1,
                        'positives': 1 if bPlay else 0,
                        'negatives': 0 if bPlay else 1
                    }]
        data['positives'] += 1 if bPlay else 0
        data['negatives'] += 0 if bPlay else 1
    return data
def __Ganancia(oData, attribute):
    total = oData['positives'] + oData['negatives']
    #Calcula las probabilidades de los positivos y los negativos
    Ppositives = oData['positives'] / total
    Pnegatives = oData['negatives'] / total
    return __I(Ppositives, Pnegatives) - __Resto(oData)
def __Resto(oData):
    #Obtiene el total de veces que se juega y las que no
    total = oData['positives'] + oData['negatives']
    #Calcula el resto
    resto = 0
    for v in oData:
        #Si no es el atributo que tiene el contador de positivos o negativos
        if(isinstance(v, list)):
            #Total de veces que se juega y que no para cada atributo
            totalAttribute = v['positives'] + v['negatives']
            resto += (totalAttribute / total) * __I( v['positives'] / totalAttribute, v['negatives'] / totalAttribute)
    return resto
def __I (*args):
    I = 0
    for Pv in args:
        I += (-Pv) * math.log2(Pv)
    return I

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
    global columnResult
    startClasiffier = examples[0][columnResult]
    for i in range(1, len(examples)):
        if(examples[i][columnResult] != startClasiffier):
            return False
    return True

#MUESTRA EL ARBOL POR PANTALLA

def showTree(tree):
    print(" "+tree['name'])
    __showTreeR(tree['children'], 2) 
def __showTreeR (children, i):
    for c in children:
        try:
            print("| "*(i-1) +" "+c['name'] )
            newC = c['children']
            __showTreeR(newC, i+1)
        except:
            try:
                print("| "*(i-1) +" "+ c['value'])
                newC = c['children']
                __showTreeR(newC, i+1)
            except:
                #desicion = ("| "*(i-1))
                #print(desicion)
                print(("| "*(i-1)) + "  " +c['desicion'])


