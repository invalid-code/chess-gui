import pygame as pg

from piece.knight.black_knight import BlackKnight
from piece.knight.white_knight import WhiteKnight

from .constants import IMAGE_SIZE


class BlackKnights(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackKnight(
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
                if index == 1 or index == 6
            ]
        )


class WhiteKnights(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteKnight(
                    (
                        index * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (
                        index,
                        7 if pieces[0] == "w" else 0,
                    ),
                )
                for index in range(8)
                if index == 1 or index == 6
            ]
        )
