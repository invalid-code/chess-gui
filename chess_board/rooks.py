import pygame as pg

from piece.knight.black_knight import BlackKnight
from piece.knight.white_knight import WhiteKnight

from .constants import IMAGE_SIZE


class BlackRooks(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [
                BlackKnight((index * IMAGE_SIZE, 0 * IMAGE_SIZE), (index, 0))
                for index in range(8)
                if index == 0 or index == 7
            ]
        )


class WhiteRooks(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.add(
            [
                WhiteKnight((index * IMAGE_SIZE, 7 * IMAGE_SIZE), (index, 7))
                for index in range(8)
                if index == 0 or index == 7
            ]
        )
