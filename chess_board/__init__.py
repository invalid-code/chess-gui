from typing import Optional

import pygame as pg

from chess_board.piece import King

from .board import Board
from .pieces import Pieces
from .players import Opponent, Player
from .types import Check, Piece


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.player = Player()
        self.opponent = Opponent(self.player)
        print(f"player pieces: {self.player_pieces}")
        print(f"opponent pieces: {self.opponent.pieces}")
        self.pieces = Pieces(self.player_pieces)
        self.board = Board()
        self.selected_piece: Optional[Piece] = None
        self.taken_pieces: list[Piece] = []
        self.is_check: Check = {"is_check": False, "pieces": None}
        self.pieces.start_board_repr(self.board_repr)
        print(f"starting board representation: {self.board_repr}")

    @property
    def board_repr(self):
        return self.board.board_repr

    @property
    def player_pieces(self):
        return self.player.pieces

    def get_clicked_piece(self, pos: tuple[int, int]):
        return self.pieces.get_clicked_piece(pos)

    def get_clicked_square(self, pos: tuple[int, int]):
        return self.board.get_clicked_square(pos)

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        if self.selected_piece:
            selected_square = self.get_clicked_square(pos)
            if not selected_square:
                return
            if self.pieces.is_check():
                self.reset()
                return
            if self.board.has_piece(*selected_square.board_coordinate):
                taken_piece = self.get_clicked_piece(pos)
                if not taken_piece:
                    return
                if isinstance(taken_piece, King):
                    self.reset()
                    return
                if taken_piece.is_same_piece(taken_piece.is_player_piece):
                    self.reset()
                    return
                if not self.selected_piece.allowed_take(
                    *selected_square.board_coordinate
                ):
                    self.reset()
                    return
                self.add_to_taken_pieces(taken_piece)
                print(f"{repr(self.selected_piece)} has taken {taken_piece}")
            else:
                if not self.selected_piece.allowed_move(
                    *selected_square.board_coordinate
                ):
                    self.reset()
                    return
                print(
                    f"{repr(self.selected_piece)} has moved to {selected_square.board_coordinate}"
                )
            self.update(
                self.selected_piece,
                selected_square.rect.topleft,
                selected_square.board_coordinate,
            )
            self.reset()
        else:
            self.selected_piece = self.get_clicked_piece(pos)
            print(f"selected piece: {repr(self.selected_piece)}")

    def add_to_taken_pieces(self, piece: Piece):
        piece.kill()
        self.taken_pieces.append(piece)

    def update(
        self,
        piece: Piece,
        dest: tuple[int, int],
        board_coordinate: tuple[int, int],
    ):
        self.board.update_board_repr(
            piece.board_coordinate, board_coordinate, piece.name
        )  # update board representation
        piece.move(
            dest, board_coordinate
        )  # update piece ui and board coordinate
        self.is_check = {
            "is_check": self.pieces.is_check(),
            "pieces": "b" if piece.name[0] == "w" else "w",
        }
        if self.is_check["is_check"]:
            print(
                f"{'white' if self.is_check['pieces'] == 'w' else 'black'} is check"
            )
        print(f"board representation: {self.board_repr}")

    def reset(self):
        self.selected_piece = None

    def draw(self):
        self.board.draw(self.screen)
        self.draw_pieces()

    def draw_pieces(self):
        self.pieces.pawns.draw(self.screen)
        self.pieces.kings.draw(self.screen)
