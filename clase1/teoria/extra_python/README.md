# Extra - Introducción a Python

<div align="center">
  <img src="images/img-003.png" alt="Python Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

---

## 🐍 ¿Qué es Python?

* Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
* Es un lenguaje de programación multiparadigma: permite programación orientada a objetos, programación imperativa y programación funcional.
* OBS: En el fondo, Python es un lenguaje orientado a objetos, todo, absolutamente todo es un objeto.
* Python usa tipado dinámico y conteo de referencias para la gestión de memoria.
* Python reemplazó en gran medida a LISP en IA, principalmente por ser multiparadigma.

### Compilado vs Interpretado

Esquema de compilado:
Editor → Compilación → Montaje → Ejecución (Código fuente → Programa objeto → Programa ejecutable)

Esquema de interpretado:
Código fuente → Intérprete → Traducción → Ejecución

---

## 🚀 ¿Por qué Python?

Python es uno de los lenguajes más usados en Ciencia de datos. ¿Por qué?
* Porque tiene una sintaxis simple y es fácil de adaptar para quienes no vienen de ambientes de ingeniería o ciencia de la informática.

Python es famoso por ser lento comparado con lenguajes como C++, ¿por qué se usa en Machine Learning o IA?
* La respuesta es que no se usa librerías hechas Python. Ninguna de las bibliotecas que se utilizan está realmente escrita en Python.
* Casi siempre están escritos en Fortran o C++ y simplemente interactúan con Python a través de algún wrapper.
* La velocidad de Python es irrelevante si solo se interactúa con las librerías escritas en un C++ altamente optimizado.

Fuente: https://qr.ae/pKrGdr

---

## 💻 Entornos de Ejecución

### Modo interactivo

Python posee un modo interactivo: Se escriben las instrucciones en una especie de intérprete de comandos. Las expresiones pueden ser introducidas una a una.

<div align="center">
  <img src="images/img-007.jpg" alt="Modo interactivo Python" width="50%">
</div>

### iPython

iPython (Parte de SciPy): Extiende la capacidad del modo interactivo y provee un kernel para Jupyter

<div align="center">
  <img src="images/img-008.jpg" alt="iPython" width="50%">
</div>

### Jupyter Notebook

Es un entorno computacional interactivo basado en la web para crear documentos de notebook. Jupyter Notebook es similar a la interfaz de notebook de otros programas como Maple, Mathematica y SageMath, un estilo de interfaz computacional que se originó con Mathematica en la década de 1980.

<div align="center">
  <img src="images/img-009.png" alt="Jupyter Notebook" width="10%">
</div>

<div align="center">
  <img src="images/img-013.jpg" alt="Jupyter Notebook ejemplo" width="50%">
</div>

### Google Colab

Si por algún motivo no podés correr Python de local o tienes un setup malo, podes usar Google Colab en la nube.

Google Colab permite escribir y ejecutar Python en el navegador:
* Sin configurar
* Fácil de compartir
* Acceso a GPUs sin cargo

Es una Jupyter Notebook que corre en una máquina virtual de Google Cloud:
* Es gratuito
* Ofrece 12 GB de RAM y 100 GB de disco.
* Las notebooks quedan en Google Drive, fácil de compartir.

<div align="center">
  <img src="images/img-014.png" alt="Google Colab Logo" width="20%">
</div>

<div align="center">
  <img src="images/img-018.png" alt="Google Colab ejemplo" width="50%">
</div>

---

## 📦 Variables en Python

* Específico y sensible a mayúsculas y minúsculas.
* Llamar al valor a través del nombre de la variable

Tipos de variables:
* Numéricas: Integer, float, complejos
* Caracteres: String
* Lógicas: Bool
* Listas
* Tuplas
* Set
* Diccionarios

### Funciones útiles para variables

* En Python, con `type()` puedo saber que variable es.
* Además, puedo convertir algunas variables en otra: `int()`, `float()`, `str()`, `bool()`, `list()`, `dict()`
* Preguntar el tipo de variable: `isinstance(a, int)`

