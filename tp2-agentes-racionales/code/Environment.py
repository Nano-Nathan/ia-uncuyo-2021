import random
class Environment:
    def __init__(self, sizeX = 2, sizeY = 2, dirt_rate = 0.1):
        #Guarda el desempeño del agente
        self.performance = 0;
        #Define e inicia el tablero
        t = [];
        for _ in range (sizeX):
            t.append([0] * sizeY);
        self.board = t;
        #Guarda la posicion inicial del agente
        self.sizeX = sizeX;
        self.sizeY = sizeY;
        #Ensucia el tablero
        self._initBoard(int(dirt_rate * 10));
    
    def _initBoard(self, dirtRate):
        #Se genera un arreglo que guarda la probabilidad de que un cuadrado esté sucio
        aRate = ([True] * dirtRate) + ([False] * (10 - dirtRate));
        #Ensucia algunos cuadros del tablero
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(aRate[random.randrange(10)]): #Si en la posicion es True, la casilla está sucia
                    self.board[j][i] = 1;

    def isDirty(self):
        return self.board[self.posX][self.posY] == 1;

    def move(self, x, y):
        self.posX = x;
        self.posY = y;

    def clean(self):
        self.performance += 1;
        self.board[self.posX][self.posY] = 0;

    def getPerformance(self):
        dirty = 0;
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if (self.board[j][i]):
                    dirty += 1;
        return dirty;

    def printEnvironment(self):
        #Arreglo que guardará la cantidad de filas que hay en el casillero
        aBoard = [""] * len(self.board[0]);
        #Se generan los strings de cada fila
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(self.board[j][i] == 1): #Casillero Sucio
                    aBoard[i] += " dirty |";
                else: # Casillero limpio
                    aBoard[i] += "       |";
            #Elimina el ultimo '|' de la columna
            aBoard[i] = aBoard[i][: len(aBoard[i]) - 1];
        #Agrega al tablero el agente
        aBoard[self.posY] = aBoard[self.posY][:8*self.posX] + " AGENT " + aBoard[self.posY][8*self.posX + 7:];
        #Se muestra por pantalla el tablero
        for sRow in aBoard:
            print(sRow);
        print("");
