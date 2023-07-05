from .piece.groups import KingGroup, PawnGroup


class Pieces:
    def __init__(self, pieces: str) -> None:
        self.pawns = PawnGroup(pieces)
        self.kings = KingGroup(pieces)
