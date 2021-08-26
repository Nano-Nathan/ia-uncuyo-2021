from Agente import Agent
from Environment import Environment

#Arreglo que guardará los estados generados en cada caso.
aBFS = [];
print("\nEjecutando...\n");
#Ejecuta el argoritmo 30 veces en escenarios distintos
for _ in range (30):
    #Genera el agente y el entorno
    E = Environment();
    A = Agent(E);
    #Obtiene los resultados de BFS
    _, states, Movements = A.BFS();
    #print("Se han generado "+str(states)+" estados posibles.");
    #print("\nLos pasos a seguir son: ", end="");
    #Movements.show();
    aBFS.append(states or 0);
    #Muestra en entorno
    #E.printEnvironment();

#Muestra los resultados
print("Estados generados en BFS: ");
print(aBFS,"\n");
#Explica que significa cada cosa
#print("\n-----------------------------\n  Obstáculo: [   ]\n  Casillas exploradas:  . \n-----------------------------");