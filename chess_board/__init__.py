from typing import Optional

import pygame as pg
from .piece import King, Pawn

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
        if self.is_checkmate:
            return
        if self.selected_piece:
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
                    return self.reset()
                if isinstance(taken_piece, King):
                    return self.reset()
                if not self.selected_piece.allowed_take(
                    *taken_piece.board_coordinate
                ):
                    return self.reset()
                self.remove_piece(taken_piece)
            elif (
                self.selected_piece.name == f"{self.player.piece_color[0]}p"
                and self.selected_piece.allowed_take(*dest_board_coordinate)
            ):
                if (
                    self.board_repr[dest_board_coordinate[1] + 1][
                        dest_board_coordinate[0]
                    ]
                    != f"{self.opponent.piece_color[0]}p"
                ):
                    pass
                else:
                    for pawn in self.pieces.pawns.sprites():
                        if pawn.is_player_piece:
                            pass
                        elif not (
                            pawn.board_coordinate
                            == (
                                dest_board_coordinate[0],
                                dest_board_coordinate[1] + 1,
                            )
                        ):
                            pass
                        elif pawn.en_passant:
                            pass
                        else:
                            self.board_repr[pawn.board_coordinate[1]][
                                pawn.board_coordinate[0]
                            ] = ""
                            self.remove_piece(pawn)
                            break
            else:
                if not self.selected_piece.allowed_move(
                    *dest_board_coordinate
                ):
                    return self.reset()
                if isinstance(self.selected_piece, Pawn):
                    if not self.selected_piece.first_move:
                        pass
                    elif not (
                        self.board_repr[dest_board_coordinate[1]][
                            dest_board_coordinate[0] - 1
                        ]
                        == f"{self.player.piece_color[0]}p"
                    ):
                        pass
                    elif not (
                        self.board_repr[dest_board_coordinate[1]][
                            dest_board_coordinate[0] + 1
                        ]
                        == f"{self.player.piece_color[0]}p"
                    ):
                        pass
                    else:
                        self.selected_piece.en_passant = True
                if isinstance(self.selected_piece, King):
                    if (
                        self.selected_piece.board_coordinate[0] + 2
                        == dest_board_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[1]
                        if not rook.first_move:
                            return self.reset()
                        self.update(
                            rook,
                            (
                                rook.board_coordinate[0] - 2,
                                rook.board_coordinate[1],
                            ),
                        )
                    if (
                        self.selected_piece.board_coordinate[0] - 2
                        == dest_board_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[0]
                        if not rook.first_move:
                            return self.reset()
                        self.update(
                            rook,
                            (
                                rook.board_coordinate[0] + 3,
                                rook.board_coordinate[1],
                            ),
                        )
            self.update(self.selected_piece, dest_board_coordinate)
            if isinstance(self.selected_piece, Pawn):
                self.selected_piece.promote()
            self.reset()
            self.is_check = self.pieces.is_check()
            if self.is_check:
                self.is_checkmate = self.pieces.is_checkmate(self.board_repr)
        else:
            self.selected_piece = self.get_clicked_piece(pos)
        if self.is_checkmate:
            return

    def draw(self):
        self.board.draw(self.screen)
        self.pieces.draw(self.screen)

    def reset(self):
        self.selected_piece = None

    def get_clicked_piece(self, pos: tuple[int, int]):
        return self.pieces.get_clicked_piece(pos)

    def remove_piece(self, taken_piece: Piece):
        self.taken_pieces.append(taken_piece)
        taken_piece.kill()

    def update(
        self, moving_piece: Piece, dest_board_coordinate: tuple[int, int]
    ):
        self.board.update_board_repr(
            dest_board_coordinate,
            moving_piece,
        )
        moving_piece.move(
            dest_board_coordinate,
        )

    @property
    def board_repr(self):
        return self.board.board_repr
