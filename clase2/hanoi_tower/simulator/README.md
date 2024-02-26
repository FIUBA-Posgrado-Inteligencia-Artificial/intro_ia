# Simulador de Torre de Hanoi

Este es un script que permite visualizar la resolución del problema de la Torre de Hanoi de forma gráfica y amena. Para 
funcionar, utiliza el módulo [PyGame](https://www.pygame.org/news) y además hace uso de Matplotlib únicamente para 
obtener los colores de los discos.

El script es altamente configurable, tanto en velocidad general como en tamaños y geometrías, todos accesibles desde 
`constants.py`.

Para ejecutar el script, se debe utilizar el siguiente comando:
```bash
python3 ./simulation_hanoi.py

```

Para su funcionamiento, el script depende de dos archivos JSON que deben encontrarse en la raíz del mismo:
- initial_state.json: Este JSON indica cómo se inicializan los discos y determina cuántos discos habrá en total.
- sequence.json: Este JSON indica el orden de los movimientos de los discos. 

El script permite movimientos ilegales dentro del juego de movimientos de discos, y siempre recuerda la altura a 
la que debe quedar el disco al insertarse en un pegamento específico. Sin embargo, no puede realizar movimientos 
imposibles, como mover un disco que no esté en la varilla correcta o sacar el último disco de una varilla llena. 
En sí, el script no fallará, pero la animación resultante puede no tener sentido en estos casos.

## Requisitos para los programas de búsqueda de soluciones

Los programas utilizados para encontrar soluciones deben respetar las siguientes especificaciones para que la 
solución pueda ser visualizada correctamente en el script.

### initial_state.json

El programa de búsqueda debe generar (o pueden crear manualmente) un JSON con el estado inicial de la ubicación de 
los discos. Se aceptan cualquier configuración y número de discos (en la configuración estándar, máximo 15 discos).

El archivo tiene el siguiente formato:

```JSON
{
  "peg_1": [5, 4, 3, 2, 1],
  "peg_2": [],
  "peg_3": []
}
```
Donde `peg_1` es la varilla de la izquierda, `peg_2` es la varilla del medio y `peg_3` es la varilla de la derecha. 
Para cada varilla se guarda un array con los números correspondientes a cada disco, siendo el 1 el más pequeño y 
así sucesivamente.

Se acepta cualquier configuración siempre y cuando **no se repita** ningún número de disco y todos los discos 
estén presentes (por ejemplo, si está el disco 4, también deben estar presentes el 1, el 2 y el 3).

Este es otro ejemplo válido:

```JSON
{
  "peg_1": [6, 2],
  "peg_2": [8, 7, 4],
  "peg_3": [1, 5, 3]
}
```

❌ Este es invalido porque falta el disco 4

```JSON
{
  "peg_1": [6, 2],
  "peg_2": [8, 7],
  "peg_3": [1, 5, 3]
}
```

❌ Este es inválido porque el disco 6 está repetido dos veces

```JSON
{
  "peg_1": [6, 2],
  "peg_2": [8, 7, 6],
  "peg_3": [1, 5, 3]
}
```

### sequence.json

El programa de búsqueda debe generar un JSON con la secuencia de movimientos de un disco por vez.

El archivo tiene el siguiente formato:

```JSON
[
	{
		"type": "movement",
		"disk": 1,
		"peg_start": 1,
		"peg_end": 2
	},
	{
		"type": "movement",
		"disk": 2,
		"peg_start": 1,
		"peg_end": 3
	},
        .
        .
        . 
	{
		"type": "movement",
		"disk": 3,
		"peg_start": 2,
		"peg_end": 1
	}
]
```

Se observa que es un array de objetos JSON.

Cada movimiento indica qué disco (`disk`) se mueve, desde qué varilla (`peg_start`) y hacia qué varilla se inserta 
(`peg_end`). El script ejecuta el movimiento si es de tipo `movement`. Otros tipos de secuencias son ignorados por 
el script, esto se hace para evitar la animación de secuencias en las que el programa de búsqueda decide no mover 
ningún disco.
