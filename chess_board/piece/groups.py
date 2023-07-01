from chess_board.base import BaseGroup


class PieceGroup(BaseGroup):
    def sprites(self) -> list[PieceType]:
        return super().sprites()

    def start_board_repr(self, board: list[list[str]]):
        for piece in self.sprites():
            piece.set_board_repr(board, piece.name)

    def is_clicked(self, pos: tuple[int, int]) -> Optional[PieceType]:
        for piece in self.sprites():
            if piece.rect.collidepoint(pos):
                return piece
        return None
