import random
import copy

class Environment:
    def __init__(self, dimention):
        self.dim = dimention
        self.state, self.cost = self.newBoard();

    def getState(self):
        return self.state;
    def getCost (self):
        return self.cost;
    def setCost (self, value):
        self.cost = value;
    def newBoard (self):
        board = [0] * self.dim;
        for i in range (self.dim):
            board[i] = random.randrange(self.dim);
        return board, self.H(board);

    def getNeighbor(self, state):
        dim = len(state);
        position = random.randrange(dim);
        newValue = random.randrange(dim);
        currentValue = state[position];
        while (currentValue == newValue):
            newValue = random.randrange(dim);
        state[position] = newValue;
        return state, self.H(state);

    #Calcula el costo de los demás movimientos a partir del estado actual y devuelve los de menor
    def getStatesWithLowerCost (self, currentState):
        #Calcula el costo del estado actual
        currentCost = self.H(currentState);
        statesWithLowerCost = [];
        #Si no es el estado solucion
        if(currentCost > 0):
            #Itera sobre los posibles movimientos
            for i in range (self.dim):
                #Crea una copia del estado actual, para ir modificando la posicion de cada reina
                newState = copy.copy(currentState);
                for j in range (self.dim):
                    # Solo calcula el costo para estados distintos al original
                    if(j != currentState[i]):
                        # Mueve a la reina
                        newState[i] = j;
                        newCost = self.H(newState);
                        # Si el costo del nuevo estado es menor al actual, resetea el array
                        if(newCost < currentCost):
                            currentCost = newCost;
                            statesWithLowerCost = [copy.copy(newState)];
                        # Si es igual, lo agrega
                        elif(newCost == currentCost):
                            statesWithLowerCost.append(copy.copy(newState));
        return statesWithLowerCost, currentCost;
    
    # Calcula la cantidad de choques que contiene el estado actual del tablero
    # Choque: 2 reinas pueden "verse"
    def H (self, newBoard):
        countCrashes = 0;
        isRow = True;
        length = len(newBoard);
        for i in range (length):
            currentQueen = newBoard[i];
            #Si no hay una reina en la diagonal superior
            isTopDiagonal = True;
            #Si no hay una reina en la diagonal inferior
            isBottomDiagonal = True;
            #Si no hay una reina en la misma fila

            for j in range (i+1, length):
                neighborQueen = newBoard[j];
                diagonal = j - i;
                                
                #Si se encuentra en la misma linea
                if(isRow and currentQueen == neighborQueen):
                    isRow = False;
                    countCrashes += 1;
                #Si esta en la diagonal hacia abajo (sin salirse del tablero)
                elif( 
                    isBottomDiagonal and
                    currentQueen + diagonal < length and
                    neighborQueen == currentQueen + diagonal
                ):
                    isBottomDiagonal = False;
                    countCrashes += 1;
                #Si esta en la diagonal hacia arriba  (sin salirse del tablero)
                elif (
                    isTopDiagonal and
                    currentQueen - diagonal >= 0 and
                    neighborQueen == currentQueen - diagonal
                ):
                    isTopDiagonal = False;
                    countCrashes += 1;
        return countCrashes;
