import random
from graph import Graph;
from list import LinkedList;

class Agent:
    def __init__(self, env): #recibe como parámetro un objeto de la clase Environment
        #Define el tamaño del tablero
        self.maxX = env.sizeX - 1;
        self.maxY = env.sizeY - 1;
        
        #Define una posicion aleatoria
        x = random.randrange(env.sizeX);
        y = random.randrange(env.sizeY);
        
        while (env.isDirty(x, y)): #Si hay obstáculo, sigue buscando una posicion al azar
            x = random.randrange(env.sizeX);
            y = random.randrange(env.sizeY);
        self.currentX = x;
        self.currentY = y;
        #Avisa al tablero donde se va a encontrar
        env.move(self.currentX, self.currentY);
        #Guarda el entorno
        self.env = env;

    #Acciones del agente
    def up(self):
        #Se mueve
        self.currentY -= 1;
        #Envia la nueva posicion 
        self.__sendPosition();
    def down(self):
        #Se mueve
        self.currentY += 1;
        #Envia la nueva posicion 
        self.__sendPosition();
    def left(self):
        #Se mueve
        self.currentX -= 1;
        #Envia la nueva posicion 
        self.__sendPosition();
    def right(self):
        #Se mueve
        self.currentX += 1;
        #Envia la nueva posicion 
        self.__sendPosition();
    def __sendPosition (self): 
        self.env.move(self.currentX, self.currentY);

    def BFS (self):
        #Crea el grafo
        G = Graph();
        #Crea la cola
        Q = LinkedList();
        #Posicion actual
        currentPosition = (self.currentX, self.currentY);
        #Posicion objetivo
        target = (self.env.targetX, self.env.targetY);
        #Si la posición actual es el objetivo
        if(currentPosition == target):
            return False, print("La posicion inicial es el destino");
        
        #Agrega la posición inicial
        G.addVertex(0, currentPosition);
        Q.enqueue(0);
        #Contador que llevará la cuenta para que cada vértice tenga un nombre distinto
        currentVertex = 0;
        #Mientras no haya más nodos a revisar
        while (Q.lenght() > 0):
            #Actualiza la posición
            vertex = G.getVertex( Q.dequeue() );
            currentPosition = vertex.getValue();
            #Si la posición actual es el destino, genera el camino hasta la posicion inicial y lo devuelve
            if(currentPosition == target):
                self.env.setTarget(target[0], target[1]);
                return self._generateRoad(G, vertex.getName());
            #Agrega los nodos a revisar y devuelve el número del vertice actual
            currentVertex = self._getFrontier(G, Q, vertex, currentVertex);
        return False, print("No existe el camino")
    def _getFrontier(self, G, queue, vertex, currV):
        x = vertex.getValue()[0];
        y = vertex.getValue()[1];
        parent = vertex.getName();
        childrens = {};
        #Función que agrega el vértice al gafo, sus conecciones y el nombre a la lista
        def appendNode (currX, currY, movement, currentV):
            currentV += 1;
            childrens[currentV] = {
                "value": (currX, currY),
                "key": movement 
            };
            #Setea la casilla como visitada
            self.env.setVisited(currX, currY);
            #Agrega a la cola el vértice a visitar
            queue.enqueue( currentV );
            return currentV;
 
        #Se puede mover a la derecha y nunca ha ido a ese lugar
        if( (x < self.maxX) and (not self.env.isVisited(x + 1, y)) ): 
            currV = appendNode(x + 1, y, "derecha", currV);
            
        #Se puede mover a la izquierda
        if( (x > 0) and (not self.env.isVisited(x - 1, y)) ): 
            currV = appendNode(x - 1, y, "izquierda", currV);

        #Se puede mover abajo 
        if( (y < self.maxY) and (not self.env.isVisited(x, y + 1)) ): 
            currV = appendNode(x, y + 1, "abajo", currV);
            
        #Se puede mover arriba
        if( (y > 0) and (not self.env.isVisited(x, y - 1))): 
            currV = appendNode(x, y - 1, "arriba", currV);
        G.addChildrens(parent, childrens);
        return currV;
    def _generateRoad(self, G, current):
        L = LinkedList();
        states = len(G.V);
        currentV = G.getVertex(current);
        while (currentV.getParent() != None):
            L.enqueue(currentV.getKey());
            currentV = currentV.getParent();
        print("Se han generado "+str(states)+" estados posibles.");
        print("\nLos pasos a seguir son: ", end="");
        L.show();
        return True, states;