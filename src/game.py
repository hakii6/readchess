import numpy as np


class Game:
    def __init__(self, seconds_per_player=300, bonus_seconds_per_move=3) -> None:
        self.seconds_per_player = seconds_per_player
        self.bonus_seconds_per_move = bonus_seconds_per_move
        self.squares = np.zeros([8, 8])


class Move:
    def __init__(self, start_square, end_square) -> None:
        self.start_square = start_square
        self.end_square = end_square


class Turn:
    def __init__(self, player_color) -> None:
        self.player_color = player_color
