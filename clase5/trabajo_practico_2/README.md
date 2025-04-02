# TP2: Regresión del valor de valor medio de casas en distritos de California

Se requiere construir una regresión que permita predecir el valor medio de las casas en distritos de California, EE. UU. (medido en cientos de miles de dólares, es decir, $100,000). Este conjunto de datos proviene del censo de 1990 de EE. UU., donde cada observación corresponde a un bloque. Un bloque es la unidad geográfica más pequeña para la cual la Oficina del Censo de EE. UU. publica datos de muestra. Un bloque típicamente tiene una población de entre 600 y 3.000 personas.

Los atributos, en el orden en que se encuentran en el conjunto de datos, son:

- `MedInc`: Ingreso medio en el bloque
- `HouseAge`: Edad mediana de las casas en el bloque
- `AveRooms`: Número promedio de habitaciones por hogar.
- `AveBedrms`: Número promedio de dormitorios por hogar.
- `Population`: Población del bloque.
- `AveOccup`: Número promedio de miembros por hogar.
- `Latitude`: Latitud del bloque.
- `Longitude`: Longitud del bloque.

El target es:

- `MedHouseVal`: Mediana del costo de las casas en el bloque (en unidades de $100.000).

Para este TP, se proporciona un notebook (`ayuda.ipynb`) con la lectura del dataset, la separación de los datos, entre otras ayudas para resolver este trabajo práctico.

## Tareas y preguntas a resolver:

1. **Obtener la correlación** entre los atributos y entre los atributos y el target. ¿Qué atributo tiene mayor correlación lineal con el target? ¿Cuáles atributos parecen estar más correlacionados entre sí? Se pueden obtener los valores de correlación o graficarlos directamente utilizando un mapa de calor.
2. **Graficar los histogramas** de los diferentes atributos y el target. ¿Qué tipo de forma tienen los histogramas? ¿Se observa alguna forma de campana que sugiera que los datos provienen de una distribución gaussiana, sin realizar pruebas de hipótesis?
3. **Calcular la regresión lineal** utilizando todos los atributos. Con el conjunto de entrenamiento, calcular la varianza total del modelo y la varianza explicada por el modelo. ¿Está el modelo capturando el comportamiento del target? Expanda su respuesta.
4. **Calcular las métricas de MSE, MAE y R²** para el conjunto de evaluación.
5. Crear una **regresión de Ridge**. Usando validación cruzada de 5 folds y tomando como métrica el MSE, calcular el mejor valor de α, buscando entre [0, 12.5]. Graficar el valor de MSE versus α.
6. **Comparar entre la regresión lineal y la mejor regresión de Ridge** los resultados obtenidos en el conjunto de evaluación. ¿Cuál de los dos modelos da mejores resultados (usando MSE y MAE)? Conjeturar por qué el modelo que da mejores resultados mejora. ¿Qué error se puede haber reducido?

### Entregables:

El entregable debe consistir en uno o más archivos de notebook Jupyter (`.ipynb`) con las respuestas. Aunque se permite usar otros tipos de entregables, es importante incluir tanto el código como las respuestas. Pueden subir el contenido o proporcionar un enlace a un repositorio público (GitHub o GitLab) con el contenido. **No olviden especificar los autores del trabajo práctico en el entregable**.

### Recursos:

Para resolver este trabajo práctico, son libres de utilizar los recursos que consideren necesarios. Pueden hacerlo en cualquier lenguaje de programación y de la forma que consideren apropiada.
