from .bishops import BlackBishops, WhiteBishops
from .kings import BlackKings, WhiteKings
from .knights import BlackKnights, WhiteKnights
from .pawns import BlackPawns, WhitePawns
from .queens import BlackQueens, WhiteQueens
from .rooks import BlackRooks, WhiteRooks


class Pieces:
    def __init__(self, pieces: str) -> None:
        # * white pieces
        self.white_pawns = WhitePawns(pieces)
        self.white_knights = WhiteKnights(pieces)
        self.white_bishops = WhiteBishops(pieces)
        self.white_rooks = WhiteRooks(pieces)
        self.white_queens = WhiteQueens(pieces)
        self.white_kings = WhiteKings(pieces)
        # * black pieces
        self.black_pawns = BlackPawns(pieces)
        self.black_knights = BlackKnights(pieces)
        self.black_bishops = BlackBishops(pieces)
        self.black_rooks = BlackRooks(pieces)
        self.black_queens = BlackQueens(pieces)
        self.black_kings = BlackKings(pieces)
