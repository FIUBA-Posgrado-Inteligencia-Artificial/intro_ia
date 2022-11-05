# Guía de Ejercicios
Ejercicios de aplicación de NumPy aplicados a Ingeniería de Features y Regresión Lineal.

#### Ejecicio #1:    Normalización
Muchos algoritmos de Machine Learning necesitan datos de entrada centrados y normalizados. Una normalización habitual es el z-score, que implica restarle la media y dividir por el desvío a cada feature de mi dataset. 

Dado un dataset X de n muestras y m features, implementar un método en numpy para normalizar con z-score. Pueden utilizar np.mean() y np.std().

#### Ejecicio #2:    Remover filas y columnas con NaNs en un dataset
Dado un dataset, hacer una función que, utilizando numpy, filtre las columnas y las filas que tienen NaNs.

#### Ejecicio #3:    Reemplazar NaNs por la media de la columna
Dado un dataset, hacer una función que utilizando numpy reemplace los NaNs por la media de la columna.

#### Ejecicio #4:    Dado un dataset X separarlo en 70 / 20 / 10
Como vimos en el ejercicio integrador, en problemas de Machine Learning es fundamental que separemos los datasets de n muestras, en 3 datasets de la siguiente manera:

* Training dataset: los datos que utilizaremos para entrenar nuestros modelos. Ej: 70% de las muestras.
* Validation dataset: los datos que usamos para calcular métricas y ajustar los hiperparámetros de nuestros modelos. Ej: 20% de las muestras.
* Testing dataset: una vez que entrenamos los modelos y encontramos los hiperparámetros óptimos de los mísmos, el testing dataset se lo utiliza para computar las métricas finales de nuestros modelos y analizar cómo se comporta respecto a la generalización. Ej: 10% de las muestras.

A partir de utilizar np.random.permutation, hacer un método que dado un dataset, devuelva los 3 datasets como nuevos numpy arrays.

#### Ejercicio #5:   A partir del dataset de consigna, aplicar los conceptos de regresión lineal.
1. Armar una clase para cargar el [dataset](data/income.csv) en un ndarray estructurado, tal como se realizó en el ejercicio 10 de la Clase 1.
2. Incluir un método split a la clase para obtener los sets de training y test.
3. Crear una clase métrica base y una clase MSE (Error cuadrático medio) que herede de la clase base.
4. Crear una clase modelo base y clases regresión lineal y regresión afín que hereden de la primera. Usar los conocimientos teóricos vistos en clase.
5. Hacer un fit de las regresiones con los datos de entrenamiento.
6. Hacer un predict sobre los datos de test y reportar el MSE en cada caso.
7. Graficar la curva obtenida.

