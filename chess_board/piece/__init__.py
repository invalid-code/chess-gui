from chess_board.base import BaseSprite


class Piece(BaseSprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int],
        pos: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Piece(board_coordinate={self.board_coordinate})"

    def __str__(self) -> str:
        return f"board coordinate is{self.board_coordinate}"


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
        return f"Pawn(board_coordinate={self.board_coordinate}, first_move={self.first_move})"

    def __str__(self) -> str:
        return f"board coordinate is{self.board_coordinate}\nfirst move is {self.first_move}"

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
        return f"Knight(board_coordinate={self.board_coordinate})"

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


class Rook(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Rook(board_coordinate={self.board_coordinate})"

    def allowed_move(self, x: int, y: int):
        if x != self.board_coordinate[0]:
            return False
        if y != self.board_coordinate[1]:
            return False
        return True

    def allowed_take(self, x: int, y: int):
        if x != self.board_coordinate[0]:
            return False
        if y != self.board_coordinate[1]:
            return False
        return True


class Queen(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Queen(board_coordinate={self.board_coordinate})"

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
        if x != self.board_coordinate[0]:
            return False
        if y != self.board_coordinate[1]:
            return False
        return True

    def allowed_take(self, x: int, y: int):
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
        if x != self.board_coordinate[0]:
            return False
        if y != self.board_coordinate[1]:
            return False
        return True


class King(Piece):
    def __init__(
        self,
        img_path: str,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)

    def __repr__(self) -> str:
        return f"King(board_coordinate={self.board_coordinate})"

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
