from typing import Optional

import pygame as pg

from .base import BaseGroup, BaseSprite
from .types import IMAGE_SIZE


class Square(BaseSprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int],
        pos: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)


class WhiteSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
        board_coordinate: tuple[int, int] = (0, 0),
    ) -> None:
        white_square = pg.image.load(
            "img/chess_board/white_square.png"
        ).convert_alpha()
        super().__init__(pos, white_square, board_coordinate)


class BlackSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
        board_coordinate: tuple[int, int] = (0, 0),
    ) -> None:
        black_square = pg.image.load(
            "img/chess_board/black_square.png"
        ).convert_alpha()
        super().__init__(pos, black_square, board_coordinate)


class Board(BaseGroup):
    def __init__(self):
        super().__init__(
            [
                [
                    WhiteSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    if col % 2 == 0
                    else BlackSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    for col in range(8)
                ]
                if row % 2 == 0
                else [
                    BlackSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    if col % 2 == 0
                    else WhiteSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    for col in range(8)
                ]
                for row in range(8)
            ]
        )

        self.board_repr = [["" for _ in range(8)] for _ in range(8)]

    def sprites(self) -> list[WhiteSquare | BlackSquare]:
        return super().sprites()

    def get_clicked_square(
        self, pos: tuple[int, int]
    ) -> Optional[WhiteSquare | BlackSquare]:
        for square in self.sprites():
            if square.rect.collidepoint(pos):
                return square
        return None
