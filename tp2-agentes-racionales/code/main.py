import Environment;
import Agente;
i = 2
while i < 129:
    print("----- Tamaño: ", i, "x", i, " -----");
    j = 0.1;
    while j < 0.9:
        print("Suciedad: ", j);
        oEnviroment = Environment.Environment(i, i, j);
        oAgente = Agente.Agent(oEnviroment);

        #print("\n\nEstado inicial del tablero: ")
        #oEnviroment.printEnvironment();

        #1000 ciclos de vida
        for _ in range (1000):
            
            ## EJERCICIO C
            oAgente.doAction();

            ## EJERCICIO E
            #oAgente.doActionRandom();

        #print("Estado final del tablero: ");
        #oEnviroment.printEnvironment();
        print("\tPuntos obtenidos: ", oEnviroment.performance);
        print("\tCasillas sucias: ", oEnviroment.getPerformance());
        j *= 2;
    i *= 2;
"""
print("\nLos movimientos del agente son: \n");
for a in oAgente.getRecord():
    print(a);
"""

#print("Posición final del agente: (",oAgente.currentX,", ",oAgente.currentY,")\n");