from piece.bishop import BlackBishops, WhiteBishops
from piece.king import BlackKings, WhiteKings
from piece.knight import BlackKnights, WhiteKnights
from piece.pawn import BlackPawns, WhitePawns
from piece.queen import BlackQueens, WhiteQueens
from piece.rook import BlackRooks, WhiteRooks


class Pieces:
    def __init__(self, pieces: str) -> None:
        self.white_pawns = WhitePawns(pieces)
        self.white_knights = WhiteKnights(pieces)
        self.white_bishops = WhiteBishops(pieces)
        self.white_rooks = WhiteRooks(pieces)
        self.white_queens = WhiteQueens(pieces)
        self.white_kings = WhiteKings(pieces)
        self.black_pawns = BlackPawns(pieces)
        self.black_knights = BlackKnights(pieces)
        self.black_bishops = BlackBishops(pieces)
        self.black_rooks = BlackRooks(pieces)
        self.black_queens = BlackQueens(pieces)
        self.black_kings = BlackKings(pieces)

    def get_clicked_piece(
        self,
        pos: tuple[int, int],
    ):
        white_pawn = self.white_pawns.is_clicked(pos)
        white_knight = self.white_knights.is_clicked(pos)
        white_bishop = self.white_bishops.is_clicked(pos)
        white_rook = self.white_rooks.is_clicked(pos)
        white_queen = self.white_queens.is_clicked(pos)
        white_king = self.white_kings.is_clicked(pos)
        black_pawn = self.black_pawns.is_clicked(pos)
        black_knight = self.black_knights.is_clicked(pos)
        black_bishop = self.black_bishops.is_clicked(pos)
        black_rook = self.black_rooks.is_clicked(pos)
        black_queen = self.black_queens.is_clicked(pos)
        black_king = self.black_kings.is_clicked(pos)
        if white_pawn:
            return white_pawn
        if white_knight:
            return white_knight
        if white_bishop:
            return white_bishop
        if white_rook:
            return white_rook
        if white_queen:
            return white_queen
        if white_king:
            return white_king
        if black_pawn:
            return black_pawn
        if black_knight:
            return black_knight
        if black_bishop:
            return black_bishop
        if black_rook:
            return black_rook
        if black_queen:
            return black_queen
        if black_king:
            return black_king
        return None

    def start_board_repr(self, board: list[list[str]]):
        self.white_pawns.start_board_repr(board)
        self.white_knights.start_board_repr(board)
        self.white_bishops.start_board_repr(board)
        self.white_rooks.start_board_repr(board)
        self.white_queens.start_board_repr(board)
        self.white_kings.start_board_repr(board)
        self.black_pawns.start_board_repr(board)
        self.black_knights.start_board_repr(board)
        self.black_bishops.start_board_repr(board)
        self.black_rooks.start_board_repr(board)
        self.black_queens.start_board_repr(board)
        self.black_kings.start_board_repr(board)
