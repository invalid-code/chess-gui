from typing import Any, TypedDict

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece.bishop.black_bishop import BlackBishop
from piece.bishop.white_bishop import WhiteBishop
from piece.king.black_king import BlackKing
from piece.king.white_king import WhiteKing
from piece.knight.black_knight import BlackKnight
from piece.knight.white_knight import WhiteKnight
from piece.pawn.black_pawn import BlackPawn
from piece.pawn.white_pawn import WhitePawn
from piece.queen.black_queen import BlackQueen
from piece.queen.white_queen import WhiteQueen
from piece.rook.black_rook import BlackRook
from piece.rook.white_rook import WhiteRook

from .bishops import BlackBishops, WhiteBishops
from .board import Board
from .kings import BlackKings, WhiteKings
from .knights import BlackKnights, WhiteKnights
from .pawns import BlackPawns, WhitePawns
from .queens import BlackQueens, WhiteQueens
from .rooks import BlackRooks, WhiteRooks


class Move(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: None


class Take(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: WhitePawn | BlackPawn


class MovingPiece(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

    def add_to_moving(self, piece):
        self.add(piece)

    def rem_moving(self):
        self.remove(self.sprites()[0])


class TakenPiece(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

    def add_to_taken(self, piece):
        self.add(piece)

    def rem_moving(self):
        self.remove(self.sprites()[-1])

    def hide(self):
        for sprite in self.sprites():
            sprite.kill()


class ChessBoard(pg.sprite.Group):
    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()
        self.screen = screen
        self.board = Board()
        self.black_pawns = BlackPawns()
        self.white_pawns = WhitePawns()
        self.black_knights = BlackKnights()
        self.white_knights = WhiteKnights()
        self.black_bishops = BlackBishops()
        self.white_bishops = WhiteBishops()
        self.black_rooks = BlackRooks()
        self.white_rooks = WhiteRooks()
        self.black_queens = BlackQueens()
        self.white_queens = WhiteQueens()
        self.black_kings = BlackKings()
        self.white_kings = WhiteKings()
        self.moving_piece = MovingPiece()
        self.taken_piece = TakenPiece()
        self.is_moving = False
        self.is_taking = False
        self.board_repr: list[list[str | None]] = []
        for rowi in range(8):
            row = []
            for coli in range(8):
                if rowi == 0:
                    if coli in (0, 7):
                        row.append(BlackRook.name)
                    if coli in (1, 6):
                        row.append(BlackKnight.name)
                    if coli in (2, 5):
                        row.append(BlackBishop.name)
                    if coli == 3:
                        row.append(BlackKing.name)
                    if coli == 4:
                        row.append(BlackQueen.name)
                elif rowi == 7:
                    if coli in (0, 7):
                        row.append(WhiteRook.name)
                    if coli in (1, 6):
                        row.append(WhiteKnight.name)
                    if coli in (2, 5):
                        row.append(WhiteBishop.name)
                    if coli == 3:
                        row.append(WhiteKing.name)
                    if coli == 4:
                        row.append(WhiteQueen.name)
                elif rowi == 1:
                    row.append(BlackPawn.name)
                elif rowi == 6:
                    row.append(WhitePawn.name)
                else:
                    row.append(None)
            self.board_repr.append(row)

    def draw(self):
        self.board.draw(self.screen)

    def draw_pieces(self):
        self.black_pawns.draw(self.screen)
        self.white_pawns.draw(self.screen)
        self.black_knights.draw(self.screen)
        self.white_knights.draw(self.screen)
        self.black_bishops.draw(self.screen)
        self.white_bishops.draw(self.screen)
        self.black_rooks.draw(self.screen)
        self.white_rooks.draw(self.screen)
        self.black_queens.draw(self.screen)
        self.white_queens.draw(self.screen)
        self.black_kings.draw(self.screen)
        self.white_kings.draw(self.screen)

    def get_clicked_piece(self, pos: tuple[int, int]):
        for white_pawn in self.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                self.moving_piece.add(white_pawn)
                self.is_moving = True

        for black_pawn in self.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                self.moving_piece.add(black_pawn)
                self.is_moving = True

        for white_knight in self.white_knights:
            if white_knight.rect.collidepoint(pos):
                self.moving_piece.add(white_knight)
                self.is_moving = True

        for black_knight in self.black_knights:
            if black_knight.rect.collidepoint(pos):
                self.moving_piece.add(black_knight)
                self.is_moving = True

        for white_bishop in self.white_bishops:
            if white_bishop.rect.collidepoint(pos):
                self.moving_piece.add(white_bishop)
                self.is_moving = True

        for black_bishop in self.black_bishops:
            if black_bishop.rect.collidepoint(pos):
                self.moving_piece.add(black_bishop)
                self.is_moving = True

        for white_rook in self.white_rooks:
            if white_rook.rect.collidepoint(pos):
                self.moving_piece.add(white_rook)
                self.is_moving = True

        for black_rook in self.black_rooks:
            if black_rook.rect.collidepoint(pos):
                self.moving_piece.add(black_rook)
                self.is_moving = True

        for white_queen in self.white_queens:
            if white_queen.rect.collidepoint(pos):
                self.moving_piece.add(white_queen)
                self.is_moving = True

        for black_queen in self.black_queens:
            if black_queen.rect.collidepoint(pos):
                self.moving_piece.add(black_queen)
                self.is_moving = True

        for white_king in self.white_kings:
            if white_king.rect.collidepoint(pos):
                self.moving_piece.add(white_king)
                self.is_moving = True

        for black_king in self.black_kings:
            if black_king.rect.collidepoint(pos):
                self.moving_piece.add(black_king)
                self.is_moving = True

    def get_move_pos(self, pos: tuple[int, int]):
        for row in self.board.sprites():
            if row.rect.collidepoint(pos):
                return row

    def set_is_taking(self, move):
        x, y = move.board_coordinate[0], move.board_coordinate[1]
        if self.board_repr[y][x]:
            self.is_taking = True
            self.is_moving = False
            self.taken_piece.add(self.get_taken_piece(pg.mouse.get_pos()))
        else:
            self.is_taking = False

    def get_taken_piece(self, pos: tuple[int, int]):
        for white_pawn in self.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                return white_pawn

        for black_pawn in self.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                return black_pawn

        for white_knight in self.white_knights:
            if white_knight.rect.collidepoint(pos):
                return white_knight

        for black_knight in self.black_knights:
            if black_knight.rect.collidepoint(pos):
                return black_knight

        for white_bishop in self.white_bishops:
            if white_bishop.rect.collidepoint(pos):
                return white_bishop

        for black_bishop in self.black_bishops:
            if black_bishop.rect.collidepoint(pos):
                return black_bishop

        for white_rook in self.white_rooks:
            if white_rook.rect.collidepoint(pos):
                return white_rook

        for black_rook in self.black_rooks:
            if black_rook.rect.collidepoint(pos):
                return black_rook

        for white_queen in self.white_queens:
            if white_queen.rect.collidepoint(pos):
                return white_queen

        for black_queen in self.black_queens:
            if black_queen.rect.collidepoint(pos):
                return black_queen

        for white_king in self.white_kings:
            if white_king.rect.collidepoint(pos):
                return white_king

        for black_king in self.black_kings:
            if black_king.rect.collidepoint(pos):
                return black_king
                
    def ui_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        if self.taken_piece:
            self.taken_piece.hide()
        piece.rect.left, piece.rect.top = (
            pos[0] * IMAGE_SIZE,
            pos[1] * IMAGE_SIZE,
        )
        self.is_moving = False

    def back_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        self.set_board_repr(
            (piece.board_coordinate[0], piece.board_coordinate[1], None),
            (pos[0], pos[1], piece.name),
        )
        piece.board_coordinate = pos
        if piece.name in ("bp, wp"):
            if self.moving_piece.sprites()[0].first_move:
                self.moving_piece.sprites()[0].first_move = False
        self.moving_piece.rem_moving()

    def set_board_repr(self, *args: tuple[int, int, Any]):
        for piece in args:
            self.board_repr[piece[1]][piece[0]] = piece[2]

    def is_piece_allowed_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        x, y = pos
        if self.is_moving:
            return piece.allowed_move(x, y)
        if self.is_taking:
            return piece.allowed_take(x, y)

    def not_allowed_move(self):
        if self.moving_piece:
            self.moving_piece.rem_moving()
            self.is_moving = False
        if self.is_taking:
            self.taken_piece.rem_moving()
            self.is_taking = False
