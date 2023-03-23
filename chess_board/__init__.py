from typing import Any, TypedDict

import pygame as pg

from chess_board.constants import IMAGE_SIZE
from piece.pawn.black_pawn import BlackPawn
from piece.pawn.white_pawn import WhitePawn

from .board import Board
from .pawns import BlackPawns, WhitePawns


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

    def add_to_moving(self, piece: BlackPawn | WhitePawn):
        self.add(piece)

    def rem_moving(self):
        self.remove(self.sprites()[0])


class TakenPiece(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

    def add_to_taken(self, piece: BlackPawn | WhitePawn):
        self.add(piece)

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

    def get_clicked_piece(self, pos: tuple[int, int]):
        if self.is_moving is False:
            for white_pawn, black_pawn in zip(
                self.white_pawns.sprites(), self.black_pawns.sprites()
            ):
                if white_pawn.rect.collidepoint(pos):
                    self.moving_piece.add(white_pawn)
                    self.is_moving = True
                if black_pawn.rect.collidepoint(pos):
                    self.moving_piece.add(black_pawn)
                    self.is_moving = True

    def get_move_pos(self, pos: tuple[int, int]):
        for row in self.board.sprites():
            if row.rect.collidepoint(pos):
                return row

    def set_is_taking(self, move):
        x, y = move.board_coordinate[0], move.board_coordinate[1]
        if self.board_repr[y][x]:
            self.is_taking = True
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
        self.moving_piece.rem_moving()

    def set_board_repr(self, *args: tuple[int, int, Any]):
        for piece in args:
            self.board_repr[piece[1]][piece[0]] = piece[2]