### ¿Qué pasa cuando asignamos una variable?

Una variable de Python es un nombre simbólico que es una referencia o puntero a un objeto.

<div align="center">
  <img src="images/img-020.png" alt="Asignación variable paso 1" width="50%">
</div>

<div align="center">
  <img src="images/img-022.png" alt="Asignación variable paso 2" width="50%">
  <img src="images/img-024.png" alt="Asignación variable paso 2 código" width="50%">
</div>

<div align="center">
  <img src="images/img-026.png" alt="Asignación variable paso 3" width="50%">
  <img src="images/img-028.png" alt="Asignación variable paso 3 código" width="50%">
</div>

<div align="center">
  <img src="images/img-030.png" alt="Asignación variable paso 4" width="50%">
  <img src="images/img-032.png" alt="Asignación variable paso 4 código" width="50%">
</div>

### Mutabilidad

* **Mutables:** Permiten ser modificadas una vez creados.
* **Inmutables:** No permiten ser modificables una vez creados.

| Mutables | Inmutables |
|---|---|
| Listas | Variables numéricas |
| Diccionarios | Strings |
| Sets | Tuplas |

---

## 🧮 Operadores

### Aritméticos

| Operación | Operador | Ejemplo |
|---|---|---|
| Suma | `+` | `x + y` |
| Resta | `-` | `x - y` |
| Multiplicación | `*` | `x * y` |
| División | `/` | `x / y` |
| Módulo | `%` | `x % y` |
| División entera | `//` | `x // y` |
| Exponente | `**` | `x ** y` |

### Comparadores (retornan booleanos)

| Operación | Operador | Ejemplo |
|---|---|---|
| Mayor | `>` | `x > y` |
| Menor | `<` | `x < y` |
| Igual | `==` | `x == y` |
| Distinto | `!=` | `x != y` |
| Mayor o igual | `>=` | `x >= y` |
| Menor o igual | `<=` | `x <= y` |

### Lógicos (solo para booleanos)

| Operador | Ejemplo |
|---|---|
| `and` | `x and y` |
| `or` | `x or y` |
| `not` | `not x` |

### De asignación

| Operación | Operador | Ejemplo |
|---|---|---|
| Asignar | `=` | `x = y` |
| Sumar y asigna | `+=` | `x += y (x = x + y)` |
| Resta y asigna | `-=` | `x -= y (x = x - y)` |
| Multiplicación y asigna | `*=` | `x *= y (x = x * y)` |
| Divide y asigna | `/=` | `x /= y (x = x / y)` |

### Identificadores (devuelven booleanos)

| Operador | Ejemplo |
|---|---|
| `is` | `x is y` |
| `is not` | `x is not y` |

---

## 📚 Funciones y Librerías

### Llamada a funciones

* Las funciones son llamadas con un nombre y entre paréntesis los argumentos:
  `pow(2,5)  # Devuelve 32, es equivalente a 2**5`
* Esta forma de introducir los argumentos se llama de forma posicional.
* Otra forma de introducir los argumentos es mediante keys:
  `pow(exp=5, base=2)`
* Algunas funciones tienen argumentos opcionales:
  `pow(2, 5, mod=3)  # Es equivalente a (2**5) % 3`
* Los argumentos opcionales siempre son en modo de key.

Built-in Functions de Python: https://docs.python.org/3/library/functions.html

### Funciones Built-In importantes

* `print()` - Imprime en pantalla una cadena de strings
* `type()` - Retorna el tipo del objeto/variable.
* `abs()` - Retorna el valor absoluto
* `sorted()` - Retorna una lista ordenada del iterable
* `max()` - Retorna el máximo elemento de un iterable
* `min()` - Retorna el mínimo elemento de un iterable
* `round()` - Retorna un flotante redondeado
* `len()` - Retorna la cantidad de elementos en un objeto/iterable
* `sum()` - Suma todos los elementos de un iterable.
* `help()` - Muestra la documentación del objeto

### Importando librerías externas

