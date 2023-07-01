from chess_board.constants import IMAGE_SIZE

from . import Piece, PieceGroup


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


class BlackPawns(PieceGroup):
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


class WhitePawns(PieceGroup):
    def __init__(self, pieces: str):
        super().__init__(
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
