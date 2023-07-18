# from typing import Literal

import pygame as pg

from .piece.groups import KingGroup, PawnGroup


class Pieces:
    def __init__(self, pieces: str) -> None:
        self.pawns = PawnGroup(pieces)
        self.kings = KingGroup(pieces)

    def get_clicked_piece(self, pos: tuple[int, int]):
        for pawn in self.pawns.sprites():
            if pawn.rect.collidepoint(pos):
                return pawn

        for king in self.kings.sprites():
            if king.rect.collidepoint(pos):
                return king

    def draw(self, screen: pg.surface.Surface):
        self.pawns.draw(screen)
        self.kings.draw(screen)

    def is_check(self):
        opponent_king = self.kings.sprites()[1]
        for pawn in self.pawns.sprites():
            if pawn.is_player_piece:
                if pawn.allowed_take(*opponent_king.board_coordinate):
                    return True
        return False

    def is_checkmate(self, board_repr: list[list[str]]):
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
                for king in self.kings.sprites():
                    if king.is_player_piece:
                        if king.allowed_take(*king_board_coordinate):
                            raise StopIteration
                move_spots.append(False)
            except StopIteration as _:
                move_spots.append(True)
        if move_spots.count(False) > 0:
            return False
        return True
