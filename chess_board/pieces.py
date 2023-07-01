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
