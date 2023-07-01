from random import choice


class Player:
    name = "w"

    def __init__(self) -> None:
        self.pieces = choice(["w", "b"])
