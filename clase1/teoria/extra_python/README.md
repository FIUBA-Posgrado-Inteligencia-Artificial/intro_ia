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

**Compilado:**

```mermaid
graph TD
    A["Editor"] --> B["Edición"]
    B --> C["Programa fuente"]
    D["Compilador"] --> E["Compilación"]
    E --> C
    C --> F["Programa objeto"]
    G["Linker"] --> H["Montaje"]
    H --> F
    F --> I["Programa ejecutable"]
    I --> J["Ejecución"]
    style A fill:#9b59b6,stroke:#7d3c98,color:#fff
    style D fill:#9b59b6,stroke:#7d3c98,color:#fff
    style G fill:#9b59b6,stroke:#7d3c98,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style E fill:#27ae60,stroke:#1e8449,color:#fff
    style H fill:#27ae60,stroke:#1e8449,color:#fff
    style J fill:#27ae60,stroke:#1e8449,color:#fff
    style C fill:#2e86c1,stroke:#1a5276,color:#fff
    style F fill:#2e86c1,stroke:#1a5276,color:#fff
    style I fill:#2e86c1,stroke:#1a5276,color:#fff
```

**Interpretado:**

```mermaid
graph TD
    A["Código fuente"] --> B["Intérprete"]
    B --> C["Traducción / Ejecución"]
    style A fill:#27ae60,stroke:#1e8449,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style C fill:#27ae60,stroke:#1e8449,color:#fff
```

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
  <img src="images/img-009.png" alt="Jupyter Notebook" width="15%">
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

**Paso 1:** 

```python
var_1 = 300
```

```mermaid
graph LR
    var_1["var_1"] -->|referencia| obj300["300"]
    style obj300 fill:#9b59b6,stroke:#7d3c98,color:#fff
```

**Paso 2:** 

```python
var_2 = var_1
```

```mermaid
graph LR
    var_1["var_1"] -->|referencia| obj300["300"]
    var_2["var_2"] -->|referencia| obj300
    style obj300 fill:#9b59b6,stroke:#7d3c98,color:#fff
```

**Paso 3:** 

```python
var_2 = 400
```

```mermaid
graph LR
    var_1["var_1"] -->|referencia| obj300["300"]
    var_2["var_2"] -->|referencia| obj400["400"]
    style obj300 fill:#9b59b6,stroke:#7d3c98,color:#fff
    style obj400 fill:#9b59b6,stroke:#7d3c98,color:#fff
```

**Paso 4:** 

```python
var_1 = "wut"
```

```mermaid
graph LR
    var_1["var_1"] -->|referencia| objwut["wut"]
    obj300["300"]
    var_2["var_2"] -->|referencia| obj400["400"]
    style objwut fill:#9b59b6,stroke:#7d3c98,color:#fff
    style obj300 fill:#808080,stroke:#666,color:#fff
    style obj400 fill:#9b59b6,stroke:#7d3c98,color:#fff
```

> *300 quedará en memoria RAM (en gris) hasta que el Garbage Collector lo recolecte o asignamos una nueva variable con 300.*

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


```python
# Forma 1
import math

var = math.sqrt(16)
print(math.pi)
```

```python
# Forma 2
import math as mt

var = mt.sqrt(16)
print(mt.pi)
```

```python
# Forma 3
from math import pi, sqrt 

var = sqrt(16)
print(pi)
```

```python
# Forma 4
from math import *

var = sqrt(16)
print(pi)
```

---

## 🚦 Declaración de Control

### IF

```mermaid
graph TD
    A{"Condición"} -->|True| B["Declaración"]
    A -->|False| C["Resto del código"]
    B --> C
    style A fill:#f39c12,stroke:#d68910,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style C fill:#2e86c1,stroke:#1a5276,color:#fff
```

```python
if <Expresión_booleana>:
    <Declaración>

<Resto_del_codigo>
```

```python
if num > 3:
    print("Epaaaa")
```

### IF – Múltiples condiciones en un IF

```python
if 3 < num < 35:
    print("Epaaaa")
```

```python
if 3 < num < 35 or b == 2:
    print("Epaaaa")
```

```python
if num > 3 and (num < 5 or b == 2):
    print("Epaaaa")
```

### IF-ELSE

