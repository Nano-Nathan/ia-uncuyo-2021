import random
from Environment import Environment
import copy
class Agent:
    def __init__(self, n = 4, maxStates = 50):
        self.env = Environment(n);
        self.maxStates = maxStates;

    def hillClimbing (self):
        limit = self.maxStates;
        # Obtiene el estado inicial
        state = self.env.getState();
        # Obtiene el costo del estado inicial
        currentCost = self.env.getCost();
        while limit > 0:
            # Obtiene los estados con menor costo
            neighbors, newCost = self.env.getStatesWithLowerCost(state);
            # Si existe, elije uno y sigue, sino devuelve el resultado
            if (len(neighbors) > 0 and newCost < currentCost):
                state = copy.copy(neighbors[random.randrange(len(neighbors))]);
                currentCost = newCost;
            else:
                break;
            limit -= 1;
        # Estado final, estados recorridos, costo del estado final
        return state,(self.maxStates - limit), currentCost ;
