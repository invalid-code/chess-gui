import pygame as pg

from .board import Board
from .pieces import Pieces
from .players import Opponent, Player
from .types import Turn


class ChessBoard:
    def __init__(self, screen: pg.surface.Surface) -> None:
        self.screen = screen
        self.turn = Turn.WHITE
        self.player = Player()
        self.opponent = Opponent(self.player)
        self.pieces = Pieces(self.player.pieces)
        self.board = Board()
        self.selected_piece = None
        self.taken_piece = []
        self.pieces.start_board_repr(self.board_repr)

    @property
    def board_repr(self):
        return self.board.board_repr

    def get_clicked_piece(self, pos: tuple[int, int]):
        return self.pieces.get_clicked_piece(pos)

    def get_clicked_square(self, pos: tuple[int, int]):
        return self.board.get_clicked_square(pos)

    def handle_input(self, event: pg.event.Event):
        pos: tuple[int, int] = event.dict["pos"]
        selected_piece = self.get_clicked_piece(pos)
        if not selected_piece:
            return
        selected_square = self.get_clicked_square(pos)
        if not selected_square:
            return
        selected_piece.move(selected_square.rect.topleft)

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

    # def get_move_pos(self, pos: tuple[int, int]):
    #     for row in self.board.sprites():
    #         if row.rect.collidepoint(pos):
    #             return row

    # def set_is_taking(self, move):
    #     x, y = move.board_coordinate[0], move.board_coordinate[1]
    #     if self.board_repr[y][x]:
    #         self.is_moving = False
    #         self.is_taking = True
    #         self.taken_piece.add(self.get_taken_piece(pg.mouse.get_pos()))
    #     else:
    #         self.is_taking = False

    # def get_taken_piece(self, pos: tuple[int, int]) -> Optional[Piece]:
    #     for white_pawn in self.pieces.white_pawns:
    #         if white_pawn.rect.collidepoint(pos):
    #             return white_pawn

    #     for black_pawn in self.pieces.black_pawns:
    #         if black_pawn.rect.collidepoint(pos):
    #             return black_pawn

    #     for white_knight in self.pieces.white_knights:
    #         if white_knight.rect.collidepoint(pos):
    #             return white_knight

    #     for black_knight in self.pieces.black_knights:
    #         if black_knight.rect.collidepoint(pos):
    #             return black_knight

    #     for white_bishop in self.pieces.white_bishops:
    #         if white_bishop.rect.collidepoint(pos):
    #             return white_bishop

    #     for black_bishop in self.pieces.black_bishops:
    #         if black_bishop.rect.collidepoint(pos):
    #             return black_bishop

    #     for white_rook in self.pieces.white_rooks:
    #         if white_rook.rect.collidepoint(pos):
    #             return white_rook

    #     for black_rook in self.pieces.black_rooks:
    #         if black_rook.rect.collidepoint(pos):
    #             return black_rook

    #     for white_queen in self.pieces.white_queens:
    #         if white_queen.rect.collidepoint(pos):
    #             return white_queen

    #     for black_queen in self.pieces.black_queens:
    #         if black_queen.rect.collidepoint(pos):
    #             return black_queen

    #     for white_king in self.pieces.white_kings:
    #         if white_king.rect.collidepoint(pos):
    #             return white_king

    #     for black_king in self.pieces.black_kings:
    #         if black_king.rect.collidepoint(pos):
    #             return black_king

    # def ui_move(self, pos: tuple[int, int]):
    #     piece = self.moving_piece.sprites()[0]
    #     if self.taken_piece:
    #         self.taken_piece.hide()
    #     piece.rect.left, piece.rect.top = (
    #         pos[0] * IMAGE_SIZE,
    #         pos[1] * IMAGE_SIZE,
    #     )
    #     self.is_moving = False

    # def back_move(self, pos: tuple[int, int]):
    #     piece = self.moving_piece.sprites()[0]
    #     self.set_board_repr(
    #         (piece.board_coordinate[0], piece.board_coordinate[1], None),
    #         (pos[0], pos[1], piece.name),
    #     )
    #     piece.board_coordinate = pos
    #     if isinstance(piece, WhitePawn | BlackPawn):
    #         if piece.first_move:
    #             piece.first_move = False
    #     self.moving_piece.rem_moving()
    # self.change_turn()

    # def set_board_repr(self, *args: tuple[int, int]):
    #     for piece in args:
    #         self.board_repr[piece[1]][piece[0]] = piece[2]

    # def is_piece_allowed_move(self, pos: tuple[int, int]):
    #     piece = self.selected_piece.sprites()[0]
    #     x, y = pos
    #     if self.is_moving:
    #         return piece.allowed_move(x, y, self.board_repr)
    #     if self.is_taking:
    #         return piece.allowed_take(x, y)

    # def not_allowed_move(self):
    #     if self.selected_piece:
    #         self.selected_piece.rem_moving()
    #         self.is_moving = False
    #     if self.is_taking:
    #         self.taken_piece.rem_moving()
    #         self.is_taking = False

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