```mermaid
graph TD
    A{"Condición"} -->|True| B["Declaración 1"]
    A -->|False| C["Declaración 2"]
    B --> D["Resto del código"]
    C --> D
    style A fill:#f39c12,stroke:#d68910,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style C fill:#e74c3c,stroke:#c0392b,color:#fff
    style D fill:#2e86c1,stroke:#1a5276,color:#fff
```

```python
if <Expresión_booleana>:
    <Declaración_1>
else: 
    <Declaración_2>

<Resto_del_codigo>
```

```python
if num > 3:
    print("num es mayor a 3")
else:
    print("num es menor o igual a 3")
```

### Nested IF-ELSE

```python
if <Expresión_1>:
    <Declaración_1>
    if <Expresión_2>:
        <Declaración_2>
else: 
    <Declaración_3>
    if <Expresión_4>:
        <Declaración_4>

<Resto_del_codigo>
```

```python
if num > 3:
    print("num es mayor a 3")
    if num < 5: 
        print("num es menor a 5")
else:
    print("num es menor o igual a 3")
    if num > 1:
        print("num es mayor a 1")
```

### ELIF

```mermaid
graph TD
    A{"Condición 1"} -->|True| B["Declaración 1"]
    A -->|False| C{"Condición 2"}
    C -->|True| D["Declaración 2"]
    C -->|False| E{"Condición 3"}
    E -->|True| F["Declaración 3"]
    E -->|False| G["Declaración 4"]
    B --> H["Resto del código"]
    D --> H
    F --> H
    G --> H
    style A fill:#f39c12,stroke:#d68910,color:#fff
    style C fill:#f39c12,stroke:#d68910,color:#fff
    style E fill:#f39c12,stroke:#d68910,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style D fill:#27ae60,stroke:#1e8449,color:#fff
    style F fill:#27ae60,stroke:#1e8449,color:#fff
    style G fill:#e74c3c,stroke:#c0392b,color:#fff
    style H fill:#2e86c1,stroke:#1a5276,color:#fff
```

```python
if <Expresión_1>:
    <Declaración_1>
elif <Expresión_2>:
    <Declaración_2>
elif <Expresión_3>:
    <Declaración_3>
else: 
    <Declaración_4>

<Resto_del_codigo>
```

```python
if num == 3:
    print("num es 3")
elif num == 5:
    print("num es 5")
elif num == 42:
    print("num es 42")
else:
    print("num no es 3, 4, o 42")
```

---

## 🔄 Bucles

```mermaid
graph TD
    A{"Condición"} -->|True| B["Declaración"]
    B --> A
    A -->|False| C["Resto del código"]
    style A fill:#f39c12,stroke:#d68910,color:#fff
    style B fill:#27ae60,stroke:#1e8449,color:#fff
    style C fill:#2e86c1,stroke:#1a5276,color:#fff
```

### While

No es el bucle más popular de Python

```python
while <Expresión>:
    <declaración_1>
    <declaración_2>
    ...
    <declaración_n>

<Resto_del_codigo>
```

```python
nivel = 0
while nivel <= 9000:
    print("Aumentando de nivel")
    nivel += 1

print("It's over 9000!!")
```

### Ciclo FOR

```python
for <iterable> in <objeto_iterable>:
    <declaración_1>
    <declaración_2>
    ...
    <declaración_n>

<Resto_del_codigo>
```

```python
producto = 0
for value in range(1, 11):
    producto *= value
```

### Iterables

* Un iterable es un objeto en Python capaz de retornar un miembro a la vez, permitiendo que sea iterable en un loop FOR.
* Las listas, tuplas, strings, diccionarios, sets son iterables
* Una versión de iterables son los generadores, que evitan guardar cada elemento en memoria, sino que se generan en la medida que se necesitan

* Tenemos la función `range(start, stop, step)` que genera una secuencia de números enteros.

```python
for i in range(10):
    print(i)
```

Ejemplos de iteración sobre: Lista o tupla, String, Diccionario

```python
lista = [0, 'alice', 3.14]
for elemento in lista:
    print(elemento)
```

```python
string = "Buenas noches América!"
for char in string:
    print(char)
```

```python
diccionario = {
    "nombre": "Aureliano",
    "apellido": "Buendia",
    "pais": "Colombia"
}
for key in diccionario:
    print(key)
    print(diccionario[key])
```

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

