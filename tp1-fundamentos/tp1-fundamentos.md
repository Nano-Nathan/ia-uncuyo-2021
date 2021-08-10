# IA débil: ¿Pueden las máquinas actuar con inteligencia?
 
**[Alan Turing][0]** en su famoso artículo *[Computing Machinery and Intelligence][1]* sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si las máquinas pueden aprobar un test de inteligencia conductiva (*[Test de Turing][2]*). El *test de turing* consiste en una conversación entre un *"ChatBot"* y un *"Interlocutor"* la cual tiene una duración de 5 minutos. El *Interlocutor* debe averiguar si se está comunicando con un programa o una persona, si la IA engaña al usuario en cuestión un 30% del tiempo, ésta pasará la prueba.
 
Turing también examinó una gran gama de posibles objeciones ante la posibilidad de las máquinas inteligentes, se mencionan algunas a continuación.
 
### El argumento de incapacidad.
 
Este argumento afirma que ***una máquina nunca puede hacer X***, siendo X las siguientes acciones:
 
> *"Ser amable, tener recursos, ser guapo, ser simpático, tener iniciativas, tener sentido del humor, distinguir lo correcto de lo erróneo, cometer errores, enamorarse, disfrutar de las fresas con nata, hacer que otra persona también se enamore, aprender de la experiencia, utilizar palabras de forma adecuada, ser el tema de su propio pensamiento, tener tanta diversidad de comportamientos como el hombre, hacer algo realmente nuevo."*
 
Actualmente las computadoras hacen muchísimas cosas que anteriormente eran solo del dominio humano. Como por ejemplo, jugar al ajedrez, a las damas, al fifa y a muchos juegos más, inspeccionan piezas de las líneas de producción, comprueban la ortografía en los procesadores de texto, conducen coches, diagnostican enfermedades, y hacen otras cientos de tareas tan bien o mejor que los hombres. Han hecho pequeños pero significativos descubrimientos, en Astronomía, Matemáticas, Química, Mineralogía, Biología, Informática y otros campos que necesitan rendimiento a nivel de experto.
 
Sin embargo, a pesar de todo lo que hoy en día se ha conseguido programar en las computadoras, estas no son capaces de utilizar la intuición ni el entendimiento humano. También es cierto que existen muchas tareas donde las computadoras no sobresalen, incluido el *[Test de Turing][2]*.
 
### La objeción matemática
 
Ciertas cuestiones matemáticas no pueden ser respondidas por sistemas formales concretos. El *[teorema de la incompletitud de Gödel][3]* es el ejemplo más conocido en este respecto. En resumen, el teorema dice lo siguiente:
> Para cualquier sistema axiomático formal **F** lo suficientemente potente como para realizar cálculos aritméticos, es posible construir una `sentencia Gödel` **G(F)** con las siguientes propiedades:
> - *G(F) es una sentencia de F, pero no se puede probar dentro de F.*
> - *Si F es consistente, entonces G(F) es verdadero.*
 
Filósofos han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, es decir no pueden establecer la verdad de su propia `sentencia Gödel`, mientras que los hombres no tienen dicha limitación. Como es de esperarse esta afirmación tiene problemas, se comentan algunos a continuación.
 
1) El teorema aplica sólo a sistemas formales que son lo suficientemente potentes como para realizar operaciones aritméticas, incluyendo la máquina de Turing. La afirmación, en parte, se basa en que las computadoras son máquinas de Turing, una buena aproximación pero no del todo cierta. Aunque las computadoras sean finitas, las máquinas de Turing no lo son, y cualquier computadora se puede describir como un sistema muy grande en lógica proposicional, la cual no está sujeta al teorema.
2) Dando un ejemplo matemático, una persona jamás podría calcular la suma de 10 billones de números de 10 dígitos, en cambio una computadora podría hacerlo en segundos. A pesar de eso, no lo vemos como una limitación fundamental en la habilidad de pensar del hombre. También, durante miles de años los hombres se han comportado de manera inteligente sin la existencia de las máquinas, notando así que el razonamiento matemático no tenga más que una función secundaria en lo que implica *ser inteligente*.
3) Aunque reconozcamos que las computadoras tienen limitaciones sobre lo que pueden demostrar, no existen evidencias de que los hombres sean inmunes a esas limitaciones. Es muy sencillo demostrar con rigor que un sistema formal no puede hacer X y afirmar que los hombres pueden hacer X utilizando sus propios métodos informales, sin dar ninguna evidencia al respecto. Pero es imposible demostrar que los hombres no están sujetos al teorema, porque cualquier prueba rigurosa contendría una formalización del talento humano, declarado como no formalizable. De manera que nos quedamos con el llamamiento a la intuición de que los hombres, de alguna forma, pueden realizar hazañas sobrehumanas de comprensión matemática.

