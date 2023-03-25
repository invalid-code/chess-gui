import pygame as pg

from piece.queen.black_queen import BlackQueen
from piece.queen.white_queen import WhiteQueen

from .constants import IMAGE_SIZE


class BlackQueens(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [BlackQueen((4 * IMAGE_SIZE, 0 * IMAGE_SIZE), (4, 0))]
        )


class WhiteQueens(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [WhiteQueen((4 * IMAGE_SIZE, 7 * IMAGE_SIZE), (4, 7))]
        )