```python
nombre_completo = "Aureliano Buendia"

nombre_completo[0] # Retorna A
```

```python
nombre_completo[inicio:superior]

nombre_completo[0:9]   # Retorna Aureliano
nombre_completo[:9]    # Retorna Aureliano
nombre_completo[10:17] # Retorna Buendia
nombre_completo[:17]   # Retorna Buendia
nombre_completo[-7:]   # Retorna Buendia
```

### Métodos de Strings

* Recordar que todo en Python es un objeto. Los objetos tienen atributos y métodos.
* Métodos son similares a funciones, toman argumentos, realizan una acción y devuelven algo:
  `<object>.<nombre del método>(<lista de argumentos>)`
* Strings son objetos, por lo que tienen métodos

```python
nombre_completo = "Aureliano Buendia"

nombre_completo.isupper()               # Retorna False
nombre_completo.upper()                 # Retorna AURELIANO BUENDIA
nombre_completo.lower()                 # Retorna aureliano buendia
nombre_completo.startswith("Aureliano") # Retorna True
```

---

## 📋 Listas

* Una lista es una secuencia de cero o más objetos en Python normalmente llamados ítems.
* Las listas son mutables.
* Se generan usando `[]` y los ítems se separan en coma.

```python
[] # Lista vacia
["Aureliano"] # Lista con un solo string
["Aureliano", "Buendia"] # Lista con dos strings
["Aureliano", "Buendia", 42] # Lista con dos strings y un entero
["Aureliano", ["Buendia", 42]] # Lista con un string y una lista
["Aureliano",  "Buendia", print] # Lista con dos strings y una función
```

### Acceso por índices

Las listas también se pueden acceder a ítems mediante índices y cortarlas en sublistas.

```python
list_range = list(range(0, 22, 2))

list_range[2]     # Retorna 4
list_range[:9]    # Retorna [0, 2, 4, 6, 8, 10, 12, 14, 16]
list_range[5:9]   # Retorna [10, 12, 14, 16]
list_range[-1]    # Retorna 20
list_range[-7:-1] # Retorna [8, 10, 12, 14, 16, 18]
```

### Métodos de listas

```python
listita = []           # listita es una lista vacia
listita.append(42)     # listita es [42]
listita.append(19)     # listita es [42, 19]
listita.sort()         # listita es [19, 42]
var = listita.pop()    # Guarda en var a 42, lisita es [19]
listita.append(0, 22)  # listita es [22, 19]
listita.append(-1, 55) # listita es [22, 55, 19]
listita.remove(22)     # listita es [55, 19]
listita.remove(22)     # Error (ValueError)
```

---

## 📌 Tuplas

* Una tupla es una secuencia de cero o más objetos Python normalmente llamados ítems.
* Las tuplas son inmutables.
* Se generan usando `()` y los ítems se separan en coma.

```python
("Aureliano",) # Tupla con un solo string
("Aureliano", "Buendia") # Tupla con dos strings
("Aureliano", "Buendia", 42) # Tupla con dos strings y un entero
("Aureliano", ["Buendia", 42]) # Tupla con un string y una lista
("Aureliano", "Buendia", print) # Tupla con dos strings y una función
```

---

## 🔁 Volvamos al ciclo FOR

* FOR es realmente útil para iterar en ítems en secuencias como strings, listas y tuplas, entre otros…
* Es equivalente:

```python
listita = [4, 8, 15, 16, 23, 42]
for item in listita:
    print(item)
```

```python
listita = [4, 8, 15, 16, 23, 42]
for index in range(len(listita)):
    print(listita[index])
```

### ¿Y si quiero también el index?

```python
listita = [4, 8, 15, 16, 23, 42]
for index, item in enumerate(listita):
    print(f"Posicion {index}")
    print(f"Elemento {item}")
```

---

## 📖 Diccionario

* Un diccionario es una secuencia de un key único con un valor.
* Los diccionarios son mutables.
* Se generan usando `{}` y los ítems se separan en coma.

```python
dictionary1 = {} # Un diccionario vacio
dictionary = {
  "nombre": "Aureliano",
  "apellido": "Buendia",
  "edad": 42,
  "hobbies": ["tenis", "cocer"]
} # Un diccionario con 4 entradas
```

### Acceso y métodos

* Accedemos usando las keys

