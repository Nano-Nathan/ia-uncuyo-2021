1. Describir en detalle una formulación CSP para el Sudoku.

    Variables: ***Position_i_j** con 0 < i < 10 y 0 < j < 10*

    Dominios: {1, 2, 3, 4, 5, 6, 7, 8, 9}

    Restriccion: Variables que se encuentren en la misma fila, columna o sub-cuadrado no pueden tener el mismo valor. 
    
        Ej: *Position_i_j != Position_k_j*

<br/>

2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=Red, V=Blue} para el problema del colorear el mapa de Australia.

    Comenzando con la asignación parcial dada en el enunciado, el estado inicial es el siguiente:

    <img src="./img/0.png"/>
    
    Si comenzamos viendo la arco-consistencia de SA con respecto a NT notamos que es incosistente, lo cual se puede corregir eliminando el color ***Verde*** de NT:

    <img src="./img/1.png"/>

    Al haber eliminado un elemento del dominio de NT, debemos revisar los vecinos. Como con WA y SA se cumple la consistencia, solo analizamos a Q y vemos que no se cumple la arco-consistencia, entonces se elimina el color ***Azul*** de Q:
    
    <img src="./img/2.png"/>

    Siguiendo el algoritmo es el momento de analizar los vecinos de Q (NT, SA y NSW). Hay consistencia con NT, con SA hay inconsistencia que se soluciona eliminando el color ***Verde*** de Q:

    <img src="./img/3.png"/>

    Para finalizar queda NSW, el cual no puede tomar los valores que tenía inicialmente ya que Q tendría una asignación parcial ***Roja*** y SA una ***Verde***.

    Q.E.D.

<br/>

3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP.

    La complejidad en el peor caso es de $O(n^2d^3)$ siendo $n$ la cantidad de variables y $d$ la cantidad de elementos pertenecientes al dominio de cada variable.

<br/>

4. AC-3 coloca de nuevo en la cola todo arco $(x_k, x_i)$ cuando cualquier valor es removido del dominio de $x_i$ incluso si cada valor de $x_k$ es consistente con los valores restantes de $x_i$. Si por cada arco $(x_k,x_i)$ se lleva cuenta del número de valores que quedan de $x_i$ que sean consistentes con $x_k$. Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O($n^2d^2$).



<br/>

5. Demostrar la correctitud del algoritmo CSP para  árboles estructurados. Para ello, demostrar: 
    1. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
    2. Argumentar por qué lo demostrado en 1. es suficiente. 