La declaración `import` permite hacer visibles identificadores de otros módulos.
* Built-in libraries: https://docs.python.org/3/library/

<div align="center">
  <img src="images/img-036.png" alt="Import forma 1" width="50%">
  <img src="images/img-038.png" alt="Import forma 2" width="50%">
</div>

<div align="center">
  <img src="images/img-040.png" alt="Import forma 3" width="50%">
  <img src="images/img-042.png" alt="Import forma 4" width="50%">
</div>

<div align="center">
  <img src="images/img-044.jpg" alt="Import ejemplo 1" width="50%">
  <img src="images/img-046.jpg" alt="Import ejemplo 2" width="50%">
</div>

---

## 🚦 Declaración de Control

### IF

Diagrama de flujo:
Condición → True → Declaración → Resto del código
Condición → False → Resto del código

<div align="center">
  <img src="images/img-049.jpg" alt="IF diagrama" width="50%">
  <img src="images/img-051.png" alt="IF ejemplo" width="50%">
</div>

### IF – Múltiples condiciones en un IF

<div align="center">
  <img src="images/img-053.png" alt="Múltiples condiciones" width="50%">
  <img src="images/img-055.jpg" alt="Múltiples condiciones ejemplo 1" width="50%">
  <img src="images/img-057.jpg" alt="Múltiples condiciones ejemplo 2" width="50%">
</div>

### IF-ELSE

Diagrama de flujo:
Condición → True → Declaración
Condición → False → Declaración
→ Resto del código

<div align="center">
  <img src="images/img-059.png" alt="IF-ELSE diagrama" width="50%">
  <img src="images/img-061.png" alt="IF-ELSE ejemplo" width="50%">
</div>

### Nested IF-ELSE

<div align="center">
  <img src="images/img-063.png" alt="Nested IF-ELSE" width="50%">
  <img src="images/img-065.png" alt="Nested IF-ELSE ejemplo" width="50%">
</div>

### ELIF

Diagrama de flujo:
Condición → True → Declaración
↓ False
Condición → True → Declaración
↓ False
Condición → True → Declaración
↓ False
Declaración → Resto del código

<div align="center">
  <img src="images/img-067.png" alt="ELIF diagrama" width="50%">
  <img src="images/img-069.png" alt="ELIF ejemplo" width="50%">
</div>

---

## 🔄 Bucles

### While

Diagrama de flujo:
Condición → True → Declaración → (vuelve a Condición)
Condición → False → Resto del código

No es el bucle más popular de Python

<div align="center">
  <img src="images/img-072.png" alt="While diagrama" width="50%">
  <img src="images/img-074.png" alt="While ejemplo" width="50%">
</div>

### Ciclo FOR

<div align="center">
  <img src="images/img-076.png" alt="FOR diagrama" width="50%">
  <img src="images/img-078.png" alt="FOR ejemplo" width="50%">
</div>

### Iterables

* Un iterable es un objeto en Python capaz de retornar un miembro a la vez, permitiendo que sea iterable en un loop FOR.
* Las listas, tuplas, strings, diccionarios, sets son iterables
* Una versión de iterables son los generadores, que evitan guardar cada elemento en memoria, sino que se generan en la medida que se necesitan

* Tenemos la función `range(start, stop, step)` que genera una secuencia de números enteros.

<div align="center">
  <img src="images/img-080.png" alt="range() ejemplo" width="50%">
</div>

Ejemplos de iteración sobre: Lista o tupla, String, Diccionario

<div align="center">
  <img src="images/img-082.png" alt="Iteración lista/tupla" width="50%">
  <img src="images/img-084.png" alt="Iteración string" width="50%">
  <img src="images/img-086.png" alt="Iteración diccionario" width="50%">
</div>

---

## 🔡 Strings y sus operaciones

