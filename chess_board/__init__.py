from typing import Optional

import pygame as pg

from chess_board.piece import King

from .board import Board
from .players import PlayerA, PlayerB
from .types import Piece


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.player = PlayerA()
        self.opponent = PlayerB(self.player)
        self.board = Board()
        self.taken_pieces: list[Piece] = []

    @property
    def board_repr(self):
        return self.board.board_repr

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]

    def draw(self):
        self.board.draw(self.screen)
        self.draw_pieces()

    def draw_pieces(self):
        pass
