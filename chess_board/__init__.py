# from enum import Enum
from typing import Any, TypedDict

import pygame as pg

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
from Players.opponent import Opponent
from Players.player import Player

from .board import Board
from .constants import IMAGE_SIZE
from .pieces import Pieces

# class PieceEnum(Enum):
#     BLACK_PAWN = BlackPawn
#     WHITE_PAWN = WhitePawn
#     BLACK_KNIGHT = BlackKnight
#     WHITE_KNIGHT = WhiteKnight
#     BLACK_BISHOP = BlackBishop
#     WHITE_BISHOP = WhiteBishop
#     BLACK_ROOK = BlackRook
#     WHITE_ROOK = WhiteRook
#     BLACK_QUEEN = BlackQueen
#     WHITE_QUEEN = WhiteQueen
#     BLACK_KING = BlackKing
#     WHITE_KING = WhiteKing


class Move(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: None | BlackPawn | WhitePawn | BlackKnight | WhiteKnight | BlackBishop | WhiteBishop | BlackRook | WhiteRook | BlackKing | WhiteKing | BlackQueen | WhiteQueen


class Take(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: BlackPawn | WhitePawn | BlackKnight | WhiteKnight | BlackBishop | WhiteBishop | BlackRook | WhiteRook | BlackKing | WhiteKing | BlackQueen | WhiteQueen


class MovingPiece(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

    def add_to_moving(self, piece):
        self.add(piece)

    def rem_moving(self):
        self.remove(self.sprites()[0])

    def sprites(
        self,
    ) -> list[
        BlackPawn
        | WhitePawn
        | BlackKnight
        | WhiteKnight
        | BlackBishop
        | WhiteBishop
        | BlackRook
        | WhiteRook
        | BlackKing
        | WhiteKing
        | BlackQueen
        | WhiteQueen
    ]:
        return super().sprites()


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
        self.turn = "w"
        self.player = Player()
        self.opponent = Opponent(self.player)
        self.pieces = Pieces("black" if self.player.pieces[0] == "b" else "w")
        self.board = Board()
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
        self.pieces.black_pawns.draw(self.screen)
        self.pieces.white_pawns.draw(self.screen)
        self.pieces.black_knights.draw(self.screen)
        self.pieces.white_knights.draw(self.screen)
        self.pieces.black_bishops.draw(self.screen)
        self.pieces.white_bishops.draw(self.screen)
        self.pieces.black_rooks.draw(self.screen)
        self.pieces.white_rooks.draw(self.screen)
        self.pieces.black_queens.draw(self.screen)
        self.pieces.white_queens.draw(self.screen)
        self.pieces.black_kings.draw(self.screen)
        self.pieces.white_kings.draw(self.screen)

    def get_clicked_piece(self, pos: tuple[int, int]):
        for white_pawn in self.pieces.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                self.moving_piece.add(white_pawn)
                self.is_moving = True

        for black_pawn in self.pieces.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                self.moving_piece.add(black_pawn)
                self.is_moving = True

        for white_knight in self.pieces.white_knights:
            if white_knight.rect.collidepoint(pos):
                self.moving_piece.add(white_knight)
                self.is_moving = True

        for black_knight in self.pieces.black_knights:
            if black_knight.rect.collidepoint(pos):
                self.moving_piece.add(black_knight)
                self.is_moving = True

        for white_bishop in self.pieces.white_bishops:
            if white_bishop.rect.collidepoint(pos):
                self.moving_piece.add(white_bishop)
                self.is_moving = True

        for black_bishop in self.pieces.black_bishops:
            if black_bishop.rect.collidepoint(pos):
                self.moving_piece.add(black_bishop)
                self.is_moving = True

        for white_rook in self.pieces.white_rooks:
            if white_rook.rect.collidepoint(pos):
                self.moving_piece.add(white_rook)
                self.is_moving = True

        for black_rook in self.pieces.black_rooks:
            if black_rook.rect.collidepoint(pos):
                self.moving_piece.add(black_rook)
                self.is_moving = True

        for white_queen in self.pieces.white_queens:
            if white_queen.rect.collidepoint(pos):
                self.moving_piece.add(white_queen)
                self.is_moving = True

        for black_queen in self.pieces.black_queens:
            if black_queen.rect.collidepoint(pos):
                self.moving_piece.add(black_queen)
                self.is_moving = True

        for white_king in self.pieces.white_kings:
            if white_king.rect.collidepoint(pos):
                self.moving_piece.add(white_king)
                self.is_moving = True

        for black_king in self.pieces.black_kings:
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
            self.is_moving = False
            self.is_taking = True
            self.taken_piece.add(self.get_taken_piece(pg.mouse.get_pos()))
        else:
            self.is_taking = False

    def get_taken_piece(
        self, pos: tuple[int, int]
    ) -> (
        None
        | WhitePawn
        | BlackPawn
        | WhiteKnight
        | BlackKnight
        | WhiteBishop
        | BlackBishop
        | WhiteRook
        | BlackRook
        | WhiteQueen
        | BlackQueen
        | WhiteKing
        | BlackKing
    ):
        for white_pawn in self.pieces.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                return white_pawn

        for black_pawn in self.pieces.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                return black_pawn

        for white_knight in self.pieces.white_knights:
            if white_knight.rect.collidepoint(pos):
                return white_knight

        for black_knight in self.pieces.black_knights:
            if black_knight.rect.collidepoint(pos):
                return black_knight

        for white_bishop in self.pieces.white_bishops:
            if white_bishop.rect.collidepoint(pos):
                return white_bishop

        for black_bishop in self.pieces.black_bishops:
            if black_bishop.rect.collidepoint(pos):
                return black_bishop

        for white_rook in self.pieces.white_rooks:
            if white_rook.rect.collidepoint(pos):
                return white_rook

        for black_rook in self.pieces.black_rooks:
            if black_rook.rect.collidepoint(pos):
                return black_rook

        for white_queen in self.pieces.white_queens:
            if white_queen.rect.collidepoint(pos):
                return white_queen

        for black_queen in self.pieces.black_queens:
            if black_queen.rect.collidepoint(pos):
                return black_queen

        for white_king in self.pieces.white_kings:
            if white_king.rect.collidepoint(pos):
                return white_king

        for black_king in self.pieces.black_kings:
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
        if isinstance(piece, WhitePawn | BlackPawn):
            if piece.first_move:
                piece.first_move = False
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

    def change_turn(self):
        if self.turn == "w":
            self.turn = "b"
            return
        self.turn = "w"

    def is_player_piece(self):
        moving_piece = self.moving_piece.sprites()
        if moving_piece:
            if moving_piece[0].name[0] != self.player.pieces[0]:
                self.not_allowed_move()

    def is_taking_own_pieces(self, move) -> bool | None:
        x, y = move.board_coordinate
        move_pos = self.board_repr[y][x]
        if move_pos:
            return move_pos[0] == self.moving_piece.sprites()[0].name[0]
