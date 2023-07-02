from typing import Optional

import pygame as pg

from .board import Board
from .pieces import Pieces
from .players import Opponent, Player
from .types import Piece


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.player = Player()
        self.opponent = Opponent(self.player)
        print(f"player pieces: {self.player.pieces}")
        print(f"opponent pieces: {self.opponent.pieces}")
        self.turn = "white"
        print(f"game turn: {self.turn}")
        self.pieces = Pieces(self.player_piece)
        self.board = Board()
        self.selected_piece: Optional[Piece] = None
        self.taken_pieces: list[Piece] = []
        self.is_moving = False
        self.pieces.start_board_repr(self.board_repr)
        print(f"starting board representation: {self.board_repr}")

    @property
    def board_repr(self):
        return self.board.board_repr

    @property
    def player_piece(self):
        return self.player.pieces

    def get_clicked_piece(self, pos: tuple[int, int]):
        return self.pieces.get_clicked_piece(pos)

    def get_clicked_square(self, pos: tuple[int, int]):
        return self.board.get_clicked_square(pos)

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        if self.selected_piece:
            if not self.selected_piece.is_player_piece(
                self.selected_piece.name, self.player_piece
            ):
                self.reset()
                return
            selected_square = self.get_clicked_square(pos)
            if not selected_square:
                return
            x, y = selected_square.board_coordinate
            if self.board.has_piece(x, y):
                taken_piece = self.get_clicked_piece(pos)
                if not taken_piece:
                    return
                if taken_piece.is_player_piece(
                    taken_piece.name, self.selected_piece.name
                ):
                    return
                if not self.selected_piece.allowed_take(x, y):
                    return
                self.add_to_taken_pieces(taken_piece)
                print(
                    f"{self.selected_piece.name} has taken {taken_piece.name}({taken_piece.board_coordinate})"
                )
            else:
                if not self.selected_piece.allowed_move(x, y):
                    return
                print(
                    f"{self.selected_piece.name} has moved to {selected_square.board_coordinate}"
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
        print(f"board representation: {self.board_repr}")

    def reset(self):
        self.selected_piece = None

    def draw(self):
        self.board.draw(self.screen)
        self.draw_pieces()

    def draw_pieces(self):
        self.pieces.pawns.draw(self.screen)

    # def change_turn(self):
    #     match self.turn:
    #         case 0:
    #             self.turn = Turn.BLACK
    #         case 1:
    #             self.turn = Turn.WHITE

    # def is_player_piece(self):
    #     moving_piece = self.selected_piece.sprites()
    #     if moving_piece[0].name[0] == self.player.pieces[0]:
    #         return True
    #     return False

    # def is_taking_own_pieces(self, move) -> bool | None:
    #     x, y = move.board_coordinate
    #     move_pos = self.board_repr[y][x]
    #     if move_pos:
    #         return move_pos[0] != self.selected_piece.sprites()[0].name[0]
    #     return True

    # def update(self):
    #     # self.ui_move(move.board_coordinate)
    #     # self.back_move(move.board_coordinate)
    #     # self.board.
    #     pass
