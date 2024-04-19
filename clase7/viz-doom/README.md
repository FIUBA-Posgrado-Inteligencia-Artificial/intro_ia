# Juego de Aprendizaje por Refuerzo con Q-Learning en VizDoom

Este proyecto implementa un juego simple utilizando el entorno VizDoom y un agente de aprendizaje por refuerzo que 
utiliza el algoritmo Q-Learning para aprender a jugar el juego.

El objetivo de este proyecto es demostrar cómo se puede utilizar el aprendizaje por refuerzo para entrenar a un 
agente a jugar un juego simple. En este caso, el juego consiste en un escenario en VizDoom donde un agente debe 
moverse y disparar para maximizar su recompensa.

## Estructura del Código

El código está dividido en tres partes principales:

- `game_logic.py`: Incluyen GameSimple, que representa el juego y su lógica, y AgentQLearning, que implementa el 
agente de aprendizaje por refuerzo utilizando Q-Learning. 
- `train.py`: Bucle principal de entrenamiento. Este bucle maneja el entrenamiento del agente a lo largo de 
múltiples episodios del juego. Guarda la tabla Q entrenada en el archivo `last_q.npy`.
- `test.py`: Bucle principal de evaluación. Este bucle ejecuta la tabla Q de la Política encontrada por el 
algoritmo de Q-Learning (Lee el archivo `last_q.npy`). Calcula la recompensa promedio por episodio.

### Dependencias

- Python >=3.8
- VizDoom
- NumPy
