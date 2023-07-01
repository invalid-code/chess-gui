from piece import Piece, PieceGroup

from chess_board.constants import IMAGE_SIZE


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


class BlackRooks(PieceGroup):
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


class WhiteRooks(PieceGroup):
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
