import pygame as pg

from piece.queen.black_queen import BlackQueen
from piece.queen.white_queen import WhiteQueen

from .constants import IMAGE_SIZE


class BlackQueens(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackQueen(
                    (
                        4 * IMAGE_SIZE,
                        0 * IMAGE_SIZE if pieces[0] == "w" else 7 * IMAGE_SIZE,
                    ),
                    (4, 0 if pieces[0] == "w" else 7),
                )
            ]
        )


class WhiteQueens(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                WhiteQueen(
                    (
                        4 * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (
                        4,
                        7 if pieces[0] == "w" else 0,
                    ),
                )
            ]
        )
