import random
import numpy as np
import vizdoom as vzd

from config import Actions, AnimationConstants, POS_BLOCK_RANGE, LAST_BLOCK, FIRST_BLOCK, PLAYER_INITIAL


class Agent:
    """
    Representa un agente que interactúa con el entorno del juego VizDoom.

    Esta clase maneja la lógica del agente, incluyendo su posición, movimientos,
    recompensas y tablas de aprendizaje (Q-table y política).

    Atributos:
        movements (int): Contador de movimientos realizados
        total_reward (float): Recompensa total acumulada
        pos_block_range (tuple): Rango de posiciones válidas en bloques
        position_block (int): Bloque actual donde se encuentra el agente
        position (float): Posición exacta del agente
        player_actions_in_game (dict): Mapeo de acciones a botones del juego
        q_table (numpy.ndarray): Tabla Q que almacena valores estado-acción
        policy_table (numpy.ndarray): Tabla de política que define probabilidades de acciones
    """

    def __init__(self):
        self.movements = 0
        self.total_reward = 0

        # Ubicaciones que se puede mover el agente
        self.pos_block_range = POS_BLOCK_RANGE

        # Arrancamos sin idea de la posición, el entorno nos tiene que decir
        self.position_block = None
        self.position = None

        # Teclas que se presionan para mover el personaje
        self.player_actions_in_game = {Actions.MOV_LEFT.name: [True, False, False],   # Mover a la izquierda
                                       Actions.MOV_RIGHT.name: [False, True, False],  # Mover a la derecha
                                       Actions.STAND.name: [False, False, False],     # No realiza acción
                                       Actions.SHOOT.name: [False, False, True]}      # Dispara

        # El agente va a guardar su propia tabla, siempre se inicia en cero. No dejamos la acción Stand porque no es
        # una acción disponible, sino que sirve para las animaciones
        self.q_table = np.zeros((len(POS_BLOCK_RANGE) + 1, len(Actions) - 1), dtype=float)
        self.policy_table = np.ones_like(self.q_table) * 1/3

    def make_action(self, action_value: int) -> list:
        """
        El agente realiza una acción en el juego.

        Parámetros:
            action_value(int): Valor numérico que identifica la acción a realizar

        Retorna:
            list: Lista de booleanos que indican qué botones están presionados
        """
        return self.player_actions_in_game[Actions(action_value).name]

    def player_move(self, pos_end: int) -> list:
        """
        Determina los botones a apretar para el jugador basada en la posición actual y la posición objetivo.

        Parámetros:
            pos_end (int): Posición objetivo para el jugador.

        Retorna:
            list: Lista de booleanos que indican qué botones están presionados
        """
        action = Actions.STAND.value
        if self.position_block < pos_end:
            action = Actions.MOV_LEFT.value
        if self.position_block > pos_end:
            action = Actions.MOV_RIGHT.value
        return self.make_action(action)

    def player_shoot(self) -> list :
        """
        El jugador realiza un disparo.

        Retorna:
            list: Lista de booleanos que indican qué botones están presionados
        """
        return self.make_action(Actions.SHOOT.value)

    def player_stand(self) -> list:
        """
        El jugador se queda quieto.

        Retorna:
            list: Lista de booleanos que indican qué botones están presionados
        """
        return self.make_action(Actions.STAND.value)

    def obtain_position_block(self, pos: float) -> int:
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

    def obtain_next_block(self, action_value: Actions) -> int:
        """
        Obtiene el próximo bloque a moverse del jugador.

        Parámetros:
            action (Actions): Acción del jugador.

        Retorna:
            int: Próximo bloque a moverse del jugador.
        """
        # Movemos el jugador si corresponde moverse
        new_pos = self.position_block
        if action_value == Actions.MOV_RIGHT.value:
            if self.position_block > FIRST_BLOCK:
                new_pos -= 1
        if action_value == Actions.MOV_LEFT.value:
            if self.position_block < LAST_BLOCK:
                new_pos += 1
        return new_pos

    def get_position(self) -> int:
        """
        Obtiene la posicion actual del agente.
    
        Retorna:
            int: Obtiene en que celda se encuentra el agente.
        """
        return self.position_block

    def set_new_position(self, position: float):
        """
        Configura la posición del agente.

        Parámetros:
            position (float): Posición.
        """
        self.position = position
        self.position_block = self.obtain_position_block(position)

    def set_reward(self, reward: float):
        """
        Actualiza la recompensa acumulada del agente.

        Parámetros:
            reward (float): Valor de recompensa a sumar al total acumulado.
        """
        self.total_reward += reward

    def reset_reward(self):
        """
        Reinicia la recompensa acumulada del agente a cero.
        """
        self.total_reward = 0

    def reset_movements(self):
        """
        Reinicia los movimientos del agente a cero.
        """
        self.movements = 0

    def add_movement(self):
        """
        Incrementa el contador de movimientos del agente en uno.
        """
        self.movements += 1

    def set_q_table(self, table: np.ndarray):
        """
        Establece la tabla Q del agente.

        Parámetros:
            table (numpy.ndarray): Tabla Q.
        """
        self.q_table = table

    def set_policy_table(self):
        """
        Calcula y establece la tabla de política basada en los valores Q actuales.

        La tabla de política determina la probabilidad de seleccionar cada acción en cada estado.
        Las probabilidades se calculan normalizando los valores Q ajustados (desplazados al positivo)
        para cada estado. Si todos los valores Q son iguales, se asignan probabilidades uniformes.
        """
        num_estados, num_acciones = self.q_table.shape

        self.policy_table = np.zeros((num_estados, num_acciones), dtype=float)

        for state_idx in range(num_estados):
            q_values_for_state = self.q_table[state_idx, :]
            min_q_value_in_row = np.min(q_values_for_state)
            adjusted_q_values = q_values_for_state - min_q_value_in_row + 1e-6
            sum_adjusted_q_values = np.sum(adjusted_q_values)

            if sum_adjusted_q_values == 0:
                probabilities_for_state = np.full(num_acciones, 1.0 / num_acciones)
            else:
                probabilities_for_state = adjusted_q_values / sum_adjusted_q_values

            self.policy_table[state_idx, :] = probabilities_for_state

    def get_q_table(self) -> np.ndarray:
        """
        Metodo getter para obtener la tabla Q del agente.

        Parámetros:
            numpy.ndarray: Tabla Q.
        """
        return self.q_table

    def get_policy_table(self) -> np.ndarray:
        """
        Metodo getter para obtener la política del agente.

        Parámetros:
            numpy.ndarray: Tabla con la política
        """
        return self.policy_table

    def next_action_trained(self, pos_block: int, deterministic: bool = True) -> Actions:
        """
        Determina la próxima acción a tomar cuando el agente ya está entrenado.

        Parámetros:
            pos_block (int): Bloque de posición actual.
            deterministic (bool): Indica si el agente se va a comportar de forma deterministica o va a comportarse
                                  con cierta aleatoriedad usando la tabla de política. Por defecto, True.

        Retorna:
            Actions: Acción a realizar.
        """
        if deterministic:
            action_number = np.argmax(self.q_table[pos_block, :])
        else:
            # Si es al azar tiramos un dado, con mas probabilidad a quien tenga mayor probabilidad
            action_number = np.random.choice(self.policy_table.shape[1], p=self.policy_table[pos_block, :])

        return Actions(action_number)


