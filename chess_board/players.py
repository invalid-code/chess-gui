from random import choice
from typing import Literal


class Player:
    def __init__(self) -> None:
        self.piece_color: Literal["white", "black"] = choice(
            ["white", "black"]
        )


class Opponent:
    def __init__(self, opponent: Player) -> None:
        self.piece_color = (
            "white" if opponent.piece_color == "black" else "black"
        )
