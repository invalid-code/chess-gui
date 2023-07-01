from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece import Piece


class Queen(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Queen(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def allowed_move(self, x: int, y: int, board: list[list[None | str]]):
        # bishop move rules
        if x < self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        if x < self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        # rook move rules
        if x == self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x == self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x < self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] + i == x
                ):
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


class BlackQueen(Queen):
    name = "bq"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_queen.png", pos, board_coordinate)


class WhiteQueen(Queen):
    name = "bq"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_queen.png", pos, board_coordinate)


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

    def sprites(self) -> list[BlackQueen]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[BlackQueen]:
        for black_queen in self.sprites():
            if black_queen.rect.collidepoint(pos):
                return black_queen
        return None


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

    def sprites(self) -> list[WhiteQueen]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[WhiteQueen]:
        for white_queen in self.sprites():
            if white_queen.rect.collidepoint(pos):
                return white_queen
        return None
