from chess_board.base import BaseSprite


class Piece(BaseSprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int] = (0, 0),
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def set_board_repr(self, board: list[list[str]], name: str):
        x, y = self.board_coordinate
        board[y][x] = name

    def move(self, dest: tuple[int, int]):
        self.rect.topleft = dest

    def __repr__(self) -> str:
        return f"Piece(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"


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


class Knight(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Knight(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

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


class Bishop(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Bishop(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

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


class Rook(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Rook(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

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


class Queen(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Queen(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

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


class King(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"King(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

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
