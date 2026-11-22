# Evaluación práctica - Módulo 5 - Swiss Dataset

## 📋 Descripción del problema

En este ejercicio deberán entrenar y comparar distintos modelos de **regresión** para predecir la fertilidad de las provincias de Suiza, utilizando el conjunto de datos **Swiss**.

> El dataset **Swiss** es un conjunto de datos clásico, incluido en el lenguaje R, que contiene información socioeconómica y demográfica de 47 provincias de habla francesa de Suiza alrededor del año 1888. Algunas de las variables incluidas son una medida de la fertilidad, el nivel de educación, la proporción de católicos y la mortalidad infantil.

El objetivo es construir modelos de regresión capaces de predecir la variable `Fertility` a partir del resto de las variables, y analizar qué ocurre cuando agregamos muchos atributos con pocos datos.

En el notebook ya están resueltas la carga de los datos y su separación en entrenamiento y evaluación. También se les dan dos funciones de ayuda: `evaluate`, que calcula e imprime las métricas de un modelo, y `show_coefficients`, que grafica sus coeficientes.

---

## ✅ Qué deben entregar

El notebook se divide en cuatro partes. En cada una deben completar el código indicado y, donde se pide, responder una pregunta con sus palabras.

### Parte 1: Regresión lineal múltiple

- Armar un `Pipeline` con `StandardScaler` y `LinearRegression` que use los 5 atributos del dataset.
- Entrenarlo con el set de entrenamiento y evaluarlo con la función `evaluate`.

### Parte 2: Atributos polinómicos

- Armar un `Pipeline` que agregue **atributos polinómicos** de grado 2 con `PolynomialFeatures` (que llevan el modelo a 20 atributos), los escale con `StandardScaler` y aplique `LinearRegression`.
- Entrenarlo y evaluarlo con la función `evaluate`.
- **Responder la pregunta 1:** comparar el $R^2$ en entrenamiento y en evaluación, y explicar qué está pasando y por qué, teniendo en cuenta la cantidad de atributos y de observaciones de entrenamiento.

### Parte 3: Regularización

- Armar, entrenar y evaluar una **regresión de Ridge** (`RidgeCV`) y una **regresión de Lasso** (`LassoCV`) con los mismos 20 atributos, buscando el mejor valor de $\alpha$ con validación cruzada de 3 folds.
- Imprimir el valor de $\alpha$ elegido para cada modelo.
- Graficar los coeficientes de los tres modelos con 20 atributos usando la función `show_coefficients`.
- Imprimir la lista de los atributos que **conservó** Lasso (los de coeficiente distinto de cero).
- **Responder la pregunta 2:** explicar qué diferencia observan entre los coeficientes de Ridge y los de Lasso, y qué atributos conservó Lasso.

### Parte 4: Comparación de modelos y conclusiones

- Completar la tabla con el MAE, el MSE y el $R^2$ en el set de evaluación de los cuatro modelos.
- **Responder la pregunta 3:** justificar qué modelo elegirían para predecir la fertilidad, teniendo en cuenta las métricas y la complejidad de cada modelo.

---

## 🛠️ Instrucciones de Entrega

A continuación, se dejan los enlaces al notebook que deben completar para resolver el ejercicio y al dataset.

> [!IMPORTANT]
> Es **obligatorio** completar únicamente las secciones indicadas en el notebook, sin agregar contenido adicional.

🔗 **[Notebook a completar](swiss_reg.ipynb)**

📊 **[Dataset Swiss](swiss.csv)**

> [!NOTE]
> El notebook necesita el archivo `swiss.csv`, que está en esta misma carpeta.
