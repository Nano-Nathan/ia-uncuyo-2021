# Indicaciones de cómo se encuentran estructuradas las respuestas.

El trabajo práctico se divide en 3 archivos los cuales contienen respuestas teóricas y resultados del programa, además cuenta con una carpeta donde se implementan los objetos requeridos. Dicha carpeta contiene 3 script escritos en Python los cuales se explican brevemente luego de nombrarlos:
1) **Agente.py**
2) **Environment.py**
3) **main.py**

Dentro del archivo *Agente.py* se implementa un agente inteligente el cual simula una aspiradora, éste objeto cuenta con:
- 6 métodos que realizan las acciones posibles (moverse a la derecha, izquierda, arriba, abajo y no hacer nada). Al ejecutarse dichos métodos, guardan en un registro lo que se realiza y le avisa al entorno que el agente se movió de posición.
- 2 métodos llamados *"doAction"* y *"doActionRandom"* los cuales se describen a continuación:
    - ***doAction***: Realiza los pasos de un *"Agente Reflexivo Simple"*. Escanéa el entorno gracias al método *perspective*, interpreta los datos con el método *think* y realiza las acciones correspondientes. Se implementa un algoritmo simple para que el agente intente limpiar de la forma más ordenada que se me ocurrió. Como el agente comienza en una posición random del tablero, se toman las acciones correspondientes para llevarlo a la posición (0,0) y luego que comience analizando esa fila. Al momento de no poder seguir avanzando en esa drección, baja a la siguiente fila y se mueve hacia la izquierda para realizar lo mismo hasta analizar todo el tablero.
    - ***doActionRandom***: Este método responde al *Ejercicio E*, durante la vida del agente (1.000 acciones) se toman desiciones aleatorias para moverse, si llega a una casilla que se encuentra sucia, la limpia y sigue con la eleccion aleatoria. Si el agente no puede moverse en la dirección seleccionada (por salirse del tablero), no realiza ninguna acción.

El archivo *Environment.py* implementa el entorno donde se encuentra el agente ya especificado. El método a resaltar es *_initBoard*. Este inicializa el tablero creando un arreglo de 10 posiciones, el cual contiene tantos verdaderos como 10 veces el porcentaje de suciedad (*dirt_rate*). Por ejemplo: Si *dirt_rate* es 0.4, el arreglo contendrá 4 valores verdaderos y 6 falsos. Se selecciona un valor al azar de dicho arreglo, obteniendo así cierta probabilidad (pasada por parámetro) de que la casilla donde se encuantra el bucle esté sucia.

Para finalizar, queda el archivo *main.py* el cual como en todo programa ejecuta el flujo principal del programa. Dicho scrip realiza la ejecución del agente en todas las ocaciones que se indican dentro del trabajo práctico. Tableros de tamaño 2x2, 4x4, 8x8, 16x16, 32x32, 64x64 y 128x128 con una probabilidad de suciedad del 0.1, 0.2, 0.4 y 0.8. Se nota en el bucle que comienza en la línea 16 que se encuentran las opciones para ejecutar un agente programado o uno con movimientos aleatorios.