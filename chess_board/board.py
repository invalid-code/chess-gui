from chess_board.piece import Piece

from .base import BaseGroup, BaseSprite
from .constants import IMAGE_SIZE
from .pieces import Pieces


class Square(BaseSprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int],
        pos: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    @property
    def pixel_coordinate(self):
        return self.rect.topleft


class Board(BaseGroup):
    def __init__(self):
        super().__init__(
            [
                [
                    Square(
                        "img/chess_board/white_square.png",
                        (col, row),
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                    )
                    if col % 2 == 0
                    else Square(
                        "img/chess_board/black_square.png",
                        (col, row),
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                    )
                    for col in range(8)
                ]
                if row % 2 == 0
                else [
                    Square(
                        "img/chess_board/black_square.png",
                        (col, row),
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                    )
                    if col % 2 == 0
                    else Square(
                        "img/chess_board/white_square.png",
                        (col, row),
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                    )
                    for col in range(8)
                ]
                for row in range(8)
            ]
        )

        self.board_repr = [["" for _ in range(8)] for _ in range(8)]

    def sprites(self) -> list[Square]:
        return super().sprites()

    def get_clicked_square(self, pos: tuple[int, int]):
        for square in self.sprites():
            if square.rect.collidepoint(pos):
                return square

    def start_board_repr(self, pieces: Pieces):
        for pawn in pieces.pawns.sprites():
            self.board_repr[pawn.board_coordinate[1]][
                pawn.board_coordinate[0]
            ] = pawn.name
        for rook in pieces.rooks.sprites():
            self.board_repr[rook.board_coordinate[1]][
                rook.board_coordinate[0]
            ] = rook.name
        for king in pieces.kings.sprites():
            self.board_repr[king.board_coordinate[1]][
                king.board_coordinate[0]
            ] = king.name

    def update_board_repr(
        self, board_coordinate: tuple[int, int], piece: Piece
    ):
        self.board_repr[piece.board_coordinate[1]][
            piece.board_coordinate[0]
        ] = ""
        self.board_repr[board_coordinate[1]][board_coordinate[0]] = piece.name

    def has_piece(self, board_coordinate: tuple[int, int]):
        return self.board_repr[board_coordinate[1]][board_coordinate[0]] != ""
