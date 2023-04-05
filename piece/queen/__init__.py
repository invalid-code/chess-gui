from piece import Piece


class Queen(Piece):
    def __init__(
        self,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(board_coordinate, pos)

    def __repr__(self) -> str:
        return f"Queen(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"

    def allowed_move(self, x: int, y: int, board: list[list[None | str]]):
        for i in range(1, 8):
            # bishop move rules
            if x < self.board_coordinate[0] and y < self.board_coordinate[1]:
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] - i
                ]:
                    return False

            if x > self.board_coordinate[0] and y > self.board_coordinate[1]:
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] + i
                ]:
                    return False

            if x < self.board_coordinate[0] and y > self.board_coordinate[1]:
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0] - i
                ]:
                    return False

            if x > self.board_coordinate[0] and y < self.board_coordinate[1]:
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0] + i
                ]:
                    return False

            if x == self.board_coordinate[0] and y < self.board_coordinate[1]:
                if board[self.board_coordinate[1] - i][
                    self.board_coordinate[0]
                ]:
                    return False

            if x == self.board_coordinate[0] and y > self.board_coordinate[1]:
                if board[self.board_coordinate[1] + i][
                    self.board_coordinate[0]
                ]:
                    return False

            if x < self.board_coordinate[0] and y == self.board_coordinate[1]:
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] - i
                ]:
                    return False

            if x > self.board_coordinate[0] and y == self.board_coordinate[1]:
                if board[self.board_coordinate[1]][
                    self.board_coordinate[0] + i
                ]:
                    return False

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

            if self.board_coordinate[1] + i == y:
                return True

            if self.board_coordinate[0] + i == x:
                return True

            if self.board_coordinate[1] - i == y:
                return True

            if self.board_coordinate[0] - i == x:
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
