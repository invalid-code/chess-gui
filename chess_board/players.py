from random import choice
from typing import Optional

from .pieces import Pieces
from .types import Piece


class Player:
    def __init__(self, piece_color: str) -> None:
        self.piece_color = piece_color

        Pieces()
        self.selected_piece: Optional[Piece] = None
        self.is_check = False
        self.is_checkmate = False


class PlayerA(Player):
    def __init__(self) -> None:
        piece_color = choice(["white", "black"])
        super().__init__(piece_color)


class PlayerB(Player):
    def __init__(self, opponent: PlayerA) -> None:
        piece_color = "white" if opponent.piece_color == "black" else "black"
        super().__init__(piece_color)
