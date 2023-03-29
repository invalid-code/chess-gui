import pygame as pg

from piece.bishop.black_bishop import BlackBishop
from piece.bishop.white_bishop import WhiteBishop

from .constants import IMAGE_SIZE


class BlackBishops(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackBishop(
                    (
                        index * IMAGE_SIZE,
                        0 * IMAGE_SIZE if pieces[0] == "w" else 7 * IMAGE_SIZE,
                    ),
                    (index, 0),
                )
                for index in range(8)
                if index == 2 or index == 5
            ]
        )


class WhiteBishops(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteBishop(
                    (
                        index * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (index, 7),
                )
                for index in range(8)
                if index == 2 or index == 5
            ]
        )
