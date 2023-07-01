from random import choice


class Player:
    def __init__(self) -> None:
        self.pieces = choice(["white", "black"])


class Opponent:
    def __init__(self, player: Player) -> None:
        self.pieces = "white" if player.pieces == "black" else "black"
