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

    def allowed_move(self, x: int, y: int, board: list[list[None | str]]):
        for i in range(8):
            if board[i][i]:
                return False
            if (
                board[i][self.board_coordinate[0]]
                or board[self.board_coordinate[1]][i]
            ):
                return False
            if self.board_coordinate[1] + i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
            if self.board_coordinate[1] - i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
        return False

    def allowed_take(self, x: int, y: int):
        for i in range(8):
            if self.board_coordinate[1] + i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
            if self.board_coordinate[1] - i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
        return False
