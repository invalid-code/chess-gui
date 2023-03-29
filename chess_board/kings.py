import pygame as pg

from piece.king.black_king import BlackKing
from piece.king.white_king import WhiteKing

from .constants import IMAGE_SIZE


class BlackKings(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackKing(
                    (
                        3 * IMAGE_SIZE,
                        0 * IMAGE_SIZE if pieces[0] == "w" else 7 * IMAGE_SIZE,
                    ),
                    (3, 0),
                )
            ]
        )


class WhiteKings(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteKing(
                    (
                        3 * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (3, 7),
                )
            ]
        )
