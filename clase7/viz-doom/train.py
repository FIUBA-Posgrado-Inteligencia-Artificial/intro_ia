# Este es el script de entrenamiento. Se entrena el agente usando Q-Learning y se guarda la tabla Q.
import numpy as np

from game_logic import GameSimple, AgentQLearning, move_player

number_of_episodes = 100


if __name__ == "__main__":

    # Creamos una instancia del juego
    game = GameSimple(number_of_episodes, max_movements=15)

    # Creamos el agente
    agent = AgentQLearning(epsilon_decay= 3 / number_of_episodes)

    # Iniciamos el juego
    game.init()

    # Ciclo principal que ejecuta los episodios del juego.
    for i in range(number_of_episodes):
        print(f"Episodio #{i + 1}")

        # Iniciamos un nuevo episodio
        game.new_episode()

        sequence = 0
        start_seq = True
        pos_block_start = 0
        pos_block_end = 0
        reward = 0
        action = "stand"

        # Bucle principal del juego durante un episodio.
        while not game.is_episode_finished():

            # Obtiene el estado actual
            state_number = game.update_state()
            reward = 0

            # Dejamos que Doom Guy levante la pistola
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
                        agent.refresh_q_table(pos_block_start, pos_block_end, action, reward)
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
                        agent.refresh_q_table(game.player_position_block, None, action, reward)
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
        print("Probabilidad de exploración:", agent.epsilon)
        print("************************")

        # Decaemos la probabilidad de exploración
        agent.decay_epsilon(i)

    # Guardamos la tabla Q obtenida
    print(agent.q_table)
    np.save('./last_q.npy', agent.q_table)

    game.game.close()
