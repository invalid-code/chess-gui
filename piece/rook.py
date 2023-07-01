from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece import Piece


class Rook(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Rook(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def allowed_move(self, x: int, y: int, board: list[list[None | str]]):
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
                return True
            if self.board_coordinate[1] - i == y:
                return True
            if self.board_coordinate[0] + i == x:
                return True
            if self.board_coordinate[0] - i == x:
                return True
        return False


class WhiteRook(Rook):
    name = "wr"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_rook.png", pos, board_coordinate)


class BlackRook(Rook):
    name = "br"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_rook.png", pos, board_coordinate)


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

    def sprites(self) -> list[BlackRook]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[BlackRook]:
        for black_rook in self.sprites():
            if black_rook.rect.collidepoint(pos):
                return black_rook
        return None


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

    def sprites(self) -> list[WhiteRook]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[WhiteRook]:
        for white_rook in self.sprites():
            if white_rook.rect.collidepoint(pos):
                return white_rook
        return None
