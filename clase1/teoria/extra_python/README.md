# Extra - Introducción a Python

<div align="center">
  <img src="images/img-003.png" alt="Python Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

---

## 🐍 ¿Qué es Python?

* Python es un lenguaje de **alto nivel de programación**, **interpretado**, cuya filosofía hace hincapié en la legibilidad de su código.
* Es **multiparadigma**: permite programación orientada a objetos (todo es un objeto), imperativa y funcional.
* Usa **tipado dinámico** y conteo de referencias para la gestión de memoria.

### Compilado vs Interpretado

* **Compilado:** Código fuente → Compilación → Programa ejecutable (ej. C++)
* **Interpretado:** Código fuente → Intérprete → Ejecución (ej. Python)

---

## 🚀 Python en Ciencia de Datos e IA

Python es ampliamente utilizado en Data Science e Inteligencia Artificial porque:
1. Tiene una **sintaxis simple**, ideal para profesionales ajenos a la informática.
2. Aunque puede ser más "lento", **no ejecuta tareas pesadas directamente en Python**. Las librerías clave de ML e IA (como TensorFlow, PyTorch, NumPy) están escritas en **C++** o **Fortran** altamente optimizado. Python simplemente actúa como un *wrapper* o interfaz rápida y sencilla.

---

## 💻 Entornos de Ejecución

### Modo Interactivo e iPython
Permite escribir instrucciones en un intérprete donde las expresiones se evalúan una a una. **iPython** (de SciPy) mejora esto proveyendo el kernel base interactivamente, sobre el que funcionan muchas notebooks.

### Jupyter Notebook
Entorno computacional interactivo basado en la web para crear documentos que combinan código, texto y visualizaciones.

<div align="center">
  <img src="images/img-013.jpg" alt="Jupyter Notebook" width="60%">
</div>

### Google Colab
Jupyter Notebook ejecutado en una máquina virtual de Google Cloud.
* **Gratuito** y corre en el navegador.
* **Sin configuración previa**.
* Provee **acceso a GPUs** sin cargo y facilita compartir notebooks integrándose con Google Drive.

<div align="center">
  <img src="images/img-018.png" alt="Google Colab" width="60%">
</div>

---

## 📦 Variables

Una variable en Python es un **nombre simbólico** que actúa como referencia o puntero hacia un objeto en memoria.

### Tipos de Variables
* **Numéricas:** `int` (enteros), `float` (decimales flotantes), complejos.
* **Caracteres:** `str` (strings/cadenas de texto).
* **Lógicas:** `bool` (booleanos `True` o `False`).
* **Estructuras de datos:** Listas, Tuplas, Sets, Diccionarios.

### Mutabilidad
* **Mutables** (se pueden modificar *in-place*): Listas, Diccionarios, Sets.
* **Inmutables** (NO se pueden modificar una vez creados): Variables numéricas, Strings, Tuplas.

*Tip: Con `type(variable)` podemos saber su tipo, y podemos forzar conversiones de tipo usando constructores como `int()`, `float()`, o `str()`.*

---

## 🧮 Operadores

- **Aritméticos:** `+` (suma), `-` (resta), `*` (multiplicación), `/` (división), `%` (módulo o resto), `//` (división entera), `**` (exponente).
- **Comparadores (devuelven Bool):** `>`, `<`, `==` (igualdad), `!=` (distinto), `>=`, `<=`.
- **Lógicos (para Bool):** `and`, `or`, `not`.
- **De asignación:** `=`, `+=`, `-=`, `*=`, `/=`.
- **De identidad:** `is`, `is not`.

---

## 📚 Funciones Integradas y Librerías

### Funciones Built-In
Python trae funciones nativas y utilidades listas para usar, por ejemplo:
`print()`, `type()`, `abs()`, `sorted()`, `max()`, `min()`, `round()`, `len()`, `sum()`, `help()`.

### Importando Librerías
Usamos `import` para traer funciones de otros módulos a nuestro contexto. Podemos importar la libería completa, con seudónimos (alias), o solo aquello que vayamos a usar:
* `import math`
* `import pandas as pd`
* `from math import pi`

<div align="center">
  <img src="images/img-044.jpg" alt="Ejemplos de Imports" width="50%">
</div>

---

## 🚦 Estructuras de Control de Flujo

### Condicionales: IF, ELIF, ELSE

Nos permiten bifurcar y tomar decisiones en el flujo del código basándonos en condiciones que se evalúan implícita o explícitamente a `True` o `False`.

<div align="center">
  <img src="images/img-053.png" alt="Ejemplo IF" width="50%">
  <img src="images/img-069.png" alt="Ejemplo ELIF" width="50%">
</div>

---

## 🔄 Bucles (Loops) e Iterables

