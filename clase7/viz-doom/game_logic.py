import random
import numpy as np
import vizdoom as vzd


actions_dict = {
    0: "mov_left",
    1: "mov_right",
    2: "shoot",
}
actions_dict_inv = {
    "mov_left": 0,
    "mov_right": 1,
    "shoot": 2,
}


def move_player(pos, pos_end):
    """
    Determina la acción para el jugador basada en la posición actual y la posición objetivo.

    Parámetros:
    pos (int): Posición actual del jugador.
    pos_end (int): Posición objetivo para el jugador.

    Retorna:
    str: Acción para el jugador.
    """
    action = "stand"
    if pos > pos_end:
        action = "mov_right"
    if pos < pos_end:
        action = "mov_left"
    return action


class GameSimple:
    """
    Representa un entorno de juego simple utilizando VizDoom.
    """
    def __init__(self, n_episodes, max_movements, high_quality=False):
        """
        Inicializa el objeto JuegoSimple.

        Parámetros:
        n_episodes (int): Número de episodios a ejecutar.
        max_movements (int): Máximo de movimientos permitidos por episodio.
        high_quality (bool): Indica si se deben utilizar configuraciones de alta calidad gráfica en VizDoom.
        """
        self.number_of_episodes = n_episodes

        self.total_reward = 0
        self.movements = 0
        self.max_movements = max_movements

        # Creamos el juego de VizDoom
        self.game = vzd.DoomGame()
        self.load_config_doom(high_quality=high_quality)

        # En que bloque esta el monstruo
        self.monster_position = 0
        self.monster_pos_block = 0
        # En que bloque está el agente
        self.player_position_block = 0
        self.player_position = 0

        # Ubicaciones que se puede mover el agente
        block = 41
        self.pos_block_range = []
        for i in range(-4, 5):
            self.pos_block_range.append((self.player_position + block * i - block / 2))

        # Teclas que se presionan para mover el personaje
        self.player_actions_in_game = {"mov_left": [True, False, False],  # Mover a la izquierda
                                       "mov_right": [False, True, False],  # Mover a la derecha
                                       "stand": [False, False, False],  # No realiza acción
                                       "shoot": [False, False, True]}  # Dispara

    def init(self):
        """Inicializa el juego."""
        self.game.init()

    def new_episode(self):
        """Comienza un nuevo episodio."""
        self.game.new_episode()
        self.total_reward = 0
        self.movements = 0

    def make_action(self, action):
        """
        Realiza una acción en el juego.

        Parámetros:
        action (str): Acción a realizar.
        """
        self.game.make_action(self.player_actions_in_game[action])

    def obtain_player_next_block(self, action):
        """
        Obtiene el próximo bloque a moverse del jugador.

        Parámetros:
        action (str): Acción del jugador.

        Retorna:
        int: Próximo bloque a moverse del jugador.
        """
        # Movemos el jugador si corresponde moverse
        new_pos = self.player_position_block
        if action == "mov_left":
            if self.player_position_block < 10:
                new_pos -= 1
        if action == "mov_right":
            if self.player_position_block > 0:
                new_pos += 1
        return new_pos

    def player_shoot(self):
        """El jugador realiza un disparo."""
        self.game.make_action(self.player_actions_in_game["shoot"])

    def player_stand(self):
        """El jugador se queda quieto."""
        self.game.make_action(self.player_actions_in_game["stand"])

    def obtain_reward_position(self):
        """
        Obtiene la recompensa basada en la posición.

        Retorna:
        int: Recompensa basada en la posición.
        """
        r = np.abs(self.monster_pos_block - self.player_position_block)*(-1)
        return r

    def obtain_reward_shoot(self):
        """
        Obtiene la recompensa por disparar.

        Retorna:
        int: Recompensa por disparar.
        """
        distance = np.abs(self.monster_pos_block - self.player_position_block)
        if distance == 0:
            r = 1000
        else:
            r = -20
        return r

    def update_state(self):
        """
        Actualiza el estado del juego.

        Retorna:
        int: Número de estado.
        """
        state = self.game.get_state()
        # Obtenemos la posición del jugador y del monstruo
        for obj in state.labels:
            if obj.object_name == "Cacodemon":
                self.monster_position = obj.object_position_y
                self.monster_pos_block = self.obtain_position_block(self.monster_position)

            else:
                self.player_position = obj.object_position_y
                self.player_position_block = self.obtain_position_block(self.player_position)


        return state.number

    def is_episode_finished(self):
        """
        Indica si el episodio ha terminado.

        Retorna:
        bool: True si el episodio ha terminado, False en caso contrario.
        """
        return self.game.is_episode_finished() or self.movements >= self.max_movements

    def obtain_position_block(self, pos):
        """
        Obtiene el bloque de la posición dada.

        Parámetros:
        pos (float): Posición.

        Retorna:
        int: Bloque de la posición.
        """
        for i, value in enumerate(self.pos_block_range):
            if pos < value:
                return i

        return len(self.pos_block_range)

    def load_config_doom(self, high_quality=False):
        """
        Configura el juego Doom con las opciones específicas.

        Parámetros:
        high_quality (bool): Indica si se deben utilizar configuraciones de alta calidad gráfica en VizDoom.
        """
        # Cargamos el wad
        self.game.set_doom_scenario_path("./deterministic.wad")
        # Elegimos el mapa 01
        self.game.set_doom_map("map01")

        self.game.set_depth_buffer_enabled(False)
        self.game.set_labels_buffer_enabled(True)
        self.game.set_automap_buffer_enabled(False)
        self.game.set_objects_info_enabled(True)
        self.game.set_sectors_info_enabled(True)
        self.game.set_render_hud(True)
        self.game.set_render_minimal_hud(True)
        self.game.set_render_crosshair(False)
        self.game.set_render_weapon(True)
        self.game.set_render_messages(False)
        self.game.set_render_screen_flashes(True)
        self.game.set_sound_enabled(False)
        self.game.set_console_enabled(False)

        self.game.set_mode(vzd.Mode.PLAYER)

        if high_quality:
            self.game.set_screen_resolution(vzd.ScreenResolution.RES_1920X1080)
            self.game.set_render_decals(True)  # Balas y sangre en las paredes
            self.game.set_render_particles(True)
            self.game.set_render_effects_sprites(True)
            self.game.set_render_corpses(True)
        else:
            self.game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)
            self.game.set_render_decals(False)
            self.game.set_render_particles(False)
            self.game.set_render_effects_sprites(False)
            self.game.set_render_corpses(False)

        # Hace que la ventana aparezca
        self.game.set_window_visible(True)

        self.game.clear_available_game_variables()
        self.game.set_episode_timeout(10000)
        self.game.set_episode_start_time(10)

        # Configuramos los botones
        self.game.set_available_buttons([vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK])


