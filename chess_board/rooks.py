import pygame as pg

from piece.rook.black_rook import BlackRook
from piece.rook.white_rook import WhiteRook

from .constants import IMAGE_SIZE


class BlackRooks(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackRook(
                    (
                        index * IMAGE_SIZE,
                        0 * IMAGE_SIZE if pieces[0] == "w" else 7 * IMAGE_SIZE,
                    ),
                    (
                        index,
                        0 if pieces[0] == "w" else 7,
                    ),
                )
                for index in range(8)
                if index == 0 or index == 7
            ]
        )


class WhiteRooks(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteRook(
                    (
                        index * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (index, 7 if pieces[0] == "w" else 0),
                )
                for index in range(8)
                if index == 0 or index == 7
            ]
        )