Se utilizan para ejecutar y repetir bloques de código un determinado número de veces, o hasta que se cumpla una condición.

### While
Se ejecuta *mientras* una condición sea evaluada como verdadera.
<div align="center">
  <img src="images/img-074.png" alt="Ejemplo While" width="50%">
</div>

### For
Especialmente útil en Python para recorrer iterables uno a uno, extrayendo cada miembro en el ciclo. Se puede iterar sobre listas, tuplas, strings o diccionarios.
<div align="center">
  <img src="images/img-078.png" alt="Ejemplo For" width="50%">
</div>

*Nota: La función `range(start, stop, step)` es especialmente útil acoplada con listas porque genera una subsecuencia virtual de números enteros perfecta para índices o conteos.*

---

## 🔡 Tipos de Datos Compuestos (Colecciones)

### Strings (Cadenas de texto)
- Comparables letra a letra según su valor codificado en tabla ASCII.
- Se pueden concatenar usando `+` y repetir usando `*`.
- Soportan métodos integrados como `.upper()`, `.lower()` y **slicing** (corte con índices `[inicio:fin]`).

### Listas (`[]`)
- Secuencia estructurada y **mutable**.
- Soportan índices, slicing, y proveen amplísimos métodos útiles como `.append()`, `.pop()`, `.insert()`, o `.sort()`.

<div align="center">
  <img src="images/img-100.jpg" alt="Métodos de listas" width="50%">
</div>

### Tuplas (`()`)
- Secuencia **inmutable** de objetos. Especialmente útiles y performantes para datos crudos de lectura que garantizan que la arquitectura no alterará el bloque internamente.

### Diccionarios (`{}`)
- Estructura **mutable** que conecta pares de clave y valor (`Key: Value`).
- Sus claves deben ser únicas. Proveen un acceso mapeado O(1) ultrarrápido a los valores.

<div align="center">
  <img src="images/img-116.jpg" alt="Diccionarios" width="50%">
</div>

---

## 🎨 Formateo de Strings

Diferentes formas de formatear la inyección de variables dentro de un texto:
1. **Con variables inyectadas `%`:** `"Nombre: %s" % nombre`
2. **Con `.format()`:** `"Nombre: {}".format(nombre)`
3. **Usando *f-strings* (La más moderna y recomendada):** `f"Nombre: {nombre}"`
4. **Transformando y concatenando clásicamente:** `"Nombre: " + str(nombre)`

<div align="center">
  <img src="images/img-133.png" alt="Ejemplo formato f-strings" width="50%">
</div>

---

## 🛠️ Creación de Funciones

Definimos nuestras propias funciones para no repetir código (`DRY` - *Don't Repeat Yourself*), modularizar nuestras soluciones y facilitar el mantenimiento analítico.

* Declaradas explícitamente con `def nombre_funcion(argumentos):`.
* Variables creadas en su interior nacen y mueren ahí (**locales**).
* Tienen variables "por defecto" si uno lo desea y pueden devolver muchos valores empaquetados como si fueran una tupla usando `return`.
* **Lambda**: Python permite la creación opcional de una "función anónima de un solo uso" escrita en una sola línea a través del invocador `lambda`.

<div align="center">
  <img src="images/img-146.png" alt="Módulo de funciones" width="50%">
</div>

---

## ⚡ List Comprehension y Generadores

### List Comprehension
Es una sintaxis altamente estilizada en Python para crear fácilmente listas filtradas y transformadas compactando la acción de bucles for y condicionales if anexos en una sola línea, más performante y "pythónica".

<div align="center">
  <img src="images/img-165.png" alt="List Comprehension" width="50%">
</div>

### Generators (Generadores)
A diferencia de crear toda una lista de millones de variables y copar la memoria RAM entera intermitentemente, los generadores devuelven secuencias *lazy* o "demoradas". Crean sus valores de forma efímera **solamente cuándo y a medida que** un bucle lo expide.  

<div align="center">
  <img src="images/img-169.jpg" alt="Ejemplo Generators" width="50%">
</div>

---

## 🏛️ Clases y Objetos (Programación Orientada a Objetos)

Python tiene capacidad plena para modelar objetos complejos y plantillas como la vida real a través de POO (OOP en inglés).

* **Clase (`class`):** Plantilla maestra que describe la arquitectura para crear entidades que tienen componentes abstractos. Define atributos (propiedades base o variables inherentes al objeto) y métodos (funciones y acciones inherentes al objeto).
* **Objeto:** Es la entidad instanciada e inicializada originada a raíz del esqueleto de una Clase.
* **Herencia:** Uno puede componer super estructuras y heredar o reescribir funciones padres fácilmente creando una familia ramificada de módulos.

<div align="center">
  <img src="images/img-174.png" alt="Declaración de un bloque Clase abstracto" width="50%">
</div>
