from IA import Agent, Environment
import statistics
#Método que muestra los resultados
def __showResults(states, L, env):
    print("Se han generado "+str(states)+" estados posibles.");
    print("\nLos pasos a seguir son: ", end="");
    L.show();
    #Muestra en entorno
    env.printEnvironment();

#Arreglo que guardará los estados generados en cada caso.
aBFS = [];
aDFS =[];
aUS = [];
print("\nEjecutando...", end="");

#Ejecuta el argoritmo 30 veces en escenarios distintos
for _ in range (30):
    #Genera el agente y el entorno
    E = Environment();
    A = Agent(E);
    #
    #####    BFS
    _, statesBFS, MovementsBFS = A.BFS();
    #__showResults(statesBFS, MovementsBFS, E);
    aBFS.append(statesBFS or 0); #Agrega la cantidad de estados
    
    #####    DFS
    #Genera el agente y el entorno
    E = Environment();
    A = Agent(E);
    _, statesDFS, MovementsDFS = A.DFS();
    #__showResults(statesDFS, MovementsDFS, E);
    aDFS.append(statesDFS or 0);

    #Genera el agente y el entorno
    E = Environment();
    A = Agent(E);
    _, statesUS, MovementsUS = A.US();
    #__showResults(statesUS, MovementsUS, E);
    aUS.append(statesUS or 0);
    

#Muestra los resultados
print("\n\nEstados generados en BFS: ", end="");
print(aBFS,"\n");
print("Media: ",statistics.mean(aBFS));
print("Desviación estandar:", statistics.stdev(aBFS),"\n")
print("Estados generados en DFS: ", end="");
print(aDFS,"\n");
print("Media: ", statistics.mean(aDFS));
print("Desviación estandar", statistics.stdev(aDFS),"\n")

print("Estados generados en US: ",end="");
print(aUS,"\n");
print("Media: ",statistics.mean(aUS));
print("Desviación estandar", statistics.stdev(aUS),"\n")


#Explica que significa cada cosa
#print("\n-----------------------------\n  Obstáculo: [   ]\n  Casillas exploradas:  . \n-----------------------------");