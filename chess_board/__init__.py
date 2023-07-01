from typing import Optional

import pygame as pg

from .board import Board
from .constants import IMAGE_SIZE, Piece, Turn
from .pieces import Pieces
from .players import Opponent, Player


class SelectedPiece(pg.sprite.Group):
    """A container group that contains all moving pieces"""

    def rem_moving(self):
        self.remove(self.sprites()[0])

    def sprites(
        self,
    ) -> list[Piece]:
        return super().sprites()


class TakenPieces(pg.sprite.Group):
    """A container group that contains all taken pieces"""

    def add_to_taken(self, piece):
        self.add(piece)

    def rem_moving(self):
        self.remove(self.sprites()[-1])

    def hide(self):
        for sprite in self.sprites():
            sprite.kill()


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()
        self.screen = screen
        self.turn = Turn.WHITE
        self.player = Player()
        self.opponent = Opponent(self.player)
        self.pieces = Pieces("b" if self.player.pieces[0] == "b" else "w")
        self._board = Board()
        self.moving_piece = SelectedPiece()
        self.taken_piece = TakenPieces()
        self.is_moving = False
        self.is_taking = False
        self.pieces.start_board_repr(self.board_repr)
        # self.board_repr: list[list[str | None]] = [
        #     [None for _ in range(8)] for _ in range(8)
        # ]
        # self.start_board_repr()

    @property
    def board(self):
        return self._board

    @property
    def board_repr(self):
        return self._board.board_repr

    # def start_board_repr(self):
    #     x, y, name = None, None, ""
    #     for black_pawn in self.pieces.black_pawns:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_pawns:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for black_pawn in self.pieces.black_knights:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_knights:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for black_pawn in self.pieces.black_bishops:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_bishops:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for black_pawn in self.pieces.black_rooks:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_rooks:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for black_pawn in self.pieces.black_queens:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_queens:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for black_pawn in self.pieces.black_kings:
    #         (x, y), name = black_pawn.board_coordinate, black_pawn.name
    #         self.set_board_repr((x, y, name))

    #     for white_pawn in self.pieces.white_kings:
    #         (x, y), name = white_pawn.board_coordinate, white_pawn.name
    #         self.set_board_repr((x, y, name))

    def draw(self):
        self.board.draw(self.screen)
        self.draw_pieces()

    def draw_pieces(self):
        self.pieces.black_pawns.draw(self.screen)
        self.pieces.white_pawns.draw(self.screen)
        self.pieces.black_knights.draw(self.screen)
        self.pieces.white_knights.draw(self.screen)
        self.pieces.black_bishops.draw(self.screen)
        self.pieces.white_bishops.draw(self.screen)
        self.pieces.black_rooks.draw(self.screen)
        self.pieces.white_rooks.draw(self.screen)
        self.pieces.black_queens.draw(self.screen)
        self.pieces.white_queens.draw(self.screen)
        self.pieces.black_kings.draw(self.screen)
        self.pieces.white_kings.draw(self.screen)

    # def get_clicked_piece(self, pos: tuple[int, int]):
    #     pass
    # for white_pawn in self.pieces.white_pawns:
    #     if white_pawn.rect.collidepoint(pos):
    #         self.moving_piece.add(white_pawn)
    #         self.is_moving = True

    # for black_pawn in self.pieces.black_pawns:
    #     if black_pawn.rect.collidepoint(pos):
    #         self.moving_piece.add(black_pawn)
    #         self.is_moving = True

    # for white_knight in self.pieces.white_knights:
    #     if white_knight.rect.collidepoint(pos):
    #         self.moving_piece.add(white_knight)
    #         self.is_moving = True

    # for black_knight in self.pieces.black_knights:
    #     if black_knight.rect.collidepoint(pos):
    #         self.moving_piece.add(black_knight)
    #         self.is_moving = True

    # for white_bishop in self.pieces.white_bishops:
    #     if white_bishop.rect.collidepoint(pos):
    #         self.moving_piece.add(white_bishop)
    #         self.is_moving = True

    # for black_bishop in self.pieces.black_bishops:
    #     if black_bishop.rect.collidepoint(pos):
    #         self.moving_piece.add(black_bishop)
    #         self.is_moving = True

    # for white_rook in self.pieces.white_rooks:
    #     if white_rook.rect.collidepoint(pos):
    #         self.moving_piece.add(white_rook)
    #         self.is_moving = True

    # for black_rook in self.pieces.black_rooks:
    #     if black_rook.rect.collidepoint(pos):
    #         self.moving_piece.add(black_rook)
    #         self.is_moving = True

    # for white_queen in self.pieces.white_queens:
    #     if white_queen.rect.collidepoint(pos):
    #         self.moving_piece.add(white_queen)
    #         self.is_moving = True

    # for black_queen in self.pieces.black_queens:
    #     if black_queen.rect.collidepoint(pos):
    #         self.moving_piece.add(black_queen)
    #         self.is_moving = True

    # for white_king in self.pieces.white_kings:
    #     if white_king.rect.collidepoint(pos):
    #         self.moving_piece.add(white_king)
    #         self.is_moving = True

    # for black_king in self.pieces.black_kings:
    #     if black_king.rect.collidepoint(pos):
    #         self.moving_piece.add(black_king)
    #         self.is_moving = True

    # def get_move_pos(self, pos: tuple[int, int]):
    #     for row in self.board.sprites():
    #         if row.rect.collidepoint(pos):
    #             return row

    def set_is_taking(self, move):
        x, y = move.board_coordinate[0], move.board_coordinate[1]
        if self.board_repr[y][x]:
            self.is_moving = False
            self.is_taking = True
            self.taken_piece.add(self.get_taken_piece(pg.mouse.get_pos()))
        else:
            self.is_taking = False

    def get_taken_piece(self, pos: tuple[int, int]) -> Optional[Piece]:
        for white_pawn in self.pieces.white_pawns:
            if white_pawn.rect.collidepoint(pos):
                return white_pawn

        for black_pawn in self.pieces.black_pawns:
            if black_pawn.rect.collidepoint(pos):
                return black_pawn

        for white_knight in self.pieces.white_knights:
            if white_knight.rect.collidepoint(pos):
                return white_knight

        for black_knight in self.pieces.black_knights:
            if black_knight.rect.collidepoint(pos):
                return black_knight

        for white_bishop in self.pieces.white_bishops:
            if white_bishop.rect.collidepoint(pos):
                return white_bishop

        for black_bishop in self.pieces.black_bishops:
            if black_bishop.rect.collidepoint(pos):
                return black_bishop

        for white_rook in self.pieces.white_rooks:
            if white_rook.rect.collidepoint(pos):
                return white_rook

        for black_rook in self.pieces.black_rooks:
            if black_rook.rect.collidepoint(pos):
                return black_rook

        for white_queen in self.pieces.white_queens:
            if white_queen.rect.collidepoint(pos):
                return white_queen

        for black_queen in self.pieces.black_queens:
            if black_queen.rect.collidepoint(pos):
                return black_queen

        for white_king in self.pieces.white_kings:
            if white_king.rect.collidepoint(pos):
                return white_king

        for black_king in self.pieces.black_kings:
            if black_king.rect.collidepoint(pos):
                return black_king

    def ui_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        if self.taken_piece:
            self.taken_piece.hide()
        piece.rect.left, piece.rect.top = (
            pos[0] * IMAGE_SIZE,
            pos[1] * IMAGE_SIZE,
        )
        self.is_moving = False

    def back_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        self.set_board_repr(
            (piece.board_coordinate[0], piece.board_coordinate[1], None),
            (pos[0], pos[1], piece.name),
        )
        piece.board_coordinate = pos
        if isinstance(piece, WhitePawn | BlackPawn):
            if piece.first_move:
                piece.first_move = False
        self.moving_piece.rem_moving()
        # self.change_turn()

    def set_board_repr(self, *args: tuple[int, int]):
        for piece in args:
            self.board_repr[piece[1]][piece[0]] = piece[2]

    def is_piece_allowed_move(self, pos: tuple[int, int]):
        piece = self.moving_piece.sprites()[0]
        x, y = pos
        if self.is_moving:
            return piece.allowed_move(x, y, self.board_repr)
        if self.is_taking:
            return piece.allowed_take(x, y)

    def not_allowed_move(self):
        if self.moving_piece:
            self.moving_piece.rem_moving()
            self.is_moving = False
        if self.is_taking:
            self.taken_piece.rem_moving()
            self.is_taking = False

    def change_turn(self):
        match self.turn:
            case 0:
                self.turn = Turn.BLACK
            case 1:
                self.turn = Turn.WHITE

    def is_player_piece(self):
        moving_piece = self.moving_piece.sprites()
        if moving_piece[0].name[0] == self.player.pieces[0]:
            return True
        return False

    def is_taking_own_pieces(self, move) -> bool | None:
        x, y = move.board_coordinate
        move_pos = self.board_repr[y][x]
        if move_pos:
            return move_pos[0] != self.moving_piece.sprites()[0].name[0]
        return True

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        if self.is_moving:
            move = self.get_move_pos(pos)
            if not move:
                self.not_allowed_move()
                return
            self.set_is_taking(move)
            if not self.is_piece_allowed_move(move.board_coordinate):
                self.not_allowed_move()
                return
            if not self.is_taking_own_pieces(move):
                self.not_allowed_move()
                return
            self.ui_move(move.board_coordinate)
            self.back_move(move.board_coordinate)
        else:
            # if self.turn != self.player:
            #     return
            self.pieces.get_clicked_piece(pos)
            if len(self.moving_piece.sprites()) <= 0:
                return
            if not self.is_player_piece():
                self.not_allowed_move()
                return
            if self.turn != self.moving_piece.sprites()[0].name[0]:
                self.not_allowed_move()
                return
