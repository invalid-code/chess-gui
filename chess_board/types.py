from enum import Enum

from .piece.bishop import BlackBishop, WhiteBishop
from .piece.king import BlackKing, WhiteKing
from .piece.knight import BlackKnight, WhiteKnight
from .piece.pawn import BlackPawn, WhitePawn
from .piece.queen import BlackQueen, WhiteQueen
from .piece.rook import BlackRook, WhiteRook

IMAGE_SIZE = 57


class Turn(Enum):
    WHITE = 0
    BLACK = 1


Piece = (
    WhitePawn
    | BlackPawn
    | WhiteKnight
    | BlackKnight
    | WhiteBishop
    | BlackBishop
    | WhiteRook
    | BlackRook
    | WhiteQueen
    | BlackQueen
    | WhiteKing
    | BlackKing
)
