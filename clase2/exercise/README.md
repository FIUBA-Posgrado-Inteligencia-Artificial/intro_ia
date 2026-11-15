# Evaluación práctica - Módulo 2 - Sudoku

## 📋 Descripción del problema

En este ejercicio deberán implementar un algoritmo de búsqueda para resolver un **Sudoku**.

El problema ya está modelado en la carpeta `aima_libs`, igual que la Torre de Hanoi que vimos en clase: un estado es el tablero, cada acción pone un dígito en la primera celda vacía, y un estado es solución cuando el tablero está completo. Ustedes deben implementar el algoritmo que recorre el árbol de búsqueda.

## ⚖️ Rúbrica de Evaluación

La nota máxima dependerá del algoritmo que elijan implementar:

| Algoritmo de Búsqueda | Condición / Heurística | Nota Máxima |
| :--- | :--- | :---: |
| 🔍 Búsqueda Primero en Anchura (BFS) | - | **6** |
| 🔍 Búsqueda Primero en Profundidad (DFS) | - | **6** |
| 🔍 Búsqueda de Costo Uniforme (UCS) | - | **6** |
| 🚀 Búsqueda de Profundidad Limitada con Profundidad Iterativa | - | **7** |
| 🧠 Búsqueda Voraz (Greedy) | Heurística dada en el notebook | **8** |
| 🧠 Búsqueda Voraz (Greedy) | Heurística propia | **9** |
| ✨ Búsqueda A* | Heurística dada en el notebook | **9** |
| ✨ Búsqueda A* | Heurística propia | **10** |

### ➕ Mejora opcional: elegir mejor la celda

Por defecto, las acciones completan siempre la primera celda vacía del tablero. Si en cambio completan en cada paso la **celda vacía con menos dígitos posibles** (*MRV*, *Minimum Remaining Values*), suman **2 puntos** a la nota máxima del algoritmo, sin pasar de 10. En el notebook se explica cómo implementarla.

---

## 🛠️ Instrucciones de Entrega

A continuación, se deja el enlace al notebook que deben completar para resolver el ejercicio.

> [!IMPORTANT]
> Es **obligatorio** completar únicamente las secciones indicadas en el notebook, sin agregar contenido adicional.

🔗 **[Notebook a completar](exercise_2.ipynb)**

> [!TIP]
> Si al ejecutar el notebook les aparece `ModuleNotFoundError: No module named 'aima_libs'`, revisen la siguiente guía:
>
> 🔗 **[Cómo hacer funcionar el notebook](COMO_EJECUTAR.md)**
