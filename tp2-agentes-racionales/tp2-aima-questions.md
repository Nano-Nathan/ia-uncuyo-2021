## 2.10) Considere una versión modificada del entorno de vacío del ejercicio 2.8, en el que el agente recibe una penalización de un punto por cada movimiento.

#### A. ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno?

> No, ya que el agente no conoce el entorno y por ende no sabe donde se encuentran las casillas sucias. Es decir, no sabe por donde ir para hacer el camino más eficiente y sus movimientos dependeran de la implementación del mismo.

#### B. ¿Qué pasa con un agente reflexivo con estado?

> Este agente será capaz de ser mucho más eficiente que el anterior ya que tiene conocimiento de lo que ha hecho anteriormente y los datos del tablero alimpiar.

#### C. ¿Cómo cambian sus respuestas A y B si las percepciones del agente le dan el estado limpio/sucio de cada casilla del entorno?

> Con respecto a la pregunta A, podría mejorar considerablemente ya que puede ser capaz de trazar un camino donde no realice cualquier movimiento sino que solo los necesarios para terminar su labor. Si esto se realiza en el segundo caso puede tener la misma o peor performance, dependiendo lo que cueste analizar las casillas adyacentes (dato que ya se sabe por se un agente con estados).

## 2.11 Considere una versión modificada del entorno de vacío del ejercicio 2.8, en el que se desconoce la geografía del entorno, al igual que la configuración inicial del suelo.

#### A. ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno?

> No, ya que no conoce el entorno y por ende cada paso que realice deberá tener una validación previa para saber si puede o no realizarlo.

#### B. ¿Puede un agente reflexivo simple con una función de agente aleatoria superar a un agente reflexivo simple?

> No, al tener la función de agente aleatoria realiza movimientos sin sentido alguno.

#### C. ¿Puede diseñar un entorno en el que su agente asignado al azar tenga un desempeño deficiente?

> Si, puede ser un tablero donde todas las casillas se encuentren sucias. El agente se moverá hacia cualquier lado, limpiará a veces y tal vez limpie una o más veces una casilla limpia.

#### D. ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple?

> Si, un agenete reflexivo con estado puede superar a un agente reflexivo simpe ya que al conocer el entorno tiene una visión más amplia y puede tomar mejores decisiones al momento de limpiar el tablero.