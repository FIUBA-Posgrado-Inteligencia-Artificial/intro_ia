# Guía de Ejercicios
Ejercicios de aplicación de NumPy aplicados a K-means, PCA e Ingeniería de Features.

#### Ejecicio #1:    Datasets Sintéticos
En problemas de Machine Learning es muy importante contar con el dataset correcto. Pero muchas veces, el dataset nos es fácil de conseguir o el equipo de data engineers aún lo está generado.

Una manera sencilla de generar datos para probar soluciones de Machine Learning es crear datasets sintéticos. Por ejemplo, es simple crear datasets con grados de clusterización variables y probar cómo se comportan nuestros algoritmos en diferentes escenarios. 

Objetivo: Utilizar numpy para crear datos clusterizados A/B en 4 dimensiones.

Hint:
* Definir una matriz con centroides [1,0,0,0] y [0,1,0,0]
* Utilizar una constante para separar o alejar los centroides entre sí.
* Utilizar np.repeat para crear n/2 muestras de cada centroide.
* Sumar a cada centroide un vector aleatorio normal i.i.d. con media 0 y desvío (np.random.normal).
* Armar un arreglo que tenga n enteros indicando si la muestra pertenece a A o a B. 


#### Ejecicio #2:    Dado un dataset X, calcular PCA para reducir dimensión.
Siguiendo los pasos vistos en la teoría, se requiere utilizar numpy para calcular PCA del dataset de entrada X, utilizando la componente más importantes.

X = np.array( [ [0.8, 0.7] , [0.1, -0.1] ] )

Al finalizar la implementación en numpy, corroborar obtener los mismos resultados que utilizando el código de la librería scikit-learn. Escribir un test para comparar las matrices.


_Todas las operaciones debe ser vectorizadas._

#### Ejecicio #3:    Calcular la inversa generalizada y simular :house:
Obtener la inversa generalizada de la función de densidad de 
probabilidad que figura en la presentación y utilizar numpy para simular n muestras.

#### Ejecicio #4:    Normalización :house:
Muchos algoritmos de Machine Learning necesitan datos de entrada centrados y normalizados. Una normalización habitual es el z-score, que implica restarle la media y dividir por el desvío a cada feature de mi dataset. 

Dado un dataset X de n muestras y m features, implementar un método en numpy para normalizar con z-score. Pueden utilizar np.mean() y np.std().


#### Ejecicio #5:    Remover filas y columnas con NaNs en un dataset :house:
Dado un dataset, hacer una función que, utilizando numpy, filtre las columnas y las filas que tienen NaNs.

#### Ejecicio #6:    Reemplazar NaNs por la media de la columna :house:
Dado un dataset, hacer una función que utilizando numpy reemplace los NaNs por la media de la columna.

#### Ejecicio #7:    Dado un dataset X separarlo en 70 / 20 / 10 :house:
Como vimos en el ejercicio integrador, en problemas de Machine Learning es fundamental que separemos los datasets de n muestras, en 3 datasets de la siguiente manera:

* Training dataset: los datos que utilizaremos para entrenar nuestros modelos. Ej: 70% de las muestras.
* Validation dataset: los datos que usamos para calcular métricas y ajustar los hiperparámetros de nuestros modelos. Ej: 20% de las muestras.
* Testing dataset: una vez que entrenamos los modelos y encontramos los hiperparámetros óptimos de los mísmos, el testing dataset se lo utiliza para computar las métricas finales de nuestros modelos y analizar cómo se comporta respecto a la generalización. Ej: 10% de las muestras.

A partir de utilizar np.random.permutation, hacer un método que dado un dataset, devuelva los 3 datasets como nuevos numpy arrays.


#### Ejercicio #8:   Integrador Clase #1 y Clase #2
Aplicar todo lo visto en clase a un ejercicio de reducción de dimensionalidad y clusterización básico.

1. Utilizar un dataset de su preferencia, puede ser de su proyecto final u otro.
2. Cambiar algunos puntos de manera aleatoria y agregar NaN (0.1% del dataset).
3. Guardar el dataset en un .pkl
4. Cargar el dataset con Numpy desde el .pkl
5. Completar NaN con la media de cada feature.
6. Calcular la media y el desvío de cada feature con funciones numpy vectorizadas.
7. Aplicar PCA al dataset reduciendo a M dimensiones.
    * Analizar la contribución de cada componente.
    * Realizar un scree plot.
    * Graficar el cluster en 2 y 3 dimensiones.
    * A través de análisis estadísticos, sacar conclusiones respecto de los resultados de PCA.
8. Hacer la clusterización con el k-means desarrollado en clase. 
9. Volver a graficar el cluster con lo obtenido en (8) y comparar resultados con (7).
