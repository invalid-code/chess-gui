from .piece.groups import (BishopGroup, KingGroup, KnightGroup, PawnGroup,
                           QueenGroup, RookGroup)


class Pieces:
    def __init__(self, pieces: str) -> None:
        self.pawns = PawnGroup(pieces)
        # self.knights = KnightGroup(pieces)
        # self.bishops = BishopGroup(pieces)
        # self.rooks = RookGroup(pieces)
        # self.queens = QueenGroup(pieces)
        self.kings = KingGroup(pieces)

    def get_clicked_piece(
        self,
        pos: tuple[int, int],
    ):
        pawn = self.pawns.is_clicked(pos)
        king = self.kings.is_clicked(pos)
        if pawn:
            return pawn
        if king:
            return king
        return None

    def start_board_repr(self, board: list[list[str]]):
        for pawn in self.pawns.sprites():
            x, y = pawn.board_coordinate
            board[y][x] = pawn.name

        for king in self.kings.sprites():
            x, y = king.board_coordinate
            board[y][x] = king.name
