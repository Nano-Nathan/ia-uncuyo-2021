import random
from structs.graph import Graph;
from structs.list import LinkedList;
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
    def __sendPosition(self): 
        self.env.move(self.currentX, self.currentY);

    def AStar(self):
        pass