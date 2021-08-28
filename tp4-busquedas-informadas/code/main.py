from typing import cast
from Agente import Agent;
from Environment import Environment;
import statistics
#Método que muestra los resultados
def __showResults(states, L, env):
    print("Se han generado "+str(states)+" estados posibles.");
    print("\nLos pasos a seguir son: ", end="");
    try:
        L.show();
    except (Exception):
        print("");
    #Muestra en entorno
    env.printEnvironment();

#Arreglo que guardará los estados generados en cada caso.
aResults = [];

#Ejecuta el argoritmo 30 veces en escenarios distintos
for _ in range (30):
    #Genera el agente y el entorno
    E = Environment();
    A = Agent(E);

    states, Movements = A.AStar();
    #__showResults(states, Movements, E);
    aResults.append(states or 0); #Agrega la cantidad de estados
    

#Muestra los resultados
print("\n\nEstados generados: ", end="");
print(aResults,"\n");
print("Media: ",statistics.mean(aResults));
print("Desviación estandar:", statistics.stdev(aResults),"\n")
