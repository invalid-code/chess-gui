from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece import Piece


class Bishop(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Bishop(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def allowed_move(self, x: int, y: int, board: list[list[None | str]]):
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

        return False

    def allowed_take(self, x: int, y: int):
        for i in range(8):
            if (
                self.board_coordinate[1] + i == y
                and self.board_coordinate[0] + i == x
            ):
                return True
            if (
                self.board_coordinate[1] + i == y
                and self.board_coordinate[0] - i == x
            ):
                return True
            if (
                self.board_coordinate[1] - i == y
                and self.board_coordinate[0] - i == x
            ):
                return True
            if (
                self.board_coordinate[1] - i == y
                and self.board_coordinate[0] + i == x
            ):
                return True
        return False


class WhiteBishop(Bishop):
    name = "wb"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_bishop.png", pos, board_coordinate)


class BlackBishop(Bishop):
    name = "bb"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_bishop.png", pos, board_coordinate)


class BlackBishops(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackBishop(
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
                if index == 2 or index == 5
            ]
        )

    def sprites(self) -> list[BlackBishop]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[BlackBishop]:
        for black_bishop in self.sprites():
            if black_bishop.rect.collidepoint(pos):
                return black_bishop
        return None


class WhiteBishops(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhiteBishop(
                    (
                        index * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (index, 7 if pieces[0] == "w" else 0),
                )
                for index in range(8)
                if index == 2 or index == 5
            ]
        )

    def sprites(self) -> list[WhiteBishop]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[WhiteBishop]:
        for white_bishop in self.sprites():
            if white_bishop.rect.collidepoint(pos):
                return white_bishop
        return None
