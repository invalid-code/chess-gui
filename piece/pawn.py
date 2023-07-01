from chess_board.constants import IMAGE_SIZE

from . import Piece, Pieces


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

    def allowed_move(self, x: int, y: int):
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


class BlackPawns(Pieces):
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


class WhitePawns(Pieces):
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
