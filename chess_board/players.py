from random import choice


class PlayerA:
    def __init__(self) -> None:
        self.pieces = choice(["w", "b"])


class PlayerB:
    def __init__(self, player: PlayerA) -> None:
        self.pieces = "w" if player.pieces == "b" else "b"
