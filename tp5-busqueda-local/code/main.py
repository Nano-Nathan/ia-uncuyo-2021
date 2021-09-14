import statistics
import time
from Agent import Agent;


N = [4,8,10,12,15];
itera = 20;
limit = 250;

#Por cada tamaño del tablero
for n in N:
    states = [];
    costs = [];
    times =[];
    #Se ejecuta n veces
    for i in range (itera):
        A = Agent(n, limit);
        initTime = time.time();
        result, state, cost = A.genetic();
        #Tiempo de ejecucion
        times.append(time.time() - initTime);
        #Estados recorridos
        states.append(state);
        #Costo del estado resultado
        costs.append(cost);
    #Muestra resultados
    print("\n-------- ","Tablero de ",n, "x", n," --------");
    """#Veces que se llegó un estado optimo (porcentaje)
    print(
        "Veces que se llega a un estado óptimo: ", 
        round(
            len(
                list(
                    filter( lambda x : x == 0, costs )
                )
            ) * 100 / itera, 
            2
        ),
        "%"
    );
    #Media y desviación estandar del tiempo de ejecucion
    print("\nTiempo de ejecución: \n\tPromedio:", 
        round(statistics.mean(times), 5), "seg.\n\tDesviación estándar:",
        round(statistics.stdev(times), 5), "seg.");
    #Estados por los que pasó
    print("Estados recorridos: \n\tPromedio:", 
        round(statistics.mean(states), 2), "\n\tDesviación estándar:",
        round(statistics.stdev(states), 2));"""
    print("Estados:");
    for e in states:
        print (e);
    print("tiempos");
    for t in times:
        print(round(t, 5));