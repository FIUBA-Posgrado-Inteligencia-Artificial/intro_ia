# Guía de Ejercicios
Ejercicios de aplicación de NumPy aplicados a Ingeniería de Features.

#### Ejecicio #1:    Calcular la inversa generalizada y simular :house:
Obtener la inversa generalizada de la función de densidad de 
probabilidad que figura en la presentación y utilizar numpy para simular n muestras.

#### Ejecicio #2:    Normalización :house:
Muchos algoritmos de Machine Learning necesitan datos de entrada centrados y normalizados. Una normalización habitual es el z-score, que implica restarle la media y dividir por el desvío a cada feature de mi dataset. 

Dado un dataset X de n muestras y m features, implementar un método en numpy para normalizar con z-score. Pueden utilizar np.mean() y np.std().

#### Ejecicio #3:    Remover filas y columnas con NaNs en un dataset :house:
Dado un dataset, hacer una función que, utilizando numpy, filtre las columnas y las filas que tienen NaNs.

#### Ejecicio #4:    Reemplazar NaNs por la media de la columna :house:
Dado un dataset, hacer una función que utilizando numpy reemplace los NaNs por la media de la columna.

#### Ejecicio #5:    Dado un dataset X separarlo en 70 / 20 / 10 :house:
Como vimos en el ejercicio integrador, en problemas de Machine Learning es fundamental que separemos los datasets de n muestras, en 3 datasets de la siguiente manera:

* Training dataset: los datos que utilizaremos para entrenar nuestros modelos. Ej: 70% de las muestras.
* Validation dataset: los datos que usamos para calcular métricas y ajustar los hiperparámetros de nuestros modelos. Ej: 20% de las muestras.
* Testing dataset: una vez que entrenamos los modelos y encontramos los hiperparámetros óptimos de los mísmos, el testing dataset se lo utiliza para computar las métricas finales de nuestros modelos y analizar cómo se comporta respecto a la generalización. Ej: 10% de las muestras.

A partir de utilizar np.random.permutation, hacer un método que dado un dataset, devuelva los 3 datasets como nuevos numpy arrays.


