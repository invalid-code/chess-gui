from piece import Piece


class Pawn(Piece):
    def __init__(
        self,
        pos: tuple[int, int],
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__(board_coordinate, pos)
        self.first_move = True

    def __repr__(self) -> str:
        return f"Pawn(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive}, first_move={self.first_move})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}\nfirst move is {self.first_move}"
