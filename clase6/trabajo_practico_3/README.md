# TP3: Detector de SPAM

Uno de los problemas más comunes en la clasificación es la detección de correos electrónicos SPAM. Uno de los primeros 
modelos utilizados para abordar este problema fue el clasificador de Bayes ingenuo. La detección de SPAM es un problema 
persistente en el mundo digital, ya que los spammers continúan adaptando sus estrategias para eludir los filtros de 
correo no deseado. Además del clasificador de Bayes ingenuo, se han desarrollado y utilizado una variedad de técnicas 
más avanzadas en la detección de SPAM, que incluyen algoritmos de aprendizaje automático, redes neuronales y métodos 
basados en reglas.

En este trabajo práctico, utilizaremos un conjunto de datos que consta de 4601 observaciones de correos electrónicos, 
de los cuales 2788 son correos legítimos y 1813 son correos SPAM. Dado que el contenido de los correos electrónicos es 
un tipo de dato no estructurado, es necesario procesarlo de alguna manera. Para este conjunto de datos, ya se ha 
aplicado un procesamiento típico en el Procesamiento del Lenguaje Natural (NLP), que consiste en contar la frecuencia 
de palabras observadas en los correos.

El procesamiento de lenguaje natural (NLP) desempeña un papel fundamental en la detección de SPAM, ya que permite 
analizar el contenido de los correos electrónicos y extraer características relevantes para la clasificación. Además 
de contar la frecuencia de palabras, se pueden utilizar técnicas más sofisticadas, como la extracción de 
características semánticas y el análisis de sentimientos, para mejorar la precisión de los modelos de detección de SPAM.

En este proceso, se cuenta la cantidad de ocurrencias de cada palabra en los diferentes correos.

![spam counter](./spam.png)

Con el fin de preservar la privacidad de los mensajes, la frecuencia de palabras se encuentra normalizada. El conjunto 
de datos está compuesto por 54 columnas de atributos que se denominan:

- `word_freq_XXXX`: Donde `XXXX` es la palabra o símbolo. Los valores son enteros que van de 0 a 20k.

Además, hay una columna adicional llamada `spam`, que es 1 si el correo es SPAM o 0 si no lo es.

Los clasificadores de Bayes ingenuos fueron los primeros filtros utilizados por las aplicaciones de correo electrónico, 
basados en este principio de palabras. La idea es que, partiendo de un dato a priori sobre la probabilidad de que un 
correo sea SPAM o no, ciertas palabras nos indicarán que la probabilidad a posteriori, dadas esas palabras, es más 
probable que el correo sea SPAM o no.

Para este trabajo práctico, se proporciona una notebook (`ayuda.ipynb`) con la lectura del conjunto de datos, la 
separación de los datos, entre otras ayudas para resolverlo.

## Tareas y preguntas a resolver:

1. ¿Cuáles son las 10 palabras más encontradas en correos con SPAM y en correos No SPAM? ¿Hay palabras en común? 
¿Algunas llaman la atención?
2. Separe el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba (70% y 30% respectivamente).
3. UUtilizando un clasificador de Bayes ingenuo, entrene con el conjunto de entrenamiento.
4. Utilizando un clasificador de Regresión Logística, entrene con el conjunto de entrenamiento (en este caso, 
normalice los datos).
5. Calcule la matriz de confusión del conjunto de evaluación para ambos modelos. ¿Qué tipo de error comete más cada 
modelo? ¿Cuál de los dos tipos de error crees que es más importante para este problema?
6. Calcule la precisión y la recuperación de ambos modelos. Para cada métrica, ¿cuál es el mejor modelo? ¿Cómo se 
relacionan estas métricas con los tipos de errores analizados en el punto anterior? Expanda su respuesta.
7. Obtenga la curva ROC y el AUC (Área Bajo la Curva ROC) de ambos modelos.

El entregable consiste en uno o más archivos de notebook `ipynb` con las respuestas. Aunque se da libertad para usar 
otros tipos de entregables, es importante incluir tanto el código de lo resuelto como las respuestas. Pueden enviar 
todo mediante el formulario de entrega o proporcionar un enlace a un repositorio público (GitHub o GitLab) con el 
contenido. **No olviden especificar los autores del TP en el entregable**.

Para resolver este TP, son libres de utilizar los recursos que consideren necesarios. Pueden hacerlo en cualquier 
lenguaje de programación y de la forma que consideren apropiada.

### Enlace al formulario de Google para la entrega del TP3: 

El informe debe enviarse mediante el siguiente formulario: 
[https://forms.gle/MaXE9vwVaYLRsUCJA](https://forms.gle/MaXE9vwVaYLRsUCJA). La fecha límite de entrega es el 21/04/2024 
a las 23:59.
