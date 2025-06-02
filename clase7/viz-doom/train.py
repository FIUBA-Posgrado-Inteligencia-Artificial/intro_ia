# Este es el script de entrenamiento. Se entrena el agente usando Q-Learning y se guarda la tabla Q.
import numpy as np

from game_logic import Environment, Agent, QLearning
from config import Actions, NUMBER_OF_EPISODES, MAX_MOVS, Q_ALPHA, Q_GAMMA, Q_EPSILON, Q_EPSILON_DECAY

if __name__ == "__main__":

    # Inicializamos estas variables para que no lloren los IDEs
    action = Actions.STAND
    pos_block_end = None
    pos_block_start = None
    last_action = Actions.STAND

    # Usamos la clase agente para el monstruo porque a pesar qeu no lo vamos a mover como agente, tiene toda la logica
    # que nos facilita el control del mismo. Además, ya deja listo para adaptar a un modo multi-agente.
    monster = Agent()

    # Creamos el agente
    agent = Agent()

    # Creamos una instancia del juego
    game = Environment(n_episodes=NUMBER_OF_EPISODES, max_movements=MAX_MOVS, monster=monster)

    # Creamos el algoritmo de entrenamiento
    q_learning = QLearning(alpha=Q_ALPHA, gamma=Q_GAMMA, epsilon=Q_EPSILON, epsilon_decay=Q_EPSILON_DECAY)

    # Iniciamos el juego
    game.init()

    # Iniciamos esta función actualiza las posiciones del agente y el monstruo, si no, no saben donde están parados.
    game.update_state(agent)

    # Ciclo principal que ejecuta los episodios del juego.
    for i in range(NUMBER_OF_EPISODES):
        print(f"Episodio #{i + 1}")

        # Iniciamos un nuevo episodio
        game.new_episode(agent)

        # Bandera para indicar al agente cuando hacer una acción
        agent_decide = True

        # Bucle principal del juego durante un episodio.
        while not game.is_episode_finished(agent):

            # Obtiene el estado actual
            game.update_state(agent)

            # Movemos a Doom Guy a la posición inicial, el ambiente toma control del agente momentáneamente
            if not game.is_agent_in_position(agent):
                continue

            if agent_decide:
                # Inicializamos los FPS para llevar seguimiento de las animaciones
                game.reset_animation_fps()

                # Obtenemos donde está el agente
                pos_block_start = agent.get_position()

                # Le pasamos al algoritmo de Q_learning para que defina la siguiente acción
                action = q_learning.next_sequence(agent, pos_block_start)

                # Dado el tipo de acción, el agente obtiene a que bloque desplazarse
                pos_block_end = agent.obtain_next_block(action.value)
                last_action = action
                agent_decide = False
                print("Proxima acción:", last_action)

            # Hacemos la animación para que se mueva o dispare el agente
            agent_decide = game.animation(action, agent, pos_block_end)

            # Cuando termina la animación
            if agent_decide:
                # Actualizamos la cantidad de movimiento del agente
                agent.add_movement()

                # Actualizamos la tabla Q del agente, usando el algoritmo de Q-Learning con la recompensa obtenida
                instant_reward = game.obtain_all_reward(agent, action)
                agent.set_reward(instant_reward)
                episode_will_finish = agent.movements >= MAX_MOVS
                q_learning.refresh_q_table(agent, pos_block_start, pos_block_end, last_action, instant_reward,
                                           episode_finished=episode_will_finish)

        # Cuando el agente le pega el tiro al demonio, automáticamente se corta el episodio, por lo que debemos calcular
        # la recompensa de la última acción.
        if last_action == Actions.SHOOT and agent.position_block == game.monster.position_block:
            instant_reward = game.obtain_all_reward(agent, action)
            agent.set_reward(instant_reward)
            q_learning.refresh_q_table(agent, pos_block_start, pos_block_end, last_action, instant_reward,
                                       episode_finished=True)

        # Mostramos como fue el episodio
        print("************************")
        print("Episodio terminado.")
        print("Recompensa total:", agent.total_reward)
        print("Probabilidad de exploración:", q_learning.epsilon)
        print("Tabla de Q-value obtenida:")
        print(agent.get_q_table())
        print("************************")

        # Decaemos la probabilidad de exploración
        q_learning.decay_epsilon(i)

    # Guardamos la tabla Q obtenida
    print("Tabla de Q-value obtenida:")
    print(agent.get_q_table())
    print("Tabla de política estimada:")
    agent.set_policy_table()
    print(agent.get_policy_table())
    np.save('./last_q.npy', agent.get_q_table())

    game.game.close()
