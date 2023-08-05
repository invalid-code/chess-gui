from pygame._sdl2 import messagebox

from chess_board.base import BaseSprite
from chess_board.constants import IMAGE_SIZE


class Piece(BaseSprite):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        board_coordinate: tuple[int, int],
        pos: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)
        self.piece_color = piece_color
        self.is_player_piece = is_player_piece

    def move(
        self,
        board_coordinate: tuple[int, int],
    ):
        self.rect.topleft = (
            board_coordinate[0] * IMAGE_SIZE,
            board_coordinate[1] * IMAGE_SIZE,
        )
        self.board_coordinate = board_coordinate

    def allowed_move(self, x: int, y: int):
        return (
            self.board_coordinate[0] - 1 == x
            or self.board_coordinate[0] + 1 == x
        ) or (
            self.board_coordinate[1] - 1 == y
            or self.board_coordinate[1] + 1 == y
        )

    def allowed_take(self, x: int, y: int):
        self.allowed_move(x, y)

    @property
    def name(self):
        return f"{self.piece_color}"

    def __repr__(self) -> str:
        return f"Piece(name={self.name}, board_coordinate={self.board_coordinate}, is_player_piece={self.is_player_piece})"


class Pawn(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )
        self.first_move = True
        self.en_passant = False

    def move(
        self,
        board_coordinate: tuple[int, int],
    ):
        self.first_move = False
        super().move(board_coordinate)

    def allowed_move(self, x: int, y: int):
        return (self.board_coordinate[0] == x) and (
            (
                self.is_player_piece
                and (
                    self.board_coordinate[1] - 1 == y
                    or (self.first_move and self.board_coordinate[1] - 2 == y)
                )
            )
            or (
                (not self.is_player_piece)
                and (
                    self.board_coordinate[1] + 1 == y
                    or (self.first_move and self.board_coordinate[1] + 2 == y)
                )
            )
        )

    def allowed_take(self, x: int, y: int):
        return (
            self.board_coordinate[0] + 1 == x
            or self.board_coordinate[0] - 1 == x
        ) and (
            (self.is_player_piece and self.board_coordinate[1] - 1 == y)
            or (
                (not self.is_player_piece)
                and self.board_coordinate[1] + 1 == y
            )
        )

    def promote(self):
        if self.board_coordinate[1] != 0:
            return
        promote_window = messagebox(
            "promote window", "", buttons=("H", "B", "R", "Q")
        )
        # self.kill()
        match promote_window:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

    def __repr__(self):
        return f"Piece(name={self.name}, board_coordinate={self.board_coordinate}, is_player_piece={self.is_player_piece}, first_move={self.first_move}, en_passant={self.en_passant})"

    @property
    def name(self):
        return f"{self.piece_color}p"

    @name.setter
    def name(self, val: str):
        self.name = val


class Knight(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )

    def allowed_move(self, x: int, y: int):
        if (
            self.board_coordinate[1] - 2 == y
            or self.board_coordinate[1] + 2 == y
        ):
            if (
                self.board_coordinate[0] - 1 == x
                or self.board_coordinate[0] + 1 == x
            ):
                return True
        if (
            self.board_coordinate[0] - 2 == x
            or self.board_coordinate[0] + 2 == x
        ):
            if (
                self.board_coordinate[1] - 1 == y
                or self.board_coordinate[1] + 1 == y
            ):
                return True
        return False

    @property
    def name(self):
        return f"{self.piece_color}h"


class Bishop(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )

    def allowed_move(self, x: int, y: int):
        pass

    @property
    def name(self):
        return f"{self.piece_color}b"


class Rook(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )
        self.first_move = True

    def move(self, board_coordinate: tuple[int, int]):
        self.first_move = False
        super().move(board_coordinate)

    def allowed_move(self, x: int, y: int):
        return (
            x != self.board_coordinate[0] and y == self.board_coordinate[1]
        ) or (x == self.board_coordinate[0] and y != self.board_coordinate[1])

    @property
    def name(self):
        return f"{self.piece_color}r"


class Queen(Rook, Bishop):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )
        print(super())

    def allowed_move(self, x: int, y: int):
        return super(Rook, self).allowed_move(x, y) or super(
            Bishop, self
        ).allowed_move(x, y)

    @property
    def name(self):
        return f"{self.piece_color}q"


class King(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
        is_player_piece: bool,
    ) -> None:
        super().__init__(
            piece_color, img_path, board_coordinate, pos, is_player_piece
        )
        self.first_move = True

    def move(self, board_coordinate: tuple[int, int]):
        self.first_move = False
        super().move(board_coordinate)

    def allowed_move(self, x: int, y: int):
        return super().allowed_move(x, y) or (
            self.first_move
            and (
                x + 2 == self.board_coordinate[0]
                or x - 2 == self.board_coordinate[0]
            )
        )

    @property
    def name(self):
        return f"{self.piece_color}k"
