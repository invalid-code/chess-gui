import pygame as pg

from chess_board.constants import IMAGE_SIZE

from . import Queen


class WhiteQueen(Queen):
    name = "wq"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.image = pg.transform.scale(
            pg.image.load("img/white_queen.png").convert_alpha(),
            (IMAGE_SIZE, IMAGE_SIZE),
        )