```python
name = dictionary["nombre"] # Guarda en name el valor "Aureliano"
```

```python
name = dictionary.pop("nombre") # Guarda el valor "Aureliano" y lo saca del diccionario.
dictionary["ciudad"] = "Macondo" # Agrega la nuevca key ciudad.
dictionary.update(dictionary2) # Agrega las keys y valores de otro diccionario
```

### Ciclo FOR con el diccionario

```python
for key in dictionary:
    print(key) # Imprime solo las keys
```

```python
for key, value in dictionary.items():
    print(key)
    print(value) # Imprimimos tambien los valores de cada key
```
---

## 🎨 String Formatting

Si queremos formar texto junto a variables, hay al menos 4 formas de hacerlo 😕

Queremos imprimir usando las variables:
"Hola, tu nombre es Aureliano Buendia y tu edad es 42. Un tercio es 0.333"

```python
nombre = "Aureliano"
apellido = "Buendia"
edad = 42
tercio = 1/3
```

### Modo 1: Usando el operador `%`

```python
texto_1 = "Hola, tu nombre es %s %s y tu edad es %d. Un tercio es %.3f" % (nombre, apellido, edad, tercio)
print(texto_1)
```

### Modo 2: Usando el método `.format()`

```python
texto_2 = "Hola, tu nombre es {} {} y tu edad es {}. Un tercio es {:.3f}".format(nombre, apellido, edad, tercio)
print(texto_2)
```

```python
texto_3 = "Hola, tu nombre es {nom} {ape} y tu edad es {ed}. Un tercio es {ter:.3f}".format(
    nom=nombre, ape=apellido, ed=edad, ter=tercio
)
print(texto_3)
```

### Modo 3: Usando f-strings

```python
texto_4 = f"Hola, tu nombre es {nombre} {apellido} y tu edad es {edad}. Un tercio es {tercio:.3f}"
print(texto_4)
```

### Modo 4: Transformando y concatenando

```python
texto_5 = "Hola, tu nombre es " + nombre + " " + apellido + " y tu edad es " + str(edad) + ". Un tercio es " + str(round(tercio, 3))
print(texto_4)
```

---

## 🛠️ Funciones

### Creación de nuevas funciones

Supongamos que queremos calcular el número combinatorio:

$$ C(m, n) = \frac{m!}{(m-n)!n!} $$

Donde $n!$ (el factorial de $n$) es el producto de los números enteros de 1 a $n$.

$$ n! = 1 \cdot 2 \cdot 3 \dots (n-1) \cdot n = \prod_{i=1}^{n} i $$

```python
# Factorial de n!
f = 1
for i in range(1, n + 1):
  f *= i
```

```python
n, m = 3, 5

# Numerador
num = 1
for i in range(1, m + 1):
  num *= i

# Denominador
den_a = 1
for i in range(1, n + 1):
  den_a *= i

den_b = 1
for i in range(1, m - n + 1):
  den_b *= i

den = den_a * den_b

# Resultado
num_conv = num / den
```

### Modularización con funciones

Escribir el mismo código una y otra vez es propenso a errores y difícil de mantener el código. Si creamos una función que haga la multiplicación va a ser mucho más sencillo.

```python
def <nombre_función>(argumentos):
  <secuencia_de_código>
```

```python
def factorial(n):
  """Calcula el factorial de n"""
  output = 1
  for i in range(1, n + 1):
    output *= i

  return output

def num_con(n, m):
  """Calcula el numero combinatorio de n y m
  
  n es la cantidad de objetos a seleccionar de un conjunto total de m objetos
  """

  return int(factorial(m) / (factorial(n) * factorial(m - n)))
```

### Variables locales

Las variables que están dentro de las funciones existen solamente dentro de las funciones (variables locales). Las funciones deben ser definidas antes de ser llamadas.

```python
first() # Da error (no definida)

def first():
  print("Hola")
  second() # Que pasaría aqui?

def second():
  print("Hola, soy segunda")

first() # Aquí es correcto
```

### Argumentos opcionales

Podemos agregar argumentos opcionales fácilmente en nuestras funciones.

```python
def factorial(n, print_output=False):
  """Calcula el factorial de n"""
  output = 1
  for i in range(1, n + 1):
    output *= i

  if print_output:
    print(output)

  return output
```

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
