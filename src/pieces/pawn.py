from attr import dataclass
from square import Square
from src import Player
from src.pieces.piece import Piece


@dataclass
class Pawn(Piece):
    current_square: Square
    player: Player
