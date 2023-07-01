from piece import Piece, PieceGroup

from chess_board.constants import IMAGE_SIZE


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


class BlackQueens(PieceGroup):
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


class WhiteQueens(PieceGroup):
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
