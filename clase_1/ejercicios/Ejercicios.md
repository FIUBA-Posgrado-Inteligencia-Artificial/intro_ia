# Guía de Ejercicios
Ejercicios de aplicación de NumPy. Varios de ellos se utilizarán más adelante en la materia como parte de problemas más grandes.

#### Ejecicio #1:    Operaciones Matriciales
Dada una matriz en formato numpy array, donde cada fila de la matriz representa un vector matemático: 
* Computar las normas l0, l1, l2, l-infinito
    * l0: número de elementos diferentes a cero en el vector
    * l1-l2: 
    ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BOrange%7D%20%5Cleft%20%5C%7C%20x%20%5Cright%20%5C%7C_%7Bp%7D%20%3D%20%5Cleft%20%28%20%5Csum_%7B1%7D%5E%7Bn%7D%20%5Cleft%20%7C%20x_%7Bi%7D%20%5Cright%20%7C%5Ep%20%5Cright%20%29%5E%7B%5Ctfrac%7B1%7D%7Bp%7D%7D%7D)
    * l-infinito:
     ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BOrange%7D%20%5Cleft%20%5C%7C%20x%20%5Cright%20%5C%7C_%7Bp%7D%20%3D%20%5Cleft%20%28%20%5Csum_%7B1%7D%5E%7Bn%7D%20%5Cleft%20%7C%20x_%7Bi%7D%20%5Cright%20%7C%5Ep%20%5Cright%20%29%5E%7B%5Ctfrac%7B1%7D%7Bp%7D%7D%7D)
#### Ejecicio #2:    Sorting
Dada una matriz en formato numpy array, donde cada fila de la matriz representa un vector matemático, se requiere computar la norma l2 de cada vector.
Una vez obtenida la norma, se debe ordenar las mísmas de mayor a menor. Finalmente, obtener la matriz original ordenada por fila según la norma l2.

_Todas las operaciones debe ser vectorizadas._

#### Ejecicio #3:    Indexing
El objetivo es construir un índice para identificadores de usuarios, es decir _id2idx_ e _idx2id_.
Para ello crear una clase, donde el índice se genere en el constructor. Armar métodos _get_users_id_ y _get_users_idx_.

* Identificadores de usuarios : users_id = [15, 12, 14, 10, 1, 2, 1]
* Índice de usuarios : users_id = [0, 1, 2, 3, 4, 5, 4]
```
id2idx =  [-1     4     5    -1    -1    -1     -1    -1    -1    -1     3     -1      1    -1     2     0]
          [ 0     1     2     3     4     5      6     7     8     9    10     11     12    13    14    15]

id2idx[15] -> 0 ; id2idx[12] -> 1 ; id2idx[3] -> -1
idx2id[0] -> 15 ; idx2id[4] -> 1
```

#### Ejecicio #4:    Precision, Recall, Accuracy
En los problemas de clasificación, se cuenta con dos arreglos, la **verdad** (ground truth) y la **predicción** (prediction). 
Cada elemento de los arreglos puede tomar dos valores: _True_ (representado por 1) y _False_ (representado por 0). 
Por lo tanto, se pueden definir cuatro variables:
* True Positive (TP): la verdad es 1 y la predicción es 1.
* True Negative (TN): la verdad es 0 y la predicción es 0.
* False Negative (FN): la verdad es 1 y la predicción es 0.
* False Positive (FP): la verdad es 0 y la predicción es 1.

A partir de esas cuatro variables, se definen las siguientes métricas:
* Precision = TP / (TP + FP)
* Recall = TP / (TP + FN)
* Accuracy = (TP + TN) / (TP + TN + FP + FN)

Para los siguientes arreglos, representando la **verdad** y la **predicción**,
calcular las métricas anteriores con operaciones vectorizadas en NumPy.
* truth = [1,1,0,1,1,1,0,0,0,1]
* prediction = [1,1,1,1,0,0,1,1,0,0]

#### Ejecicio #5:    Average Query Precision
En information retrieval o search engines, en general contamos con queries “q” y para cada “q” una lista de documentos que son verdaderamente relevantes. 
Para evaluar un search engine, es común utilizar la métrica **average query precision**.
Tomando de referencia el siguiente ejemplo, calcular la métrica con NumPy utilizando operaciones vectorizadas.
```
q_id =             [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
predicted_rank =   [0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3]
truth_relevance =  [T, F, T, F, T, T, T, F, F, F, F, F, T, F, F, T] 
```
* Precision para q_id 1 = 2 / 4
* Precision para q_id 2 = 3 / 3
* Precision para q_id 3 = 0 / 5
* Precision para q_id 4 = 2 / 4

