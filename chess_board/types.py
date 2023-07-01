from enum import Enum

from .piece import Bishop, King, Knight, Pawn, Queen, Rook

IMAGE_SIZE = 57


class Turn(Enum):
    WHITE = 0
    BLACK = 1


Piece = Pawn | Knight | Bishop | Rook | Queen | King
