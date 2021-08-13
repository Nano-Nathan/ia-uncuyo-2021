import random
class Environment:
    def __init__(self, sizeX = 2, sizeY = 2, init_posX = 0, init_posY = 0, dirt_rate = 0.1):
        #Guarda el desempeño del agente
        self.performance = 0;
        #Define e inicia el tablero
        x = [];
        for _ in range (sizeX):
            x.append([0] * sizeY);
        self.board = x;
        self._initBoard(int(dirt_rate * 10));
        #Guarda la posicion del agente
        self.posX = init_posX;
        self.posY = init_posY;
        self.sizeX = sizeX;
        self.sizeY = sizeY;
    
    def _initBoard(self, dirtRate):
        #Se genera un arreglo que guarda la probabilidad de que un cuadrado esté sucio
        aRate = ([True] * dirtRate) + ([False] * (10 - dirtRate));
        #Ensucia algunos cuadros del tablero
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(aRate[random.randrange(10)] == True): #Si en la posicion es True, la casilla está sucia
                    self.board[j][i] = 1;

    def acceptAction(self,action):
        bActionOK = False;
        if(action == "clean"): #Accion de limpiar casilla (donde se encuentra el agente)
            self.performance += 1;
            self.board[self.posX][self.posY] = 0;
            bActionOK = True;
        elif (action == "up"): #Subir
            if(self.posY > 0):
                self.posY -= 1;
                bActionOK = True;
        elif (action == "down"): #Bajar
            if(self.posY < len(self.board[0]) - 1):
                self.posY += 1;
                bActionOK = True;
        elif (action == "left"): #Izquierda
            if(self.posX > 0):
                self.posX -= 1;
                bActionOK = True;
        elif (action == "right"): #Derecha
            if(self.posX < len(self.board) - 1):
                self.posX += 1;
                bActionOK = True;
        return bActionOK
    
    def isDirty(self):
        return self.board[self.posX][self.posY] == 1;

    def getPerformance(self):
        return self.performance;

    def printEnvironment(self):
        #Arreglo que guardará la cantidad de filas que hay en el casillero
        aBoard = [""] * len(self.board[0]);
        #Se generan los strings de cada fila
        for i in range (self.sizeY): #Filas
            for j in range (self.sizeX): #Columnas
                if(self.board[j][i] == 1): #Casillero Sucio
                    aBoard[i] += " Dirty |";
                else: # Casillero limpio
                    aBoard[i] += "       |";
            #Elimina el ultimo '|' de la columna
            aBoard[i] = aBoard[i][: len(aBoard[i]) - 1];
        # Se agrega el agente al casillero (reemplazando lo que haya ahi)
        aBoard[self.posY] = aBoard[self.posY][:8*self.posX] + " Agent " + aBoard[self.posY][8*self.posX + 7:];
        #Se muestra por pantalla el string
        for sRow in aBoard:
            print(sRow);
        print("\n\n")
