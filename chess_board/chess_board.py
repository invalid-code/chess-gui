from typing import Literal

import pygame as pg
from pygame.event import Event
from pygame.locals import MOUSEBUTTONDOWN

IMAGE_SIZE = 57


class Piece(pg.sprite.Sprite):
    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__()
        self.piece = pg.Surface((50, 50))
        self.rect = (
            self.piece.get_rect()
            if not pos
            else self.piece.get_rect(topleft=pos)
        )
        self.board_coordinate = board_coordinate
        self.clicked = False
        self.is_alive = True

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.piece, self.rect)

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = not self.clicked


class BlackPawn(Piece):
    name = "bp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.piece = pg.image.load("img/black_pawn.png").convert_alpha()
        # self.rect = self.piece.get_rect(topleft=pos)
        # self.board_coordinate = board_coordinate


class WhitePawn(Piece):
    name = "wp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.piece = pg.image.load("img/white_pawn.png").convert_alpha()
        # self.rect = self.piece.get_rect(topleft=pos)


class ChessBoard(pg.sprite.Sprite):
    global IMAGE_SIZE

    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()

        self.screen = screen
        white_square = pg.image.load(
            "img/chess_board/white_square.png"
        ).convert_alpha()
        black_square = pg.image.load(
            "img/chess_board/black_square.png"
        ).convert_alpha()

        self.board = [
            [
                white_square if col % 2 == 0 else black_square
                for col in range(8)
            ]
            if row % 2 == 0
            else [
                black_square if col % 2 == 0 else white_square
                for col in range(8)
            ]
            for row in range(8)
        ]

        self.board_rect = [
            [
                col.get_rect(topleft=(coli * IMAGE_SIZE, rowi * IMAGE_SIZE))
                for coli, col in enumerate(row)
            ]
            for rowi, row in enumerate(self.board)
        ]

        self.black_pawns = [
            BlackPawn((index * IMAGE_SIZE, IMAGE_SIZE), (index, 1))
            for index in range(8)
        ]

        self.white_pawns = [
            WhitePawn((index * IMAGE_SIZE, IMAGE_SIZE * 6), (index, 6))
            for index in range(8)
        ]

        self.board_repr: list[list[str | None]] = []
        for rowi in range(8):
            row = []
            for coli in range(8):
                if rowi == 1:
                    row.append(BlackPawn.name)
                elif rowi == 6:
                    row.append(WhitePawn.name)
                else:
                    row.append(None)
            self.board_repr.append(row)

    def draw(self):
        for boardi, board in enumerate(self.board):
            for squarei, square in enumerate(board):
                self.screen.blit(square, self.board_rect[boardi][squarei])

    def draw_black_pawns(self):
        for black_pawn in self.black_pawns:
            self.screen.blit(black_pawn.piece, black_pawn.rect)

    def draw_white_pawns(self):
        for white_pawn in self.white_pawns:
            self.screen.blit(white_pawn.piece, white_pawn.rect)

    def active_piece(self):
        for black_pawn in self.black_pawns:
            if black_pawn.clicked:
                return black_pawn

        for white_pawn in self.white_pawns:
            if white_pawn.clicked:
                return white_pawn

    def move(
        self,
    ) -> BlackPawn | WhitePawn | dict[str, int] | None:
        for rowi, row in enumerate(self.board_rect):
            for coli, col in enumerate(row):
                if col.collidepoint(pg.mouse.get_pos()):
                    if self.board_rect[rowi][coli]:
                        for black_pawn in self.black_pawns:
                            if black_pawn.board_coordinate == (coli, rowi):
                                return black_pawn

                        for white_pawn in self.white_pawns:
                            if white_pawn.board_coordinate == (coli, rowi):
                                return white_pawn
                    else:
                        return {
                            "row": rowi,
                            "col": coli,
                            "left": col.left,
                            "top": col.top,
                        }

    def set_board_repr(self, x: int, y: int, value: str | None = None):
        self.board_repr[y][x] = value

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                active_piece = self.active_piece()
                if active_piece:
                    moved_pos = self.move()
                    if moved_pos:
                        if isinstance(moved_pos, dict):
                            self.set_board_repr(
                                active_piece.board_coordinate[0],
                                active_piece.board_coordinate[1],
                            )
                            self.set_board_repr(
                                moved_pos["col"],
                                moved_pos["row"],
                                active_piece.name,
                            )
                            active_piece.rect.top, active_piece.rect.left = (
                                moved_pos["top"],
                                moved_pos["left"],
                            )
                        else:
                            self.set_board_repr(
                                active_piece.board_coordinate[0],
                                active_piece.board_coordinate[1],
                            )
                            self.set_board_repr(
                                moved_pos.board_coordinate[0],
                                moved_pos.board_coordinate[1],
                                active_piece.name,
                            )
                            moved_pos.piece.fill((0, 0, 0, 0))
                            active_piece.rect.top, active_piece.rect.left = (
                                moved_pos.rect.top,
                                moved_pos.rect.left,
                            )
                            moved_pos.is_alive = False
                        active_piece.clicked = not active_piece.clicked
