import random
class Environment:
    def __init__(self, sizeX = 10, sizeY = 10, dirt_rate = 0.2):
        #Define e inicia el tablero
        t = [];
        for _ in range (sizeX):
            t.append([0] * sizeY);
        self.board = t;
        #Guarda el tamaño del tablero
        self.sizeX = sizeX;
        self.sizeY = sizeY;
        #Ensucia el tablero con obstaculos y agrega el objetivo
        self._initBoard(int(dirt_rate * 10));
        
    def _initBoard(self, dirtRate):
        #Se genera un arreglo que guarda la probabilidad de que un cuadrado esté sucio
        aRate = ([True] * dirtRate) + ([False] * (10 - dirtRate));
        
        #Ensucia algunos cuadros del tablero
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(aRate[random.randrange(10)]): #Si en la posicion es True, la casilla está sucia
                    self.board[j][i] = 1;
        
        #Le busca una posicion al objetivo
        self.targetX = random.randrange(self.sizeX);
        self.targetY = random.randrange(self.sizeY);
        self.board[self.targetX][self.targetY] = -1;
    
    def isDirty(self, x, y):
        return self.board[x][y] == 1;

    def move(self, x, y):
        self.posX = x;
        self.posY = y;

    def setVisited (self, x, y):
        self.board[x][y] = 2;
    
    def setTarget (self, x, y):
        self.board[x][y] = -1;

    def isVisited (self, x, y):
        #Valida que no lo ha visitado y que no hay objeto o el agente
        return self.board[x][y] == 1 or self.board[x][y] == 2 or (self.posX == x and self.posY == y);

    def printEnvironment(self):
        #Arreglo que guardará la cantidad de filas que hay en el casillero
        aBoard = [""] * len(self.board[0]);
        #Se generan los strings de cada fila
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(self.board[j][i] == 1): #Casillero Sucio
                    aBoard[i] += " [   ] |";
                elif (self.board[j][i] == -1): #Objetivo
                    aBoard[i] += "   X   |";
                elif (self.board[j][i] == 2): #Objetivo
                    aBoard[i] += "   .   |";
                else: # Casillero limpio
                    aBoard[i] += "       |";
            #Elimina el ultimo '|' de la columna
            aBoard[i] = aBoard[i][: len(aBoard[i]) - 1];
        #Agrega al tablero el agente
        try:
            aBoard[self.posY] = aBoard[self.posY][:8*self.posX] + " AGENT " + aBoard[self.posY][8*self.posX + 7:];
        except:
            pass
        #Se muestra por pantalla el tablero
        for sRow in aBoard:
            print(sRow);
        print("");
