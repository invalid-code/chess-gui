from chess_board.base import BaseGroup
from chess_board.types import Piece


class PieceGroup(BaseGroup):
    def sprites(self) -> list[Piece]:
        return super().sprites()

    def start_board_repr(self, board: list[list[str]]):
        for piece in self.sprites():
            piece.set_board_repr(board, piece.name)

    def is_clicked(self, pos: tuple[int, int]) -> Optional[Piece]:
        for piece in self.sprites():
            if piece.rect.collidepoint(pos):
                return piece
        return None


class PawnGroup(PieceGroup):
    pass


class KnightGroup(PieceGroup):
    pass


class BishopGroup(PieceGroup):
    pass


class RookGroup(PieceGroup):
    pass


class QueenGroup(PieceGroup):
    pass


class KingGroup(PieceGroup):
    pass
