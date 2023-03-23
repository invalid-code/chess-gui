import pygame as pg

from piece.pawn.black_pawn import BlackPawn
from piece.pawn.white_pawn import WhitePawn

from .constants import IMAGE_SIZE


class BlackPawns(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [
                BlackPawn((index * IMAGE_SIZE, 1 * IMAGE_SIZE), (index, 1))
                for index in range(8)
            ]
        )


class WhitePawns(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.add(
            [
                WhitePawn((index * IMAGE_SIZE, 6 * IMAGE_SIZE), (index, 6))
                for index in range(8)
            ]
        )
