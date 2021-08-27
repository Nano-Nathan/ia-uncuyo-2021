# Al un total de 30 veces cada algoritmo en un escenario aleatorio, se obtienen los siguientes resultados:

### Búsqueda en anchura (BFS)

Estados generados: [5851, 1790, 4435, 4462, 6022, 6960, 5230, 1898, 7893, 1018, 8018, 4150, 2902, 74, 4510, 1372, 3331, 4866, 4012, 6345, 4321, 5398, 3004, 6978, 3812, 3363, 4578, 4953, 0, 3325]

Media: 3977,2000

Desviación estandar: 1765,7910

### Búsqueda en profundidad limitada(DFS)
Estados generados: [7932, 1427, 1409, 7832, 3918, 7643, 2492, 3419, 7754, 7163, 2758, 1635, 2474, 7366, 7306, 4071, 2193, 4112, 6638, 8016, 7854, 2966, 5895, 6395, 4623, 2776, 1937, 7208, 1386, 7128]

Media: 4857,5333

Desviación estandar: 2476,0861

### Búsqueda de costo uniforme(US)
Estados generados: [1867, 5383, 1159, 2204, 7783, 2191, 7590, 5250, 7014, 114, 7294, 465, 3647, 5129, 7865, 4849, 5609, 7940, 7674, 6525, 4603, 7453, 1562, 1435, 1197, 4965, 7654, 6950, 6729, 7569]

Media: 4922,3000

Desviación estandar: 2643,7185

<br></br>

---

<br></br>

Si bien los 3 algoritmos logran alcanzar el objetivo, creo que el mejor en este caso es el BFS.

Por una parte, DFS busca caminos en profundidad generando menos estados de los que podría generar BFS, pero sin la seguridad de encontrar el camino más corto. 
Con respecto a la búsqueda uniforme, actua similar al anterior algoritmo con la diferencia que si encuentra el camino y se verifica que el siguiente nodo tiene menor costo, comienza a recorrer desde allí, haciendo esto se generan muchos más estados que en el aterior, pero menos que en BFS. 
Hablando de este último al recorrer el grafo por niveles, puede encontrar el camino más corto sin tener que navegar por todo el subárbol pero generando la mayor cantidad de estados si el camino es largo. 

