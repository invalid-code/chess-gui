from typing import TypedDict

import pygame as pg

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


class ChessBoard(pg.sprite.Group):
    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()
        self.screen = screen
        self.board = Board()
        self.black_pawns = BlackPawns()
        self.white_pawns = WhitePawns()
        self.moving_piece = MovingPiece()
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
                    self.is_moving = not self.is_moving
                if black_pawn.rect.collidepoint(pos):
                    self.moving_piece.add(black_pawn)
                    self.is_moving = not self.is_moving

    def get_move_pos(self, pos: tuple[int, int]):
        if self.is_moving is True:
            for row in self.board.sprites():
                for col in row:
                    if col.rect.collidepoint(pos):
                        return col
        return False

    def set_is_taking(self, move):
        if self.is_moving is True:
            if move is not False:
                if (
                    self.board_repr[move.board_coordinate[1]][
                        move.board_coordinate[0]
                    ]
                    is not None
                ):
                    self.is_taking = True
                else:
                    self.is_taking = False

    def ui_move(self, move, taken_piece=None):
        piece = self.moving_piece.sprites()[0]
        if taken_piece:
            pass
        piece.rect.left, piece.rect.top = move.board_coordinate

    def back_move(self, pos: tuple[int, int], taken_piece=None):
        if taken_piece:
            self.board_repr[pos[1]][pos[0]] = None
        self.board_repr[pos[1]][pos[0]] = self.moving_piece.sprites()[0].name