* Strings pueden ser comparados. Se comparan carácter a carácter. El orden es en ASCII (https://elcodigoascii.com.ar)
* Es decir `'a'` es menor a `'b'`, pero `'A'` es menor a `'a'`.
* También podemos usar el `+` para concatenar dos caracteres:
  `"Aureliano" + "Buendia"  # Retorna "AurelianoBuendia"`
* Si usamos `*` con un entero, repite el string:
  `"Aureliano" * 2  # Retorna "AurelianoAureliano"`

### Índices y cortes

Podemos cortar un string usando índices. Los cortes se puede determinar en rangos.

<div align="center">
  <img src="images/img-089.jpg" alt="String índices" width="50%">
  <img src="images/img-091.jpg" alt="String cortes" width="50%">
</div>

### Métodos de Strings

* Recordar que todo en Python es un objeto. Los objetos tienen atributos y métodos.
* Métodos son similares a funciones, toman argumentos, realizan una acción y devuelven algo:
  `<object>.<nombre del método>(<lista de argumentos>)`
* Strings son objetos, por lo que tienen métodos

<div align="center">
  <img src="images/img-093.jpg" alt="Métodos de strings" width="50%">
</div>

---

## 📋 Listas

* Una lista es una secuencia de cero o más objetos en Python normalmente llamados ítems.
* Las listas son mutables.
* Se generan usando `[]` y los ítems se separan en coma.

<div align="center">
  <img src="images/img-096.jpg" alt="Listas ejemplo" width="50%">
</div>

### Acceso por índices

Las listas también se pueden acceder a ítems mediante índices y cortarlas en sublistas.

<div align="center">
  <img src="images/img-098.jpg" alt="Listas índices" width="50%">
</div>

### Métodos de listas

<div align="center">
  <img src="images/img-100.jpg" alt="Métodos de listas" width="50%">
</div>

---

## 📌 Tuplas

* Una tupla es una secuencia de cero o más objetos Python normalmente llamados ítems.
* Las tuplas son inmutables.
* Se generan usando `()` y los ítems se separan en coma.

<div align="center">
  <img src="images/img-103.jpg" alt="Tuplas ejemplo" width="50%">
</div>

---

## 🔁 Volvamos al ciclo FOR

* FOR es realmente útil para iterar en ítems en secuencias como strings, listas y tuplas, entre otros…
* Es equivalente:

<div align="center">
  <img src="images/img-105.png" alt="FOR equivalencia" width="50%">
  <img src="images/img-107.jpg" alt="FOR equivalencia ejemplo" width="50%">
</div>

### ¿Y si quiero también el index?

<div align="center">
  <img src="images/img-109.jpg" alt="enumerate ejemplo" width="50%">
</div>

---

## 📖 Diccionario

* Un diccionario es una secuencia de un key único con un valor.
* Los diccionarios son mutables.
* Se generan usando `{}` y los ítems se separan en coma.

<div align="center">
  <img src="images/img-112.jpg" alt="Diccionario ejemplo" width="50%">
</div>

### Acceso y métodos

* Accedemos usando las keys

<div align="center">
  <img src="images/img-114.png" alt="Diccionario acceso" width="50%">
  <img src="images/img-116.jpg" alt="Diccionario métodos" width="50%">
</div>

### Ciclo FOR con el diccionario

<div align="center">
  <img src="images/img-118.png" alt="FOR diccionario" width="50%">
  <img src="images/img-120.png" alt="FOR diccionario ejemplo" width="50%">
</div>

---

## 🎨 String Formatting

Si queremos formar texto junto a variables, hay al menos 4 formas de hacerlo 😕

Queremos imprimir usando las variables:
"Hola, tu nombre es Aureliano Buendia y tu edad es 42. Un tercio es 0.333"

<div align="center">
  <img src="images/img-125.png" alt="Variables para formato" width="50%">
</div>

### Modo 1: Usando el operador `%`

<div align="center">
  <img src="images/img-127.png" alt="Formato con %" width="50%">
</div>

### Modo 2: Usando el método `.format()`

<div align="center">
  <img src="images/img-129.jpg" alt="Formato con .format() 1" width="50%">
  <img src="images/img-131.jpg" alt="Formato con .format() 2" width="50%">
</div>

### Modo 3: Usando f-strings

<div align="center">
  <img src="images/img-133.png" alt="Formato con f-strings" width="50%">
</div>

### Modo 4: Transformando y concatenando

<div align="center">
  <img src="images/img-135.png" alt="Formato con concatenación" width="50%">
</div>

---

## 🛠️ Funciones

### Creación de nuevas funciones

Supongamos que queremos calcular el número combinatorio:

$$ C(m, n) = \frac{m!}{(m-n)!n!} $$

Donde $n!$ (el factorial de $n$) es el producto de los números enteros de 1 a $n$.

$$ n! = 1 \cdot 2 \cdot 3 \dots (n-1) \cdot n = \prod_{i=1}^{n} i $$

<div align="center">
  <img src="images/img-142.png" alt="Función ejemplo 1" width="50%">
  <img src="images/img-144.png" alt="Función ejemplo 2" width="50%">
</div>

### Modularización con funciones

Escribir el mismo código una y otra vez es propenso a errores y difícil de mantener el código. Si creamos una función que haga la multiplicación va a ser mucho más sencillo.

<div align="center">
  <img src="images/img-146.png" alt="Función factorial 1" width="50%">
  <img src="images/img-148.png" alt="Función factorial 2" width="50%">
</div>

<div align="center">
  <img src="images/img-150.png" alt="Función combinatorio 1" width="50%">
  <img src="images/img-152.png" alt="Función combinatorio 2" width="50%">
</div>

### Variables locales

Las variables que están dentro de las funciones existen solamente dentro de las funciones (variables locales). Las funciones deben ser definidas antes de ser llamadas.

<div align="center">
  <img src="images/img-154.png" alt="Variables locales" width="50%">
</div>

### Argumentos opcionales

Podemos agregar argumentos opcionales fácilmente en nuestras funciones.

<div align="center">
  <img src="images/img-156.png" alt="Argumentos opcionales" width="50%">
</div>

### Retorno múltiple

Se pueden retornar muchos valores (que se obtendrán como en una tupla).

<div align="center">
  <img src="images/img-158.png" alt="Retorno múltiple" width="50%">
</div>

### Funciones recursivas

Una función puede llamarse a sí misma:

<div align="center">
  <img src="images/img-160.jpg" alt="Función recursiva" width="50%">
</div>

### Funciones Lambda

Una función anónima es una función sin nombre. En Python, se crea una función anónima con la palabra clave `lambda`.

<div align="center">
  <img src="images/img-162.jpg" alt="Función lambda" width="50%">
</div>

---

## ⚡ List Comprehension y Generators

### List Comprehension

* Es una expresión que genera una colección basada en otra colección.
* En general produce listas.
* Sintaxis simple y limpia.
* Soporta condicionales.
* Puede ser lazy.
* Es una de las herramientas más importante en Python

<div align="center">
  <img src="images/img-165.png" alt="List comprehension ejemplo" width="50%">
</div>

* Computa todos los valores cuando se crea (ocupa memoria).
* Es preferible usar List comprehension antes que bucles.
* También existen los:
  * Set comprehension
  * Dictionary comprehension

### Generators

Generan valores de forma lazy (no ocupan memoria) pero se consumen.

<div align="center">
  <img src="images/img-167.png" alt="Generator problema memoria" width="50%">
</div>

<div align="center">
  <img src="images/img-169.jpg" alt="Generator ejemplo" width="50%">
</div>

---

## 🏛️ Clases y Objetos

<div align="center">
  <img src="images/img-172.png" alt="Clase definición 1" width="50%">
  <img src="images/img-174.png" alt="Clase definición 2" width="50%">
</div>

<div align="center">
  <img src="images/img-176.png" alt="Clase uso 1" width="50%">
  <img src="images/img-178.jpg" alt="Clase uso 2" width="50%">
</div>

### Herencia

<div align="center">
  <img src="images/img-180.jpg" alt="Herencia ejemplo 1" width="50%">
  <img src="images/img-182.jpg" alt="Herencia ejemplo 2" width="50%">
</div>