### El argumento de la informalidad

Esta afirmación consiste en que el comportamiento humano es demasiado complejo para poder captarse mediante un conjunto de reglas y que debido a las computadoras deben seguirlo ya que no son capaces de generar un comportamiento tan inteligente como el de los hombres. En IA la incapacidad de capturarlo todo en un conjunto de reglas lógicas se denomina ***"Problema de cualificación"***.
 
En 1986 los hermanos *[Hubert][4]* y *[Stuart][5] Dreyfus* proponen un proceso de adquisición de pericia en cinco etapas, comenzando con un procesamiento basado en reglas y terminando con la habilidad de seleccionar las respuestas correctas instantáneamente. Al realizar esta propuesta, pasan de ser críticos a ser teóricos de la IA, ya que proponen una arquitectura de *[redes neuronales][6]* organizadas en una biblioteca de casos extensa, pero señalan algunos problemas. Entre estos se incluyen los siguientes:
 
1) Afirman que no se sabe cómo incorporar el conocimiento básico en el proceso de aprendizaje de las redes neuronales. Aunque existen técnicas para utilizar el conocimiento anterior (algoritmos de aprendizaje), estas dependen de la disponibilidad previa de conocimiento de forma explícita, algo que los hermanos niegan vigorosamente. Bajo nuestro punto de vista, esta es una buena razón para realizar un rediseño serio de los modelos actuales del procesamiento neuronal de forma que puedan sacar provecho del conocimiento aprendido anteriormente.
2) El aprendizaje de redes neuronales es una forma de *[aprendizaje supervisado][7]*, que requiere la identificación anterior de las entradas relevantes y las salidas correctas. Por tanto, afirman que no puede funcionar autónomamente sin la ayuda de un entrenador humano. De hecho, el aprendizaje sin un profesor se puede conseguir mediante un *[aprendizaje no supervisado][8]* y un *[aprendizaje de refuerzo][9]*.
3) No existe una forma conocida de añadir funciones nuevas, si el conjunto actual demuestra ser inadecuado para tener en cuenta los hechos aprendidos. De hecho, métodos nuevos tales como las *[máquinas vectoriales de soporte][10]* utilizan muy bien conjuntos grandes de funciones.
4) El cerebro es capaz de dirigir sus sensores para buscar la información relevante y procesarla para extraer aspectos relevantes para la situación actual. Sin embargo, afirman que actualmente, los detalles de este mecanismo ni se entienden y ni siquiera se hipotetizan para guiar la investigación en la IA. De hecho, el campo de la visión activa, respaldado por la teoría del valor de la información tiene que ver exactamente con el problema de dirigir los sensores, y algunos robots ya han incorporado los resultados teóricos obtenidos.

# IA fuerte: ¿Pueden las máquinas pensar de verdad?

Muchos filósofos han afirmado que una máquina que pasa el Test de Turing no quiere decir que realmente esté pensando, sino que solamente es una simulación.

# La ética y los riesgos de desarrollar IA


## *Conclusión*


[Mapa mental][mapa]


[0]: https://es.wikipedia.org/wiki/Alan_Turing
[1]: https://web.archive.org/web/20080702224846/http://loebner.net/Prizef/TuringArticle.html
[2]: https://es.wikipedia.org/wiki/Prueba_de_Turing
[3]: https://es.wikipedia.org/wiki/Teoremas_de_incompletitud_de_G%C3%B6del
[4]: https://es.wikipedia.org/wiki/Hubert_Dreyfus
[5]: https://en.wikipedia.org/wiki/Stuart_Dreyfus
[6]: https://es.wikipedia.org/wiki/Red_neuronal_artificial
[7]: https://es.wikipedia.org/wiki/Aprendizaje_supervisado
[8]: https://es.wikipedia.org/wiki/Aprendizaje_no_supervisado
[9]: https://es.wikipedia.org/wiki/Aprendizaje_por_refuerzo
[10]: https://es.wikipedia.org/wiki/M%C3%A1quinas_de_vectores_de_soporte


[mapa]: https://www.mindomo.com/mindmap/mapa-mental-f54eaa2040cb4e189a54e19fe84b8a11

