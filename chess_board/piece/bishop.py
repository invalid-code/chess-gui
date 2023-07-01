from piece import Piece, PieceGroup

from chess_board.constants import IMAGE_SIZE


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


class BlackBishops(PieceGroup):
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


class WhiteBishops(PieceGroup):
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
