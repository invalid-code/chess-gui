import pygame as pg
from pygame._sdl2 import messagebox

from chess_board.pieces import Pieces

from .board import Board, Square
from .piece import Bishop, King, Knight, Pawn, Queen, Rook
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
        self.selected_piece: Piece | None = None
        self.is_check = False
        self.is_checkmate = False

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        if self.selected_piece:
            selected_square = self.board.get_clicked_square(pos)
            if not selected_square:
                return
            dest_coordinate = selected_square.board_coordinate
            if self.board.has_piece(dest_coordinate):
                self.take(selected_square)
            elif (
                self.selected_piece.name == f"{self.player.piece_color[0]}p"
                and self.selected_piece.allowed_take(*dest_coordinate)
            ):
                self.en_passant(dest_coordinate)
            else:
                # moving
                if not self.selected_piece.allowed_move(*dest_coordinate):
                    return self.reset()
                self.pin()
                if isinstance(self.selected_piece, Pawn):
                    self.set_en_passant(dest_coordinate)
                if isinstance(self.selected_piece, King):
                    self.castle_rook(dest_coordinate)
            if self.selected_piece:
                self.update_piece(self.selected_piece, dest_coordinate)
            if isinstance(self.selected_piece, Pawn):
                self.promote()
            self.reset()
            self.is_check = self.pieces.is_check()
            self.pieces.check_pin(self.board_repr)
            # want to redo this part
            if self.is_check:
                self.is_checkmate = self.pieces.is_checkmate(self.board_repr)
            #
        else:
            self.selected_piece = self.get_clicked_piece(pos)

    def pin(self):
        if isinstance(self.selected_piece, Pawn):
            if self.selected_piece.pinned:
                return self.reset()
        if isinstance(self.selected_piece, Bishop):
            if self.selected_piece.pinned:
                return self.reset()
        if isinstance(self.selected_piece, Rook):
            if self.selected_piece.pinned:
                return self.reset()

    def take(self, selected_square: Square):
        taken_piece = self.get_clicked_piece(selected_square.rect.center)
        if not taken_piece:
            return self.reset()
        if taken_piece.is_player_piece:
            return self.reset()
        if isinstance(taken_piece, King):
            return self.reset()
        if not self.selected_piece.allowed_take(*taken_piece.board_coordinate):
            return self.reset()
        self.remove_piece(taken_piece)

    def set_en_passant(self, dest_coordinate: tuple[int, int]):
        if not self.selected_piece.first_move:
            return
        if (
            self.board_repr[dest_coordinate[1]][dest_coordinate[0] - 1]
            != f"{self.player.piece_color[0]}p"
            or self.board_repr[dest_coordinate[1]][dest_coordinate[0] + 1]
            != f"{self.player.piece_color[0]}p"
        ):
            return
        self.selected_piece.en_passant = True

    def castle_rook(self, dest_coordinate: tuple[int, int]):
        if not self.selected_piece.first_move:
            return self.reset()
        if self.selected_piece.board_coordinate[0] + 2 == dest_coordinate[0]:
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
        if self.selected_piece.board_coordinate[0] - 2 == dest_coordinate[0]:
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

    def promote(self):
        if self.selected_piece.board_coordinate[1] == 0:
            # make opponent be able to promote
            promote_window = messagebox(
                "promote window",
                "",
                buttons=("Knight", "Bishop", "Rook", "Queen"),
            )
            print(promote_window)
            match promote_window:
                case 0:
                    self.pieces.knights.add(
                        Knight(
                            f"{self.player.piece_color[0]}",
                            f"img/{self.player.piece_color}_knight.png",
                            self.selected_piece.board_coordinate,
                            True,
                        )
                    )
                case 1:
                    self.pieces.bishops.add(
                        Bishop(
                            f"{self.player.piece_color[0]}",
                            f"img/{self.player.piece_color}_bishop.png",
                            self.selected_piece.board_coordinate,
                            True,
                        )
                    )
                case 2:
                    self.pieces.rooks.add(
                        Rook(
                            f"{self.player.piece_color[0]}",
                            f"img/{self.player.piece_color}_rook.png",
                            self.selected_piece.board_coordinate,
                            True,
                        )
                    )
                case 3:
                    self.pieces.queens.add(
                        Queen(
                            f"{self.player.piece_color[0]}",
                            f"img/{self.player.piece_color}_queen.png",
                            self.selected_piece.board_coordinate,
                            True,
                        )
                    )
                case _:
                    pass
            self.selected_piece.kill()

    def en_passant(self, dest_coordinate: tuple[int, int]):
        if (
            self.board_repr[dest_coordinate[1] + 1][dest_coordinate[0]]
            == f"{self.opponent.piece_color[0]}p"
        ):
            for pawn in self.pieces.pawns.sprites():
                if pawn.is_player_piece:
                    continue
                if not (
                    pawn.board_coordinate
                    == (
                        dest_coordinate[0],
                        dest_coordinate[1] + 1,
                    )
                ):
                    continue
                if pawn.en_passant:
                    continue
                self.board_repr[pawn.board_coordinate[1]][
                    pawn.board_coordinate[0]
                ] = ""
                self.remove_piece(pawn)
        else:
            self.reset()

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
