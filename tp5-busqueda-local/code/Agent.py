import random
import math
import copy
from Environment import Environment
class Agent:
    def __init__(self, n = 4, maxStates = 50):
        self.env = Environment(n);
        self.n = n;
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
            print(currentCost)
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
            while (limit > 0 or T == 0):
                T = self.schedule(limit);
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
                    if(math.exp(- 1 / T) > 0.4):
                        currentState = copy.copy(neighbor);
                        currentCost = newCost;
                limit -= 1;
        return currentState, (self.maxStates - limit), currentCost;
    def schedule (self, t):
        return 0.5 * t;
    
    def genetic (self):
        file = open("result.txt", "w");
        content = "";
        minf = "";
        def functionFilter (e):
            try:
                return e['f'] == 0;
            except (Exception):
                pass
        limit = self.maxStates;
        #La pobación constará de 100 individuos y la suma de sus fitness
        currentVillage = [];
        fitnessTotal = 0;
        for _ in range (100):
            state, fitness = self.env.newBoard();
            currentVillage.append(
                {
                    'f': fitness,
                    's': state
                }
            );
            fitnessTotal += fitness;
        currentVillage.append(fitnessTotal);
        solution = list( filter (functionFilter, currentVillage) );        
        #Comienza la ejecucion
        while (limit > 0 and len(solution) == 0):
            #Selecciona los más aptos
            newVillage = self.selection(currentVillage);
            #Realiza la combinación
            newVillage = self.crossover(newVillage);
            #Les aplica mutación
            self.mutation(newVillage);
            #Calcula su fitness
            self.fitness(newVillage);
            content += str(newVillage[100] / 100) + "\n";
            minf += str(newVillage[0]['f']) + "\n"
            #Reemplaza elementos
            currentVillage = newVillage;
            #Verifica si se encontró una solucion
            solution = list( filter (functionFilter, currentVillage) );
            limit -= 1;
        file.write(content);
        file.write("\nfitness: \n");
        file.write(minf);
        file.close();
        if (len(solution) > 0):
            return solution[0]['s'], (self.maxStates - limit), solution[0]['f']
        else:
            return currentVillage[0]['s'], self.maxStates, currentVillage[0]['f']

    def selection (self, village):
        total = village.pop();
        #Calcula las probabilidades
        aProbabilities = [];
        for s in village:
            aProbabilities.append({
                'p': s['f'] / total, #Probabilidad
                'f': s['f'], #Fitness
                's': s['s'] #State
            });
        #Ordena el arreglo por probabilidad
        aProbabilities.sort(key=lambda e : e['p']);
        #Selecciona las 5 primeras
        aProbabilities = aProbabilities[:int(len(village)/2)];
        #Agrega de nuevo el fitness total
        village.append(total);
        #Arma y devuelve la nueva población
        return list(
            map (
                lambda e : {'f': e['f'], 's':e['s']},
                aProbabilities
            )
        );

    def crossover (self, village):
        dim = int(len(village) / 2);
        #Mitad del tamaño de los individuos
        midBoard = int(self.n / 2);
        #Cuarta parte
        fouBoard = int(midBoard / 2);
        #Guarda los hijos que se van creando
        newVillage = [];
        for i in range (dim):
            #Obtiene los padres
            parent1 = village[i]['s'];
            parent2 = village[i+dim]['s'];
            #Genera los hijos: 
            # [1, 2, 3, 4, 5, 6, 7, 8]
            # [a, b, c, d, e, f, g, h]
            #Hijo 1: [1, 2, c, d]
            children1 = parent1[:fouBoard] + parent2[fouBoard:midBoard];
            #Hijo 2: [a, b, 3, 4]
            children2 = parent2[:fouBoard] + parent1[fouBoard:midBoard];
            #Hijo 3: [5, 6, g, h]
            children3 = parent1[midBoard: midBoard + fouBoard] + parent2[midBoard + fouBoard:];
            #Hijo 4: [e, f, 7, 8]
            children4 = parent2[midBoard: midBoard + fouBoard] + parent1[midBoard + fouBoard:];
            newVillage.append(
                {
                    's': children1 + children3
                }
            );
            newVillage.append(
                {
                    's': children1 + children4
                }
            );
            newVillage.append(
                {
                    's': children2 + children3
                }
            );
            newVillage.append(
                {
                    's': children2 + children4
                }
            );
        return newVillage;
    
    def mutation (self, village):
        for v in village:
            state = v['s'];
            for i in range (self.n):
                for j in range(i + 1, self.n):
                    if(state[i] == state[j]):
                        state[j] = random.randrange(self.n);

    def fitness (self, village):
        totalFitness = 0;
        for v in village:
            v['f'] = self.env.H(v['s']);
            totalFitness += v['f'];
        #Ordena el arreglo por fitness
        village.sort(key=lambda e : e['f']);
        village.append(totalFitness);
