from chess_board.base import BaseGroup
from chess_board.constants import IMAGE_SIZE
from chess_board.types import Piece

from . import Bishop, King, Knight, Pawn, Queen, Rook


class PieceGroup(BaseGroup):
    pass


class PawnGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        if pieces == "white":
            self.add(
                [
                    Pawn(
                        "w",
                        "img/white_pawn.png",
                        (i * IMAGE_SIZE, 6 * IMAGE_SIZE),
                        (i, 6),
                        True,
                    )
                    for i in range(8)
                ],
                [
                    Pawn(
                        "b",
                        "img/black_pawn.png",
                        (i * IMAGE_SIZE, 1 * IMAGE_SIZE),
                        (i, 1),
                        False,
                    )
                    for i in range(8)
                ],
            )
        else:
            self.add(
                [
                    Pawn(
                        "b",
                        "img/black_pawn.png",
                        (i * IMAGE_SIZE, 6 * IMAGE_SIZE),
                        (i, 6),
                        True,
                    )
                    for i in range(8)
                ],
                [
                    Pawn(
                        "w",
                        "img/white_pawn.png",
                        (i * IMAGE_SIZE, 1 * IMAGE_SIZE),
                        (i, 1),
                        False,
                    )
                    for i in range(8)
                ],
            )

    def sprites(self) -> list[Pawn]:
        return super().sprites()


class KnightGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        x_pos = [1, 6]
        if pieces == "white":
            self.add(
                [
                    Knight(
                        "w",
                        "img/white_knight.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Knight(
                        "b",
                        "img/black_knight.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )
        else:
            self.add(
                [
                    Knight(
                        "b",
                        "img/black_knight.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Knight(
                        "w",
                        "img/white_knight.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )

    def sprites(self) -> list[Rook]:
        return super().sprites()


class BishopGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        x_pos = [2, 5]
        if pieces == "white":
            self.add(
                [
                    Bishop(
                        "w",
                        "img/white_bishop.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Bishop(
                        "b",
                        "img/black_bishop.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )
        else:
            self.add(
                [
                    Bishop(
                        "b",
                        "img/black_bishop.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Bishop(
                        "w",
                        "img/white_bishop.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )

    def sprites(self) -> list[Bishop]:
        return super().sprites()


class RookGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        x_pos = [0, 7]
        if pieces == "white":
            self.add(
                [
                    Rook(
                        "w",
                        "img/white_rook.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Rook(
                        "b",
                        "img/black_rook.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )
        else:
            self.add(
                [
                    Rook(
                        "b",
                        "img/black_rook.png",
                        (i * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (i, 7),
                        True,
                    )
                    for i in x_pos
                ],
                [
                    Rook(
                        "w",
                        "img/white_rook.png",
                        (i * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (i, 0),
                        False,
                    )
                    for i in x_pos
                ],
            )

    def sprites(self) -> list[Rook]:
        return super().sprites()


class QueenGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        if pieces == "white":
            self.add(
                Queen(
                    "w",
                    "img/white_queen.png",
                    (3 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                    (3, 7),
                    True,
                ),
                Queen(
                    "b",
                    "img/black_queen.png",
                    (3 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                    (3, 0),
                    False,
                ),
            )
        else:
            self.add(
                Queen(
                    "b",
                    "img/black_queen.png",
                    (3 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                    (3, 7),
                    True,
                ),
                Queen(
                    "w",
                    "img/white_queen.png",
                    (3 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                    (3, 0),
                    False,
                ),
            )

    def sprites(self) -> list[Queen]:
        return super().sprites()


class KingGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        if pieces == "white":
            self.add(
                King(
                    "w",
                    "img/white_king.png",
                    (4 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                    (4, 7),
                    True,
                ),
                King(
                    "b",
                    "img/black_king.png",
                    (4 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                    (4, 0),
                    False,
                ),
            )
        else:
            self.add(
                King(
                    "b",
                    "img/black_king.png",
                    (4 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                    (4, 7),
                    True,
                ),
                King(
                    "w",
                    "img/white_king.png",
                    (4 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                    (4, 0),
                    False,
                ),
            )

    def sprites(self) -> list[King]:
        return super().sprites()