**_average query precision_** = ((2/4) + (3/3) + (0/5) + (2/4)) / 4

#### Ejecicio #6:    Distancia a Centroides
Dada una nube de puntos _X_ y centroides _C_, obtener la distancia entre
cada vector _X_ y los centroides utilizando operaciones vectorizadas y broadcasting en NumPy.
Utilizar como referencia los siguientes valores:
```
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C = [[1, 0, 0], [0, 1, 1]]   
```
#### Ejecicio #7:    Etiquetar Cluster
Obtener para cada fila en _X_, el índice de la fila en _C_ con distancia euclídea más pequeña. 
Es decir, para cada fila en _X_, determinar a qué cluster pertenece en C.
_Hint_: usar np.argmin.

#### Ejercicio #8:   Implementación Básica de K-means
K-means es uno de los algoritmos más básicos en Machine Learning no supervisado.
Es un algoritmo de clusterización, que agrupa datos que comparten características similares.
Recordemos que entendemos datos como _n_ realizaciones del vector aleatorio _X_.

El algoritmo funciona de la siguiente manera:
1. El usuario selecciona la cantidad de clusters a crear _n_.
2. Se seleccionan _n_ elementos aleatorios de _X_ como posiciones iniciales del los centroides _C_.
3. Se calcula la distancia entre todos los puntos en _X_ y todos los puntos en _C_.
4. Para cada punto en _X_ se selecciona el centroide más cercano de _C_.
5. Se recalculan los centroides _C_ a partir de usar las filas de _X_ que pertenecen a cada centroide. 
6. Se itera entre 3 y 5 una cantidad fija de veces o hasta que la posición de los centroides no cambie dada una tolerancia.

Se debe por lo tanto implementar la función k_means(X, n) de manera tal que, al finalizar, devuelva la posición de los centroides
y a qué cluster pertenece cada fila de _X_. 

_Hint_: para (2) utilizar funciones de np.random, para (3) y (4) usar los ejercicios anteriores, 
para (5) es válido utilizar un for. Iterar 10 veces entre (3) y (5).  

#### Ejercicio #9:   Computar Métricas con \_\_call__ :house:
En problemas de machine learning, es muy común que para cada predicción que obtenemos en nuestro dataset de verificacion y evaluacion, almacenemos en arreglos de numpy el resultado de dicha predicción, junto con el valor verdadero y parámetros auxiliares (como el ranking de la predicción y el query id). 

Luego de obtener todas las predicciones, podemos utilizar la información almacenada en los arreglos de numpy, para calcular todas las métricas que queremos medir en nuestro sistema. 

Una buena práctica para implementar esto en Python, es crear clases que hereden de una clase Metric “base” y que cada métrica implemente el método \_\_call__.

Utilizar herencia, operador \_\_call__ y _kwargs_, para escribir un programa que permita calcular todas las métricas de los ejercicios anteriores mediante un for.

#### Ejercicio #10:   Dataset a NumPy Estructurado - Patrón de Diseño Singleton :house:
Para éste ejercicio vamos a descargar un dataset de Kaggle. Es recomendable que se creen una cuenta porque es un lugar de donde potencialmente vamos a descargar muchos recursos.

Pueden descargar el dataset desde [aquí](https://www.kaggle.com/rounakbanik/the-movies-dataset/data?select=ratings.csv).

El objetivo del ejercicio es crear una clase que permita realizar las siguientes funciones sobre el dataset:
* Crear la estructura de un structured numpy array para el dataset.
* Leer el csv, almacenar la información en el array estructurado.
* Guardar el array estructurado en formato .pkl.
* Crear una instancia singleton del array estructurado (utilizando \_\_new__ e \_\_init__).
* Al crear la instancia, si se encuentra el .pkl cargar desde el pkl. Si el .pkl no está, comenzar por transformar el .csv en .pkl y luego levantar la información.
* Encontrar una forma de optimizar la operación usando generators [opcional].
 
