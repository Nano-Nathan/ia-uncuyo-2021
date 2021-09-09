import random
import math
import copy
from Environment import Environment
class Agent:
    def __init__(self, n = 4, maxStates = 50):
        self.env = Environment(n);
        self.maxStates = maxStates;

    def hillClimbing (self):
        limit = self.maxStates;
        # Obtiene el estado inicial
        currentState = self.env.getState();
        # Obtiene el costo del estado inicial
        currentCost = self.env.getCost();
        while (limit > 0):
            # Obtiene los estados con menor costo
            neighbors, newCost = self.env.getStatesWithLowerCost(currentState);
            # Si existe, elije uno y sigue, sino devuelve el resultado
            if (len(neighbors) > 0 and newCost < currentCost):
                # Guarda el nuevo estado y su costo
                currentState = copy.copy(neighbors[random.randrange(len(neighbors))]);
                currentCost = newCost;
            else:
                break;
            limit -= 1;
        # Estado final, estados recorridos, costo del estado final
        return currentState, (self.maxStates - limit), currentCost;

    def simulatedAnnealing (self):
        limit = self.maxStates;
        # Obtiene el estado inicial
        currentState = self.env.getState();
        # Obtiene el costo del estado inicial
        currentCost = self.env.getCost();
        #Si no encontró la solución
        if(currentCost != 0):    
            while (limit > 0):
                T = self.schedule(limit);
                if(T == 0):
                    break;
                #Elije un estado vecino al azar
                neighbor, newCost = self.env.getNeighbor(copy.copy(currentState));
                #Si encontró la solución
                if(newCost == 0):
                    currentState = copy.copy(neighbor);
                    currentCost = newCost;
                    break;
                #Calcula la distancia entre los estados
                deltaE = newCost - currentCost;
                #Si el nuevo estado tiene un costo menor o buena probabilidad
                if(deltaE < 0):
                    currentState = copy.copy(neighbor);
                    currentCost = newCost;
                else:
                    if(math.exp(- 1 / T) > 0.5):
                        currentState = copy.copy(neighbor);
                        currentCost = newCost;
                limit -= 1;
        return currentState, (self.maxStates - limit), currentCost;
    def schedule (self, t):
        return 0.5 * t;