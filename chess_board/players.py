from random import choice


class Player:
    def __init__(self) -> None:
        self.piece_color = choice(["white", "black"])


class Opponent:
    def __init__(self, opponent: Player) -> None:
        self.piece_color = (
            "white" if opponent.piece_color == "black" else "black"
        )