class AgentQLearning:
    """
    Representa un agente que utiliza el algoritmo Q-Learning para aprender a jugar.
    """
    def __init__(self, gamma=0.99, alpha=0.1, epsilon=1, epsilon_decay=1/10, number_of_state=11):
        """
        Inicializa el objeto AgenteQLearning.

        Parámetros:
        gamma (float): Factor de descuento para las recompensas futuras. Por defecto, 0.99.
        alpha (float): Tasa de aprendizaje. Por defecto, 0.1.
        epsilon (float): Parámetro de exploración inicial. Por defecto, 1.
        epsilon_decay (float): Tasa de decaimiento de epsilon. Por defecto, 1/10.
        number_of_state (int): Número de estados. Por defecto, 11.
        """
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = 0

        self.number_of_actions = len(actions_dict)

        self.q_table = np.zeros((number_of_state, self.number_of_actions))

    def set_q_table(self, table):
        """
        Establece la tabla Q del agente.

        Parámetros:
        table (numpy.ndarray): Tabla Q.
        """
        self.q_table = table

    def next_sequence(self, pos_block, only_exploit=False):
        """
        Determina la próxima acción a tomar.

        Parámetros:
        pos_block (int): Bloque de posición actual.
        only_exploit (bool): Indica si se debe realizar solo la explotación. Por defecto, False.

        Retorna:
        str: Acción a realizar.
        """
        # Exploramos
        action_number = random.randint(0, len(actions_dict) - 1)
        # Pero tiramos el dado a ver si explotamos o si solo explotamos
        if np.random.uniform(0, 1) >= self.epsilon or only_exploit:
            action_number = np.argmax(self.q_table[pos_block, :])

        return actions_dict[action_number]

    def refresh_q_table(self, pos_block_init, pos_block_end, action, reward):
        """
        Actualiza la tabla Q del agente mediante la técnica indicada por Q-Learning

        Parámetros:
        pos_block_init (int): Bloque de posición inicial.
        pos_block_end (int): Bloque de posición final.
        action (str): Acción realizada.
        reward (float): Recompensa obtenida.
        """

        action_number = actions_dict_inv[action]

        # Actualizamos la tabla, una recompensa si hay un bloque al que moverse o si no.
        if pos_block_end:
            self.q_table[pos_block_init, action_number] = ((1 - self.alpha) *
                                                           self.q_table[pos_block_init, action_number] +
                                                           self.alpha * (reward + self.gamma *
                                                           max(self.q_table[pos_block_end, :])))
        else:
            self.q_table[pos_block_init, action_number] = ((1 - self.alpha) *
                                                           self.q_table[pos_block_init, action_number]
                                                           + self.alpha * (reward + self.gamma))

    def decay_epsilon(self, index):
        """
        Realiza el decaimiento del parámetro de exploración epsilon.

        Parámetros:
        index (int): Índice de iteración.
        """
        self.epsilon = max(self.min_epsilon, np.exp(-self.epsilon_decay * index))
