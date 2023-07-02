from chess_board.base import BaseSprite


class Piece(BaseSprite):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        board_coordinate: tuple[int, int] = (0, 0),
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)
        self.piece_color = piece_color

    def set_board_repr(
        self,
        board: list[list[str]],
        name: str,
    ):
        x, y = self.board_coordinate
        board[y][x] = name

    def move(
        self,
        dest: tuple[int, int],
        board_coordinate: tuple[int, int],
    ):
        self.rect.topleft = dest
        self.board_coordinate = board_coordinate

    @staticmethod
    def is_player_piece(name: str, other: str) -> bool:
        if other[0] == name[0]:
            return True
        return False

    def __repr__(self) -> str:
        return f"Piece(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}"


class Pawn(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)
        self.first_move = True

    def __repr__(self) -> str:
        return f"Pawn(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, first_move={self.first_move})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\n\nfirst move is {self.first_move}"

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

    @property
    def name(self) -> str:
        return f"{self.piece_color}p"


class Knight(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Knight(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

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

    def allowed_take(self, x: int, y: int):
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
    def name(self) -> str:
        return f"{self.piece_color}k"


class Bishop(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Bishop(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

    def allowed_move(self, x: int, y: int):
        if x < self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        if x < self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        return False

    def allowed_take(self, x: int, y: int):
        for i in range(8):
            if (
                self.board_coordinate[1] + i == y
                and self.board_coordinate[0] + i == x
            ):
                return True
            if (
                self.board_coordinate[1] + i == y
                and self.board_coordinate[0] - i == x
            ):
                return True
            if (
                self.board_coordinate[1] - i == y
                and self.board_coordinate[0] - i == x
            ):
                return True
            if (
                self.board_coordinate[1] - i == y
                and self.board_coordinate[0] + i == x
            ):
                return True
        return False

    @property
    def name(self) -> str:
        return f"{self.piece_color}b"


class Rook(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Rook(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

    def allowed_move(self, x: int, y: int):
        if x == self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x == self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x < self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        return False

    def allowed_take(self, x: int, y: int):
        for i in range(8):
            if self.board_coordinate[1] + i == y:
                return True
            if self.board_coordinate[1] - i == y:
                return True
            if self.board_coordinate[0] + i == x:
                return True
            if self.board_coordinate[0] - i == x:
                return True
        return False

    @property
    def name(self) -> str:
        return f"{self.piece_color}r"


class Queen(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Queen(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

    def allowed_move(self, x: int, y: int):
        # bishop move rules
        if x < self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        if x < self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        # rook move rules
        if x == self.board_coordinate[0] and y < self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] - i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x == self.board_coordinate[0] and y > self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0]
                ]:
                    return False
                if (
                    self.board_coordinate[1] + i == y
                    and self.board_coordinate[0] == x
                ):
                    return True

        if x < self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] - i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] - i == x
                ):
                    return True

        if x > self.board_coordinate[0] and y == self.board_coordinate[1]:
            for i in range(1, 8):
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] + i
                ]:
                    return False

                if (
                    self.board_coordinate[1] == y
                    and self.board_coordinate[0] + i == x
                ):
                    return True

        return False

    def allowed_take(self, x: int, y: int):
        for i in range(8):
            if self.board_coordinate[1] + i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
            if self.board_coordinate[1] - i == y:
                if self.board_coordinate[0] - i == x:
                    return True
                if self.board_coordinate[0] + i == x:
                    return True
                return True
        return False

    @property
    def name(self) -> str:
        return f"{self.piece_color}q"


class King(Piece):
    def __init__(
        self,
        piece_color: str,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(piece_color, img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"King(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate})"

    def allowed_move(self, x: int, y: int):
        if (
            self.board_coordinate[0] - 1 == x
            or self.board_coordinate[0] + 1 == x
        ):
            if (
                self.board_coordinate[1] - 1 == y
                or self.board_coordinate[1] + 1 == y
            ):
                return True
            return True
        if (
            self.board_coordinate[1] - 1 == y
            or self.board_coordinate[1] + 1 == y
        ):
            if (
                self.board_coordinate[0] - 1 == x
                or self.board_coordinate[0] + 1 == x
            ):
                return True
            return True

        return False

    def allowed_take(self, x: int, y: int):
        if (
            self.board_coordinate[0] - 1 == x
            or self.board_coordinate[0] + 1 == x
        ):
            if (
                self.board_coordinate[1] - 1 == y
                or self.board_coordinate[1] + 1 == y
            ):
                return True
            return True
        if (
            self.board_coordinate[1] - 1 == y
            or self.board_coordinate[1] + 1 == y
        ):
            if (
                self.board_coordinate[0] - 1 == x
                or self.board_coordinate[0] + 1 == x
            ):
                return True
            return True
        return False

    @property
    def name(self) -> str:
        return f"{self.piece_color}k"
