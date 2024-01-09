from typing import Optional

import pygame as pg

from chess_board.types import Piece

from .piece.groups import BishopGroup, KingGroup, PawnGroup, RookGroup


class Pieces:
    def __init__(self, pieces: str) -> None:
        self.pawns = PawnGroup(pieces)
        self.bishops = BishopGroup(pieces)
        self.rooks = RookGroup(pieces)
        self.kings = KingGroup(pieces)

    def get_clicked_piece(self, pos: tuple[int, int]) -> Optional[Piece]:
        for pawn in self.pawns.sprites():
            if pawn.rect.collidepoint(pos):
                return pawn

        for bishop in self.bishops.sprites():
            if bishop.rect.collidepoint(pos):
                return bishop

        for rook in self.rooks.sprites():
            if rook.rect.collidepoint(pos):
                return rook

        for king in self.kings.sprites():
            if king.rect.collidepoint(pos):
                return king

    def draw(self, screen: pg.surface.Surface):
        self.pawns.draw(screen)
        self.bishops.draw(screen)
        self.rooks.draw(screen)
        self.kings.draw(screen)

    def is_check(self) -> bool:
        opponent_king = self.kings.sprites()[1]
        board_coordinate = opponent_king.board_coordinate
        for pawn in self.pawns.sprites():
            if pawn.is_player_piece:
                if pawn.allowed_take(*board_coordinate):
                    return True
        for bishop in self.bishops.sprites():
            if bishop.is_player_piece:
                if bishop.allowed_take(*board_coordinate):
                    return True
        for rook in self.rooks.sprites():
            if rook.is_player_piece:
                if rook.allowed_take(*board_coordinate):
                    return True
        return False

    def is_checkmate(self, board_repr: list[list[str]]) -> bool:
        # can only check against opponent
        opponent_king = self.kings.sprites()[1]
        x, y = opponent_king.board_coordinate
        move_spots: list[bool] = []
        for king_board_coordinate in [
            (x + 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]:
            try:
                if (
                    king_board_coordinate[0] < 0
                    or king_board_coordinate[1] < 0
                    or board_repr[king_board_coordinate[1]][
                        king_board_coordinate[0]
                    ]
                    != ""
                ):
                    continue
                for pawn in self.pawns.sprites():
                    if pawn.is_player_piece:
                        if pawn.allowed_take(*king_board_coordinate):
                            raise StopIteration
                for bishop in self.bishops.sprites():
                    if bishop.is_player_piece:
                        if bishop.allowed_take(*king_board_coordinate):
                            raise StopIteration
                for rook in self.rooks.sprites():
                    if rook.is_player_piece:
                        if rook.allowed_take(*king_board_coordinate):
                            raise StopIteration
                for king in self.kings.sprites():
                    if king.is_player_piece:
                        if king.allowed_take(*king_board_coordinate):
                            raise StopIteration
                move_spots.append(False)
            except StopIteration:
                move_spots.append(True)
        return move_spots.count(False) > 0

    def check_pin(self, board_repr: list[list[str]]):
        for bishop in self.bishops.sprites():
            if bishop.is_player_piece:
                board_coordinate = bishop.board_coordinate
                for i in range(1, 8):
                    possible_move: tuple[int, int]
                    if (
                        board_coordinate[0] + i < 8
                        and board_coordinate[1] + i < 8
                    ):
                        possible_move = (
                            board_coordinate[0] + i,
                            board_coordinate[1] + i,
                        )
                        self.pin(bishop, board_repr, possible_move)
                    if (
                        board_coordinate[0] - i > -1
                        and board_coordinate[1] - i > -1
                    ):
                        possible_move = (
                            board_coordinate[0] - i,
                            board_coordinate[1] - i,
                        )
                        self.pin(bishop, board_repr, possible_move)
                    if (
                        board_coordinate[0] + i < 8
                        and board_coordinate[1] - i > -1
                    ):
                        possible_move = (
                            board_coordinate[0] + i,
                            board_coordinate[1] - i,
                        )
                        self.pin(bishop, board_repr, possible_move)
                    if (
                        board_coordinate[0] - i > -1
                        and board_coordinate[1] + i < 8
                    ):
                        possible_move = (
                            board_coordinate[0] - i,
                            board_coordinate[1] + i,
                        )
                        self.pin(bishop, board_repr, possible_move)

        # for rook in self.rooks.sprites():
        #     if rook.is_player_piece:
        #         pass

        # for queen in self.queens.sprites():
        #     if queen.is_player_piece:
        #         pass

    def pin(
        self,
        piece: Piece,
        board_repr: list[list[str]],
        possible_move: tuple[int, int],
    ):
        if board_repr[possible_move[1]][possible_move[0]] == "":
            return
        pinned_piece = board_repr[possible_move[1]][possible_move[0]]
        if (
            (
                board_repr[possible_move[1] + 1][possible_move[0] + 1]
                == f"{'w' if piece.is_player_piece else 'b'}k"
            )
            or (
                board_repr[possible_move[1] - 1][possible_move[0] - 1]
                == f"{'w' if piece.is_player_piece else 'b'}k"
            )
            or (
                board_repr[possible_move[1] + 1][possible_move[0] - 1]
                == f"{'w' if piece.is_player_piece else 'b'}k"
            )
            or (
                board_repr[possible_move[1] - 1][possible_move[0] + 1]
                == f"{'w' if piece.is_player_piece else 'b'}k"
            )
        ):
            pass
        else:
            return
        if pinned_piece[1] == "p":
            for pinned_pawn in self.pawns.sprites():
                if pinned_pawn.board_coordinate == possible_move:
                    pinned_pawn.pinned = True
        # elif pinned_piece[1] == "n":
        #     for pinned_knight in self.knights.sprites():
        #         if (
        #             pinned_knight.board_coordinate
        #             == board_coordinate
        #         ):
        #             pinned_knight.pinned = True
        elif pinned_piece[1] == "b":
            for pinned_bishop in self.bishops.sprites():
                if pinned_bishop.board_coordinate == possible_move:
                    pinned_bishop.pinned = True
        elif pinned_piece[1] == "r":
            for pinned_rook in self.rooks.sprites():
                if pinned_rook.board_coordinate == possible_move:
                    pinned_rook.pinned = True
        # elif pinned_piece[1] == "q":
        #     for pinned_queen in self.queens.sprites():
        #         if (
        #             pinned_queen.board_coordinate
        #             == board_coordinate
        #         ):
        #             pinned_queen.pinned = True
        #
