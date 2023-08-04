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
        if self.is_check:
            if self.is_checkmate:
                return
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
                if (
                    taken_piece.is_player_piece
                    or taken_piece.name[1] == "k"
                    or not self.selected_piece.allowed_take(
                        *taken_piece.board_coordinate
                    )
                ):
                    return self.reset()
                self.take(taken_piece)
            elif (
                self.board_repr[dest_board_coordinate[1] + 1][
                    dest_board_coordinate[0]
                ]
                == f"{self.opponent.piece_color[0]}p"
                and self.selected_piece.name
                == f"{self.player.piece_color[0]}p"
            ):
                for pawn in self.pieces.pawns.sprites():
                    if (
                        (pawn.is_player_piece)
                        or (
                            not pawn.board_coordinate
                            == (
                                dest_board_coordinate[0],
                                dest_board_coordinate[1] + 1,
                            )
                        )
                        or (not pawn.en_passant)
                        or (
                            not self.selected_piece.allowed_take(
                                *dest_board_coordinate
                            )
                        )
                    ):
                        pass
                    else:
                        self.board_repr[pawn.board_coordinate[1]][
                            pawn.board_coordinate[0]
                        ] = ""
                        self.take(pawn)
                        break
            else:
                if not self.selected_piece.allowed_move(
                    *dest_board_coordinate
                ):
                    return self.reset()
                match self.selected_piece.name[1]:
                    case "p":
                        if (not self.selected_piece.first_move) or not (
                            (
                                self.board_repr[dest_board_coordinate[1]][
                                    dest_board_coordinate[0] - 1
                                ]
                                == f"{self.player.piece_color[0]}p"
                            )
                            or (
                                self.board_repr[dest_board_coordinate[1]][
                                    dest_board_coordinate[0] + 1
                                ]
                                == f"{self.player.piece_color[0]}p"
                            )
                        ):
                            pass
                        else:
                            self.selected_piece.en_passant = True
                    case "k":
                        if (
                            self.selected_piece.board_coordinate[0] + 2
                            == dest_board_coordinate[0]
                        ):
                            rook = self.pieces.rooks.sprites()[1]
                            if not rook.first_move:
                                return self.reset()
                            board_coordinate = (
                                rook.board_coordinate[0] - 2,
                                rook.board_coordinate[1],
                            )
                            self.move(rook, board_coordinate)
                        elif (
                            self.selected_piece.board_coordinate[0] - 2
                            == dest_board_coordinate[0]
                        ):
                            rook = self.pieces.rooks.sprites()[0]
                            if not rook.first_move:
                                return self.reset()
                            board_coordinate = (
                                rook.board_coordinate[0] + 3,
                                rook.board_coordinate[1],
                            )
                            self.move(rook, board_coordinate)
            self.move(self.selected_piece, dest_board_coordinate)
            if self.selected_piece.name[1] == "p":
                self.selected_piece.promote()
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

    def take(self, taken_piece: Piece):
        self.taken_pieces.append(taken_piece)
        taken_piece.kill()

    def move(
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
