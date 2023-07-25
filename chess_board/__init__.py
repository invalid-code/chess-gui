from typing import Optional

import pygame as pg

from chess_board.pieces import Pieces

from .board import Board
from .players import Opponent, Player
from .types import Piece


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.player = Player()
        self.opponent = Opponent(self.player)
        self.pieces = Pieces(self.player.piece_color)
        self.board = Board()
        self.taken_pieces: list[Piece] = []
        self.selected_piece: Optional[Piece] = None
        self.is_check = False
        self.is_checkmate = False
        self.board.start_board_repr(self.pieces)

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        if self.is_check and self.is_checkmate:
            return
        if self.selected_piece:
            if (
                self.is_check
                and self.selected_piece.name
                != f"{self.opponent.piece_color[0]}k"
            ):
                print("can only move king when in check")  # temporary
                return self.reset()
            selected_square = self.board.get_clicked_square(pos)
            if not selected_square:
                return
            dest_board_coordinate = selected_square.board_coordinate
            if self.board.has_piece(dest_board_coordinate):
                taken_piece = self.get_clicked_piece(
                    selected_square.rect.center
                )
                if not taken_piece:
                    return
                if taken_piece.is_player_piece:
                    print("can't take own pieces")
                    return self.reset()
                if taken_piece.name[1] == "k":
                    print("can't take king")
                    return self.reset()
                if not self.selected_piece.allowed_take(
                    *taken_piece.board_coordinate
                ):
                    print("piece not allowed take")
                    return self.reset()
                self.taken_pieces.append(taken_piece)
                taken_piece.kill()
                print(
                    f"{repr(self.selected_piece)} has taken {repr(taken_piece)}"
                )
            else:
                if not self.selected_piece.allowed_move(
                    *dest_board_coordinate
                ):
                    print("piece not allowed move")
                    return self.reset()
                if self.selected_piece.name[1] == "k":
                    if (
                        self.selected_piece.board_coordinate[0] + 2
                        == dest_board_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[1]
                        if not rook.first_move:
                            print("rook cant castle")
                            return self.reset()
                        rook.move(
                            (
                                rook.board_coordinate[0] - 2,
                                rook.board_coordinate[1],
                            )
                        )
                    elif (
                        self.selected_piece.board_coordinate[0] - 2
                        == dest_board_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[0]
                        if not rook.first_move:
                            print("rook cant castle")
                            return self.reset()
                        rook.move(
                            (
                                rook.board_coordinate[0] + 3,
                                rook.board_coordinate[1],
                            )
                        )
                print(
                    f"{repr(self.selected_piece)} has moved to {dest_board_coordinate}"
                )
            self.board.update_board_repr(
                dest_board_coordinate,
                self.selected_piece,
            )
            self.selected_piece.move(
                dest_board_coordinate,
            )
            if self.selected_piece.name[1] == "p":
                self.selected_piece.promote()
            self.reset()
            self.is_check = self.pieces.is_check()
            if self.is_check:
                self.is_checkmate = self.pieces.is_checkmate(self.board_repr)
                if self.is_checkmate:
                    print("opponent lost")
                    return
                print("opponent is check")
        else:
            self.selected_piece = self.get_clicked_piece(pos)
            print(f"selected piece: {self.selected_piece}")

    def draw(self):
        self.board.draw(self.screen)
        self.pieces.draw(self.screen)

    def reset(self):
        self.selected_piece = None
        print("piece has now been reseted")

    def get_clicked_piece(self, pos: tuple[int, int]):
        return self.pieces.get_clicked_piece(pos)

    @property
    def board_repr(self):
        return self.board.board_repr
