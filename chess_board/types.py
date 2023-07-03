from typing import Optional, TypedDict

from .piece import Bishop, King, Knight, Pawn, Queen, Rook

Piece = Pawn | Knight | Bishop | Rook | Queen | King


class Check(TypedDict):
    is_check: bool
    pieces: Optional[str]
