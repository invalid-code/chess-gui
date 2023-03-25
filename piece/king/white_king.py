import pygame as pg

from chess_board.constants import IMAGE_SIZE

from . import King


class WhiteKing(King):
    name = "wk"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.image = pg.transform.scale(
            pg.image.load("img/white_king.png").convert_alpha(),
            (IMAGE_SIZE, IMAGE_SIZE),
        )

    def allowed_move(self, x: int, y: int):
        # if self.first_move:
        #     if (
        #         self.board_coordinate[1] - 2 == y
        #         or self.board_coordinate[1] - 1 == y
        #     ) and self.board_coordinate[0] == x:
        #         return True
        # else:
        #     if (
        #         self.board_coordinate[1] - 1 == y
        #         and self.board_coordinate[0] == x
        #     ):
        #         return True
        # return False
        pass

    def allowed_take(self, x: int, y: int):
        if self.board_coordinate[1] - 1 == y and (
            self.board_coordinate[0] + 1 == x
            or self.board_coordinate[0] - 1 == x
        ):
            return True
        return False
