# Clase 5 - Regresión

<div align="center">
  <img src="content/img/fiuba.png" alt="FIUBA Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

> [!NOTE]
> **Nota sobre este documento:** Este archivo sirve como resumen estructurado de los contenidos de la clase. Algunos recursos mencionados (como las evaluaciones, los foros y los videos de las clases grabadas) están alojados exclusivamente en el aula virtual y no se incluyen directamente en este repositorio. Dichos elementos están marcados con el símbolo 🔒.

## Materiales obligatorios

Comenzamos a explorar modelos de aprendizaje supervisado, iniciando con problemas de regresión y, particularmente, con el modelo de **regresión lineal**:

- 📺 Clase 5.1 - Regresión lineal (Video) 🔒 *(Solo en Campus Virtual)*

En el video anterior, vimos cómo se pueden obtener las ecuaciones normales basándonos en la minimización de los residuos al cuadrado. Sin embargo, también es posible obtenerlas mediante la maximización de la verosimilitud:

- 📘 [Obtención de ecuaciones normales mediante máxima verosimilitud](./content/ecuaciones_normales_maxima_verosimilitud.md)

Ahora veremos cómo seleccionar los atributos para encontrar el mejor modelo de regresión lineal. Además, exploraremos dos variantes de este modelo, la **regresión de Ridge** y la **regresión de Lasso**, que incluyen una componente de regularización:

- 📺 Clase 5.2 - Construcción de un modelo y regularización (Video) 🔒 *(Solo en Campus Virtual)*

En el último video vimos el **Criterio de Información de Akaike (AIC)** y el **Criterio de Información Bayesiano (BIC)**, los cuales se utilizan para seleccionar modelos. En ambos criterios aparece la **verosimilitud**. Ahora que ya sabemos cómo se calcula la verosimilitud para el caso de la regresión lineal, podemos obtener ambos índices:

- 📘 [Obtención de AIC y BIC para regresión lineal](./content/aic_bic_regresion_lineal.md)

Como material de apoyo, encontrarán a continuación el **material teórico** y la **presentación en formato HTML** utilizados durante esta clase.

- 📘 [Teoría clase 5](./content/teoria/README.md)
- 🌐 [Versión presentación html](./content/teoria/clase5.html)

> [!NOTE]
> **Aclaración sobre la presentación:** Para visualizar correctamente la versión HTML animada, es necesario descargar el archivo *clase5.html* (junto con la carpeta *img*) a tu computadora y abrirlo con cualquier navegador web (Chrome, Firefox, Edge, etc.), ya que GitHub no previsualiza este tipo de formato. Las fórmulas se dibujan con una librería que se descarga de internet, así que la computadora tiene que estar conectada.

> [!NOTE]
> **Aclaración sobre los videos:** En los videos, al $R^2$ lo llamamos *coeficiente de Pearson*. El nombre correcto es **coeficiente de determinación**, que es el que usamos en la teoría y en las notebooks. El coeficiente de Pearson es la correlación $r$ entre dos variables; en la regresión lineal simple se cumple que $R^2 = r^2$.

### Ejemplos prácticos

Con los conceptos estudiados, exploraremos algunas aplicaciones. Comencemos con un caso de **regresión simple**, que consiste en determinar la relación entre la concentración de un determinado fármaco en el torrente sanguíneo y el tiempo transcurrido desde su administración.

- 📓 [1 - Regresión lineal simple - Jupyter Notebook](./content/jupyter_notebooks/01%20-%20regresion%20simple.ipynb)

Ahora que los conceptos están más claros y hemos presentado los principales elementos que utilizaremos de **scikit-learn**, veamos un ejemplo de **regresión lineal múltiple**. Para ello, utilizaremos un famoso conjunto de datos de 50 startups:

- 📓 [2 - Regresión lineal múltiple - Jupyter Notebook](./content/jupyter_notebooks/02%20-%20regresion%20multiple.ipynb)

Obtuvimos nuestro modelo de regresión múltiple, el cual tuvo un rendimiento muy bueno. Ahora surge la pregunta: ¿podemos obtener un modelo igual o similar utilizando menos atributos? Nuestro análisis estadístico inicial sugiere que algunos atributos podrían estar de más. Un modelo más simple, con menos atributos, es mejor porque reduce la complejidad del modelo, mejora la interpretabilidad, disminuye el riesgo de sobreajuste y puede resultar en un modelo más eficiente.

En la siguiente notebook, realizaremos una selección de modelos utilizando el **criterio de información de Akaike (AIC)**:

- 📓 [3 - Selección de modelo - Jupyter Notebook](./content/jupyter_notebooks/03%20-%20seleccion%20de%20modelo.ipynb)

En la notebook anterior obtuvimos un mejor modelo mediante la selección de variables, pero ahora podemos obtener resultados similares utilizando **regularización**:

- 📓 [4 - Regresión Lasso y Ridge - Jupyter Notebook](./content/jupyter_notebooks/04%20-%20regularizacion.ipynb)

Te estarás preguntando: ¿no puedo utilizar regresión por mínimos cuadrados para ajustar curvas que no sean rectas? Y la respuesta es sí, usando **funciones base**. Esta técnica no se utiliza mucho en Machine Learning porque requiere seleccionar las funciones base, tarea que no es trivial. En general, se opta por trabajar con otros modelos de regresión, que abstraen al diseñador de hacer esta selección.

De todas formas, veamos un ejemplo práctico de cómo se trabaja en estos casos. Para ello, vamos a predecir la tasa de reacción a partir de la concentración, para una reacción enzimática que involucra células tratadas con el fármaco Puromycin:

- 📓 [5 - Regresión con funciones base - Jupyter Notebook](./content/jupyter_notebooks/05%20-%20regresion%20no%20lineal.ipynb)

### Evaluación práctica

Ahora que ya tienen las herramientas necesarias, es momento de realizar la **evaluación práctica**. Asegúrense de leer detenidamente el enunciado y no duden en plantear cualquier inquietud en el **foro**.

- 📝 Evaluación práctica - Módulo 5 - Swiss Dataset 🔒 *(Solo en Campus Virtual)*
- 📝 [Enunciado de la evaluación práctica](./exercise/README.md)

Recuerden que el código que les puede servir para realizar la evaluación está en el repositorio.

- 📓 [Link al notebook de la evaluación práctica - Jupyter Notebook](./exercise/swiss_reg.ipynb)
- 📊 [Link al dataset de la evaluación práctica - CSV](./exercise/swiss.csv)

## Dudas y consultas

Cualquier duda técnica o conceptual referida a esta unidad puede volcarse libremente en la sección de participación general del **foro**.

- 💬 Foro de consulta - Módulo 5 🔒 *(Solo en Campus Virtual)*

## Actividades no obligatorias

Si desean seguir profundizando en estos temas, les recomiendo leer los capítulos 3 y 6 de [An Introduction to Statistical Learning](https://www.statlearning.com/) de Gareth James.

Además, les dejo recursos de [StatQuest](https://statquest.org/), que prepara videos cortos y fáciles de entender, en este caso sobre modelos lineales (en inglés):

- 📺 [Linear Regression and Linear Models - StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/playlist?list=PLblh5JKOoLUIzaEkCLIUxQFjPIlapw8nU)
