# Guía de Ejercicios
Ejercicios de aplicación de NumPy aplicados a K-means y PCA.

#### Ejercicio #0: Datasets sintéticos y K-means
Consolidar los ejercicios realizados de forma grupal en clase, siguiendo las indicaciones
del [notebook](K-mean%20en%20NumPy.ipynb).

#### Ejecicio #1:    Dado un dataset X, calcular PCA para reducir dimensión.
Siguiendo los pasos vistos en la teoría y utilizando el [notebook](PCA%20en%20NumPy.ipynb) de referencia, se requiere utilizar numpy para calcular PCA del dataset de entrada X, utilizando la componente más importantes.

X = np.array( [ [0.8, 0.7] , [0.1, -0.1] ] )

Al finalizar la implementación en numpy, corroborar obtener los mismos resultados que utilizando el código de la librería scikit-learn. Escribir un test para comparar las matrices.

_Todas las operaciones debe ser vectorizadas._

#### Ejercicio #2: 
Siguiendo los ejemplos vistos en clase sobre los datasets de Human Activity Recognition y Fashion MNIST, realizar las siguientes consignas en el 
[notebook](PCA%20-%20MNIST.ipynb):

1. Aplicar PCA sobre el dataset para poder explicar el 90% de la varianza. ¿Cuántos componentes se requieren?
2. Graficar un scree plot (varianza contemplada en función del número de componentes considerados)
3. Visualizar gráficamente los primeros 5 componentes ¿Qué conclusiones se puede sacar de cada componente? [OPCIONAL].
4. Visualizar la imagen original vs. la reconstruida con los  𝑚  componentes del punto 1.
5. Graficar una matriz de correlación del dataset reducido.
6. Graficar los clusters de dígitos en 2 y 3 dimensiones usando los componentes obtenidos en PCA.
7. Aplicar K-means para clusterizar los dígitos ¿Cómo son los resultados?
8. Realizar un gráfico de inercia para obtener el número óptimo de clusters  𝑘 .
9. Analizar visualmente los límites del cluster de algún dígito y "generar" artificialmente el dígito dándole valores a los primeros dos componentes de PCA.
