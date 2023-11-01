from typing import Optional

import pygame as pg
from pygame._sdl2 import messagebox

from chess_board.pieces import Pieces

from .board import Board
from .piece import King, Pawn
from .players import Opponent, Player
from .types import Piece


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.player = Player()
        self.opponent = Opponent(self.player)
        self.pieces = Pieces(self.player.piece_color)
        self.board = Board(self.pieces)
        self.taken_pieces: list[Piece] = []
        self.selected_piece: Optional[Piece] = None
        self.is_check = False
        self.is_checkmate = False

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        # if self.is_checkmate:
        #     return
        if self.selected_piece:
            selected_square = self.board.get_clicked_square(pos)
            if not selected_square:
                return
            dest_coordinate = selected_square.board_coordinate
            if self.board.has_piece(dest_coordinate):
                # taking
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
                and self.selected_piece.allowed_take(*dest_coordinate)
            ):
                # en passant taking
                if (
                    self.board_repr[dest_coordinate[1] + 1][dest_coordinate[0]]
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
                                dest_coordinate[0],
                                dest_coordinate[1] + 1,
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
            else:
                # moving
                if not self.selected_piece.allowed_move(*dest_coordinate):
                    return self.reset()
                if isinstance(self.selected_piece, Pawn):
                    # update opponent pawn that is that can be taken with en passant
                    if not self.selected_piece.first_move:
                        pass
                    elif (
                        self.board_repr[dest_coordinate[1]][
                            dest_coordinate[0] - 1
                        ]
                        != f"{self.player.piece_color[0]}p"
                    ):
                        pass
                    elif (
                        self.board_repr[dest_coordinate[1]][
                            dest_coordinate[0] + 1
                        ]
                        != f"{self.player.piece_color[0]}p"
                    ):
                        pass
                    else:
                        self.selected_piece.en_passant = True
                if isinstance(self.selected_piece, King):
                    # update rooks if it was a castle move
                    if (
                        self.selected_piece.board_coordinate[0] + 2
                        == dest_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[1]
                        if not rook.first_move:
                            return self.reset()
                        self.update_piece(
                            rook,
                            (
                                rook.board_coordinate[0] - 2,
                                rook.board_coordinate[1],
                            ),
                        )
                    if (
                        self.selected_piece.board_coordinate[0] - 2
                        == dest_coordinate[0]
                    ):
                        rook = self.pieces.rooks.sprites()[0]
                        if not rook.first_move:
                            return self.reset()
                        self.update_piece(
                            rook,
                            (
                                rook.board_coordinate[0] + 3,
                                rook.board_coordinate[1],
                            ),
                        )
            self.update_piece(self.selected_piece, dest_coordinate)
            if isinstance(self.selected_piece, Pawn):
                # check if we can promote
                if self.selected_piece.board_coordinate[1] != 0:
                    pass
                else:
                    promote_window = messagebox(
                        "promote window", "", buttons=("H", "B", "R", "Q")
                    )
                    self.selected_piece.kill()
                    match promote_window:
                        case 0:
                            # self.pieces.knights.add()
                            pass
                        case 1:
                            # self.pieces.bishops.add(Knight(""))
                            pass
                        case 2:
                            # self.pieces.rooks.add(Rook())
                            pass
                        case 3:
                            # self.pieces.queens.add()
                            pass

            self.reset()
            self.is_check = self.pieces.is_check()
            if self.is_check:
                self.is_checkmate = self.pieces.is_checkmate(self.board_repr)
        else:
            self.selected_piece = self.get_clicked_piece(pos)

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

    def update_piece(self, piece: Piece, dest: tuple[int, int]):
        self.board.update_board(
            dest,
            piece,
        )
        piece.move(
            dest,
        )

    @property
    def board_repr(self):
        return self.board.board_repr


class WinningScreen:
    def __init__(self, won: bool):
        self.won = won
