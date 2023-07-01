from chess_board.constants import IMAGE_SIZE

from . import Piece, PieceGroup


class BlackKnight(Knight):
    name = "bk"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/black_knight.png", pos, board_coordinate)


class WhiteKnight(Knight):
    name = "wk"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__("img/white_knight.png", pos, board_coordinate)


class BlackKnights(PieceGroup):
    def __init__(self, pieces: str):
        super().__init__(
            [
                BlackKnight(
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
                if index == 1 or index == 6
            ]
        )


class WhiteKnights(PieceGroup):
    def __init__(self, pieces: str):
        super().__init__(
            [
                WhiteKnight(
                    (
                        index * IMAGE_SIZE,
                        7 * IMAGE_SIZE if pieces[0] == "w" else 0 * IMAGE_SIZE,
                    ),
                    (
                        index,
                        7 if pieces[0] == "w" else 0,
                    ),
                )
                for index in range(8)
                if index == 1 or index == 6
            ]
        )
