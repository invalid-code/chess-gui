from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece import Piece


class King(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"King(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def allowed_move(self, x: int, y: int):
        if (
            self.board_coordinate[0] - 1 == x
            or self.board_coordinate[0] + 1 == x
        ):
            if (
                self.board_coordinate[1] - 1 == y
                or self.board_coordinate[1] + 1 == y
            ):
                return True
            return True
        if (
            self.board_coordinate[1] - 1 == y
            or self.board_coordinate[1] + 1 == y
        ):
            if (
                self.board_coordinate[0] - 1 == x
                or self.board_coordinate[0] + 1 == x
            ):
                return True
            return True

        return False

    def allowed_take(self, x: int, y: int):
        if (
            self.board_coordinate[0] - 1 == x
            or self.board_coordinate[0] + 1 == x
        ):
            if (
                self.board_coordinate[1] - 1 == y
                or self.board_coordinate[1] + 1 == y
            ):
                return True
            return True
        if (
            self.board_coordinate[1] - 1 == y
            or self.board_coordinate[1] + 1 == y
        ):
            if (
                self.board_coordinate[0] - 1 == x
                or self.board_coordinate[0] + 1 == x
            ):
                return True
            return True
        return False


class BlackKing(King):
    name = "bk"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_king.png", pos, board_coordinate)


class WhiteKing(King):
    name = "wk"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_king.png", pos, board_coordinate)


class BlackKings(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackKing(
                    (
                        3 * IMAGE_SIZE,
                        0 * IMAGE_SIZE if pieces[0] == "w" else 7 * IMAGE_SIZE,
                    ),
                    (
                        3,
                        0 if pieces[0] == "w" else 7,
                    ),
                )
            ]
        )

    def sprites(self) -> list[BlackKing]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[BlackKing]:
        for black_king in self.sprites():
            if black_king.rect.collidepoint(pos):
                return black_king
        return None


class WhiteKings(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteKing(
                    (
                        3 * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (3, 7 if pieces[0] == "w" else 0),
                )
            ]
        )

    def sprites(self) -> list[WhiteKing]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[WhiteKing]:
        for white_king in self.sprites():
            if white_king.rect.collidepoint(pos):
                return white_king
        return None
