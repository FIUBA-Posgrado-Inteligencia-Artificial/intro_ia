# Este es el script de testeo. Se evalúa el agente
import numpy as np

from game_logic import GameSimple, AgentQLearning, move_player

qtable_trained = np.load('./last_q.npy')

number_of_episodes = 20
reward_all = []

if __name__ == "__main__":

    # Creamos una instancia del juego
    game = GameSimple(number_of_episodes, max_movements=10, high_quality=True)

    # Creamos el agente
    agent = AgentQLearning(epsilon=0, epsilon_decay=0)

    # Agregamos la tabla entrenada
    agent.set_q_table(qtable_trained)

    # Iniciamos el juego
    game.init()

    # Ciclo principal que ejecuta los episodios del juego.
    for i in range(number_of_episodes):
        print(f"Episodio #{i + 1}")

        # Iniciamos un nuevo episodio
        game.new_episode()

        sequence = 0
        start_seq = True
        pos_block_end = 0
        reward = 0
        action = "stand"

        # Bucle principal del juego durante un episodio.
        while not game.is_episode_finished():

            # Obtiene el estado actual
            state_number = game.update_state()

            # Dejamos que Doom guy levante la pistola
            if state_number <= 40:
                game.player_stand()
            else:

                # Iniciamos una secuencia
                if start_seq:
                    # Obtenemos la siguiente secuencia
                    pos_block_start = game.player_position_block
                    action = agent.next_sequence(pos_block_start, only_exploit=False)
                    pos_block_end = game.obtain_player_next_block(action)
                    start_seq = False

                # Secuencia de movimiento de izquierda o derecha
                if action != "shoot":
                    if sequence < 60:
                        # Movemos el personaje hasta que se acomoda
                        game.make_action(move_player(game.player_position_block, pos_block_end))
                    elif sequence == 60:
                        # Se para en la zona
                        game.player_stand()
                        # Se castiga la distancia del jugador al monstruo
                        reward = game.obtain_reward_position()
                    elif sequence == 70:
                        # Va a la siguiente secuencia
                        game.player_stand()
                        start_seq = True
                        sequence = 0
                        game.movements += 1
                    else:
                        # Jugador quieto
                        game.player_stand()
                # Secuencia de disparo
                else:
                    if sequence == 10:
                        game.player_shoot()
                        reward = game.obtain_reward_shoot()
                    elif sequence == 50:
                        game.player_stand()
                        start_seq = True
                        sequence = 0
                        game.movements += 1
                    else:
                        game.player_stand()

                sequence += 1

            game.total_reward += reward

        # Mostramos como fue el episodio
        print("Episodio terminado.")
        print("Recompensa total:", game.total_reward)
        print("************************")
        reward_all.append(game.total_reward)
    game.game.close()

    print("Evaluación terminada")
    print("Recompensa promedio por episodio:", np.mean(np.array(reward_all)))
    print("Desvío estándar de recompensa por episodio:", np.std(np.array(reward_all)))
