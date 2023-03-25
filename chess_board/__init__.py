from typing import Any, TypedDict

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece.pawn.black_pawn import BlackPawn
from piece.pawn.white_pawn import WhitePawn

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
            for _ in range(8):
                if rowi == 1:
                    row.append(BlackPawn.name)
                elif rowi == 6:
                    row.append(WhitePawn.name)
                else:
                    row.append(None)
            self.board_repr.append(row)

    def draw(self):
        self.board.draw(self.screen)

    def draw_black_pawns(self):
        self.black_pawns.draw(self.screen)

    def draw_white_pawns(self):
        self.white_pawns.draw(self.screen)

    def draw_black_knights(self):
        self.black_knights.draw(self.screen)

    def draw_white_knights(self):
        self.white_knights.draw(self.screen)

    def draw_black_bishops(self):
        self.black_bishops.draw(self.screen)

    def draw_white_bishops(self):
        self.white_bishops.draw(self.screen)

    def draw_black_rooks(self):
        self.black_rooks.draw(self.screen)

    def draw_white_rooks(self):
        self.white_rooks.draw(self.screen)

    def draw_black_queens(self):
        self.black_queens.draw(self.screen)

    def draw_white_queens(self):
        self.white_queens.draw(self.screen)

    def draw_black_kings(self):
        self.black_kings.draw(self.screen)

    def draw_white_kings(self):
        self.white_kings.draw(self.screen)

    def get_clicked_piece(self, pos: tuple[int, int]):
        for (
            white_pawn,
            black_pawn,
        ) in zip(
            self.white_pawns.sprites(),
            self.black_pawns.sprites(),
        ):
            if white_pawn.rect.collidepoint(pos):
                self.moving_piece.add(white_pawn)
                self.is_moving = True
            if black_pawn.rect.collidepoint(pos):
                self.moving_piece.add(black_pawn)
                self.is_moving = True

        for (
            white_knight,
            black_knight,
            white_bishop,
            black_bishop,
            white_rook,
            black_rook,
        ) in zip(
            self.white_knights.sprites(),
            self.black_knights.sprites(),
            self.white_bishops.sprites(),
            self.black_bishops.sprites(),
            self.white_rooks.sprites(),
            self.black_rooks.sprites(),
        ):
            if white_knight.rect.collidepoint(pos):
                self.moving_piece.add(white_knight)
                self.is_moving = True
            if black_knight.rect.collidepoint(pos):
                self.moving_piece.add(black_knight)
                self.is_moving = True
            if white_bishop.rect.collidepoint(pos):
                self.moving_piece.add(white_bishop)
                self.is_moving = True
            if black_bishop.rect.collidepoint(pos):
                self.moving_piece.add(black_bishop)
                self.is_moving = True
            if white_rook.rect.collidepoint(pos):
                self.moving_piece.add(white_rook)
                self.is_moving = True
            if black_rook.rect.collidepoint(pos):
                self.moving_piece.add(black_rook)
                self.is_moving = True

        for white_queen, black_queen, white_king, black_king in zip(
            self.white_queens.sprites(),
            self.black_queens.sprites(),
            self.white_kings.sprites(),
            self.black_kings.sprites(),
        ):
            if white_queen.rect.collidepoint(pos):
                self.moving_piece.add(white_queen)
                self.is_moving = True
            if black_queen.rect.collidepoint(pos):
                self.moving_piece.add(black_queen)
                self.is_moving = True
            if white_king.rect.collidepoint(pos):
                self.moving_piece.add(white_king)
                self.is_moving = True
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
        for black_pawn in self.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                return black_pawn

        for white_pawn in self.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                return white_pawn

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
        if self.is_moving:
            return piece.allowed_move(pos[0], pos[1])
        if self.is_taking:
            return piece.allowed_take(pos[0], pos[1])

    def not_allowed_move(self):
        if self.moving_piece:
            self.moving_piece.rem_moving()
            self.is_moving = False
        if self.is_taking:
            self.taken_piece.rem_moving()
            self.is_taking = False
