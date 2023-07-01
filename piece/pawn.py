from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE

from . import Piece


class Pawn(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)
        self.first_move = True

    def __repr__(self) -> str:
        return f"Pawn(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive}, first_move={self.first_move})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}\nfirst move is {self.first_move}"

    def allowed_move(self, x: int, y: int, _):
        if self.board_coordinate[0] == x:
            if self.first_move:
                if self.board_coordinate[1] - 2 == y:
                    return True
            if self.board_coordinate[1] - 1 == y:
                return True
        return False

    def allowed_take(self, x: int, y: int):
        if self.board_coordinate[1] - 1 == y:
            if (
                self.board_coordinate[0] + 1 == x
                or self.board_coordinate[0] - 1 == x
            ):
                return True
        return False


class WhitePawn(Pawn):
    name = "wp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_pawn.png", pos, board_coordinate)


class BlackPawn(Pawn):
    name = "bp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_pawn.png", pos, board_coordinate)


class BlackPawns(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackPawn(
                    (
                        index * IMAGE_SIZE,
                        1 * IMAGE_SIZE if pieces[0] == "w" else 6 * IMAGE_SIZE,
                    ),
                    (
                        index,
                        1 if pieces[0] == "w" else 6,
                    ),
                )
                for index in range(8)
            ]
        )

    def sprites(self) -> list[BlackPawn]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[BlackPawn]:
        for black_pawn in self.sprites():
            if black_pawn.rect.collidepoint(pos):
                return black_pawn
        return None


class WhitePawns(pg.sprite.Group):
    def __init__(self, pieces: str):
        super().__init__()
        self.add(
            [
                WhitePawn(
                    (
                        index * IMAGE_SIZE,
                        6 * IMAGE_SIZE if pieces[0] == "w" else 1 * IMAGE_SIZE,
                    ),
                    (
                        index,
                        6 if pieces[0] == "w" else 1,
                    ),
                )
                for index in range(8)
            ]
        )

    def sprites(self) -> list[WhitePawn]:
        return super().sprites()

    def is_being_clicked(self, pos: tuple[int, int]) -> Optional[WhitePawn]:
        for white_pawn in self.sprites():
            if white_pawn.rect.collidepoint(pos):
                return white_pawn
        return None
