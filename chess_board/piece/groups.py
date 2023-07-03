from typing import Optional

from chess_board.base import BaseGroup
from chess_board.constants import IMAGE_SIZE
from chess_board.types import Piece

from . import Bishop, King, Knight, Pawn, Queen, Rook


class PieceGroup(BaseGroup):
    def sprites(self) -> list[Piece]:
        return super().sprites()

    def start_board_repr(self, board: list[list[str]]):
        for piece in self.sprites():
            piece.set_board_repr(board, piece.name)

    def is_clicked(self, pos: tuple[int, int]) -> Optional[Piece]:
        for piece in self.sprites():
            if piece.rect.collidepoint(pos):
                return piece
        return None


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
    pass


class BishopGroup(PieceGroup):
    pass


class RookGroup(PieceGroup):
    pass


class QueenGroup(PieceGroup):
    pass


class KingGroup(PieceGroup):
    def __init__(self, pieces: str) -> None:
        super().__init__()
        if pieces == "white":
            self.add(
                [
                    King(
                        "w",
                        "img/white_king.png",
                        (4 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (4, 7),
                        True,
                    )
                ],
                [
                    King(
                        "b",
                        "img/black_king.png",
                        (4 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (4, 0),
                        False,
                    )
                ],
            )
        else:
            self.add(
                [
                    King(
                        "b",
                        "img/black_king.png",
                        (4 * IMAGE_SIZE, 7 * IMAGE_SIZE),
                        (4, 7),
                        True,
                    )
                ],
                [
                    King(
                        "w",
                        "img/white_king.png",
                        (4 * IMAGE_SIZE, 0 * IMAGE_SIZE),
                        (4, 0),
                        False,
                    )
                ],
            )

    def sprites(self) -> list[King]:
        return super().sprites()
