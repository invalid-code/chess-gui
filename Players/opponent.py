from .player import Player


class Opponent:
    def __init__(self, player: Player) -> None:
        self.pieces = "w" if player.pieces == "b" else "b"
