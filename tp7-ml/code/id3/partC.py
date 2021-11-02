from functions import *

result = "play"

#OBTIENE LA DATA
(oData, attributes) = getData("../../data/tenis.csv")

#CREA EL ARBOL DE DECISION
def decisionTree (examples, attributes, value):
    global result
    if (len(examples) == 0):
        return {
            'decision': value
        }
    #Si todos los elementos del ejemplo tienen la misma clasificacion (se juega o no), devolver la clasificacion
    elif(isOneValue(examples)):
        return {
            'desicion': examples[0][result]
        }
    #Si no hay mas titulos por recorrer, devolver el valor de la mayoria
    elif (len(attributes) == 0):
        return {
            'desicion': getMajority(examples, result)
        }
    else:
        #Selecciona el mejor atributo y los valores que puede tomar
        (best, bestValues) = selectBest(attributes, examples)
        #Obtiene los nuevos atributos disponibles
        attributes.remove(best)
        #Crea un nodo con el nombre del mejor atributo
        tree = {
            'name': best,
            'children': list(map(lambda e: {'value':e, 'children': []}, bestValues))
        }
        #Por cada valor que puede tomar el atributo
        for i in range (len(bestValues)):
            #Obtiene los ejemplos donde el atributo seleccionado es el valor de la iteracion
            newExamples = getExamplesWith(examples, best, bestValues[i])
            #Obtiene el valor de la mayoria (se juega o no?)
            majority = getMajority(newExamples, result)
            #Calcula el subarbol
            subTree = decisionTree(newExamples, attributes, majority)
            #Lo inserta en valor que le corresponda en el padre
            tree['children'][i]['children'].append(subTree)
        return tree

tree = decisionTree(oData, attributes, "no decision")
showTree(tree)
