from typing import Protocol

from src.constants import Player
from src.square import Square


class Piece(Protocol):
    def __init__(self, player: Player, current_square: Square) -> None:
        """"""

    def move(self, next_square: Square) -> None:
        """"""
