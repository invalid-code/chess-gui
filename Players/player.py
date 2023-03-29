from random import choice


class Player:
    def __init__(self) -> None:
        self.pieces = choice(["w", "b"])