class Environment:
    """
    Representa un entorno de juego simple utilizando VizDoom.

    Parámetros:
        n_episodes (int): Número de episodios a ejecutar.
        max_movements (int): Máximo de movimientos permitidos por episodio.
        monster (Agent): Objeto que representa al monstruo que el agente tiene que matar
        
    Atributos:
        number_of_episodes (int): Número total de episodios a ejecutar
        max_movements (int): Número máximo de movimientos permitidos por episodio
        animation_frame (int): Contador de frames para animaciones
        agent_in_position (bool): Indica si el agente está en su posición inicial
        monster (Agent): Instancia del agente que representa al monstruo
        game (DoomGame): Instancia del juego VizDoom
    """
    def __init__(self, n_episodes: int, max_movements: int, monster: Agent):

        self.number_of_episodes = n_episodes
        self.max_movements = max_movements

        self.animation_frame = 0
        self.agent_in_position = False

        # Agregamos al monstruo
        self.monster = monster

        # Creamos el juego de VizDoom y lo configuramos
        self.game = vzd.DoomGame()
        self.load_config_doom()

    def init(self):
        """
        Inicializa el juego.
        """
        self.game.init()

    def new_episode(self, agent: Agent):
        """
        Comienza un nuevo episodio.
        """
        self.game.new_episode()
        agent.reset_reward()
        agent.reset_movements()
        self.animation_frame = 0
        self.agent_in_position = False

        self.update_state(agent)

    def make_action(self, agent_buttons: list):
        """
        Realiza una acción en el juego.

        Parámetros:
            agent_buttons (list): Acción a realizar que corresponde a como se están apretando los tres botones
                                  disponibles.
        """
        self.game.make_action(agent_buttons)

    def _give_reward_position(self, agent: Agent) -> float:
        """
        Obtiene la recompensa basada en la posición del agente

        Parámetros:
            agent (Agent): El agente para saber cuál es su posición

        Retorna:
            float: Recompensa basada en la posición.
        """
        r = np.abs(self.monster.position_block - agent.position_block)*(-1)
        return r

    def _obtain_reward_shoot(self, agent: Agent) -> float:
        """
        Obtiene la recompensa por disparar.

        Parámetros:
            agent (Agent): El agente para saber cuál es su posición

        Retorna:
            float: Recompensa por disparar.
        """
        distance = np.abs(self.monster.position_block - agent.position_block)
        if distance == 0:
            r = 1000
        else:
            r = -20
        return r

    def obtain_all_reward(self, agent: Agent, last_action: Actions) -> float:
        """
        Obtiene la recompensa total cuando aplicar una acción

        Args:
            agent (Agent): El agente para saber cuál es su posición
            last_action (Actions): Accion usada para saber que recompensa aplicar

        Returns:
            float: Recompensa de la acción
        """
        match last_action:
            case Actions.SHOOT:
                r = self._obtain_reward_shoot(agent)
            case Actions.MOV_LEFT | Actions.MOV_RIGHT:
                r = self._give_reward_position(agent)
            case _:
                r = 0
        return r

    def update_state(self, agent: Agent) -> int:
        """
        Actualiza el estado del juego.

        Parámetros:
            agent (Agent): El agente para determinar su posicion dado por el entorno

        Retorna:
            int: Número del estado del juego.
        """
        state = self.game.get_state()
        # Obtenemos la posición del jugador y del monstruo
        for obj in state.labels:
            if obj.object_name == "Cacodemon":
                self.monster.set_new_position(obj.object_position_y)
            else:
                agent.set_new_position(obj.object_position_y)

        return state.number

    def reset_animation_fps(self):
        """
        Reinicia el contador de frames para animaciones.
        """
        self.animation_frame = 0

    def is_episode_finished(self, agent: Agent) -> bool:
        """
        Indica si el episodio ha terminado.

        Retorna:
            bool: True si el episodio ha terminado, False en caso contrario.
        """
        return self.game.is_episode_finished() or agent.movements >= self.max_movements

    def load_config_doom(self):
        """
        Configura el juego Doom con las opciones específicas.
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

        self.game.set_screen_resolution(vzd.ScreenResolution.RES_1920X1080)
        self.game.set_render_decals(True)  # Balas y sangre en las paredes
        self.game.set_render_particles(True)
        self.game.set_render_effects_sprites(True)
        self.game.set_render_corpses(True)

        # Hace que la ventana aparezca
        self.game.set_window_visible(True)

        self.game.clear_available_game_variables()
        self.game.set_episode_timeout(10000)
        self.game.set_episode_start_time(10)

        # Configuramos los botones
        self.game.set_available_buttons([vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK])

    def is_agent_in_position(self, agent: Agent) -> bool:
        """
        Secuencia de inicialización que ubica al agente en la posición inicial. En este momento el entorno toma control
        del agente para ponerlo en el lugar correcto.

        Args:
            agent (Agent): El ambiente lo mueve al jugador a donde se tiene que mover

        Returns:
            bool: Si el agente ya está en posición inicial, retorna True, sino False.

        """
        output = True
        if not self.agent_in_position:
            output = False
            self.animation_frame = 0

            # Movemos al agente en función desde donde está hacia la posición definida como PLAYER_INITIAL
            agent_action = Actions.STAND
            if agent.position_block < PLAYER_INITIAL:
                agent_action = Actions.MOV_LEFT
            if agent.position_block > PLAYER_INITIAL:
                agent_action = Actions.MOV_RIGHT

            # Usamos las animaciones para que hagan el movimiento
            while not self.animation(agent_action, agent, next_block=PLAYER_INITIAL):
                self.update_state(agent)
                continue

            # Si el agente está dentro del bloque que tiene que estar
            if agent.position_block == PLAYER_INITIAL:
                self.animation_frame = 0
                # Dejamos que se que parado un ratito para frenar toda inercia
                while not self.animation(Actions.STAND, agent):
                    self.update_state(agent)
                    continue
                # Inicializamos listo para que el agente tenga control de él mismo
                self.agent_in_position = True
                self.animation_frame = 0
                output = True

        return output

    def animation(self, action: Actions, agent: Agent, next_block: int = 0) -> bool:
        """
        Maneja las animaciones del agente en el juego.

        Esta función controla las secuencias de animación para diferentes acciones del agente,
        como disparar o moverse. Utiliza un contador de frames para sincronizar las animaciones
        y determinar cuándo debe terminar cada secuencia.

        Parámetros:
            action (Actions): La acción que se está animando actualmente
            agent (Agent): El agente que está realizando la acción
            next_block (int): El bloque objetivo al que el agente se está moviendo. No se usa en todos los casos.Por
                              defecto, 0.

        Retorna:
            bool: True si la animación ha terminado y el agente puede realizar otra acción,
                  False si la animación debe continuar.
        """

        nex_mov = False
        next_action = agent.player_stand()
        match action.name:
            case Actions.SHOOT.name:
                if self.animation_frame == AnimationConstants.ANIM_PLAYER_SHOOT:
                    next_action = agent.player_shoot()
                elif self.animation_frame == AnimationConstants.ANIM_PLAYER_WAIT_AFTER_SHOOT:
                    nex_mov = True
            case Actions.MOV_LEFT.name | Actions.MOV_RIGHT.name:
                if self.animation_frame < AnimationConstants.ANIM_MOV_STOP_FPS:
                    next_action = agent.player_move(next_block)
                elif self.animation_frame == AnimationConstants.ANIM_MOV_THINK_FPS:
                    nex_mov = True
            case _:
                if self.animation_frame == AnimationConstants.ANIM_MOV_THINK_FPS:
                    nex_mov = True
        self.make_action(next_action)
        self.animation_frame += 1
        return nex_mov


class QLearning:
    """
    Es el algoritmo Q-Learning que se va a utilizar para entrenar a un agente.

    Parámetros:
        gamma (float): Factor de descuento para las recompensas futuras. Por defecto, 0.99.
        alpha (float): Tasa de aprendizaje. Por defecto, 0.1.
        epsilon (float): Parámetro de exploración inicial. Por defecto, 1.
        epsilon_decay (float): Tasa de decaimiento de epsilon. Por defecto, 1/10.
        
    Atributos:
        gamma (float): Factor de descuento para recompensas futuras.
        alpha (float): Tasa de aprendizaje del agente.
        epsilon (float): Probabilidad de exploración actual.
        epsilon_decay (float): Tasa de decaimiento de epsilon.
        min_epsilon (float): Valor mínimo permitido para epsilon.

    """
    def __init__(self, gamma: float = 0.99, alpha: float = 0.1, epsilon: float = 1.0, epsilon_decay: float = 0.1):

        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = 0

    def next_sequence(self, agent: Agent, pos_block: int) -> Actions:
        """
        Determina la próxima acción a tomar el agente.

        Parámetros:
            agent (Agent): El agente que se va a entrenar.
            pos_block (int): Bloque de posición actual.

        Retorna:
            str: Acción a realizar.
        """
        # Exploramos
        action_number = random.randint(0, len(Actions) - 2)
        # Pero tiramos el dado a ver si explotamos o si solo explotamos
        if np.random.uniform(0, 1) >= self.epsilon:
            action_number = np.argmax(agent.q_table[pos_block, :])

        return Actions(action_number)

    def refresh_q_table(self, agent: Agent, pos_block_end: int, action: Actions, reward: float):
        """
        Actualiza la tabla Q del agente mediante la técnica indicada por Q-Learning

        Parámetros:
            agent (Agent): El agente que se va a entrenar.
            pos_block_end (int): Bloque de posición final.
            action (Actions): Acción realizada.
            reward (float): Recompensa obtenida.
        """

        # Actualizamos la tabla, una recompensa si hay un bloque al que moverse o si no.
        agent.q_table[agent.position_block, action.value] = ((1 - self.alpha) *
                                                        agent.q_table[agent.position_block, action.value] +
                                                        self.alpha * (reward + self.gamma *
                                                        max(agent.q_table[pos_block_end, :])))

    def decay_epsilon(self, n_iteration: int):
        """
        Realiza el decaimiento del parámetro de exploración epsilon.

        Parámetros:
            n_iteration (int): Índice de iteración.
        """
        self.epsilon = max(self.min_epsilon, np.exp(-self.epsilon_decay * n_iteration))
