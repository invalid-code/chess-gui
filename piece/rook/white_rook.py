import pygame as pg

from chess_board.constants import IMAGE_SIZE

from . import Rook


class WhiteRook(Rook):
    name = "wr"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.image = pg.transform.scale(
            pg.image.load("img/white_rook.png").convert_alpha(),
            (IMAGE_SIZE, IMAGE_SIZE),
        )
