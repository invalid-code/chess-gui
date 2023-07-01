from random import choice


class Player:
    def __init__(self) -> None:
        self.pieces = choice(["w", "b"])


class Opponent:
    def __init__(self, player: PlayerA) -> None:
        self.pieces = "w" if player.pieces == "b" else "b"
