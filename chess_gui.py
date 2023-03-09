#!/usr/bin/env python
import sys

import pygame as pg
from pygame.event import Event
from pygame.locals import MOUSEBUTTONDOWN

IMAGE_SIZE = 57


class BlackPawn(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pawn = pg.image.load("img/black_pawn.png").convert_alpha()
        self.rect = self.pawn.get_rect()
        self.clicked = False

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.pawn, (self.rect.x, self.rect.y))

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = not self.clicked


class WhitePawn(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pawn = pg.image.load("img/white_pawn.png").convert_alpha()
        self.rect = self.pawn.get_rect()
        self.clicked = False

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.pawn, self.rect)


class BlackKnight(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pawn = pg.image.load("img/black_knight.png").convert_alpha()
        self.rect = self.pawn.get_rect()
        self.clicked = False

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.pawn, self.rect)


class WhiteKnight(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pawn = pg.image.load("img/white_knight.png").convert_alpha()
        self.rect = self.pawn.get_rect()
        self.clicked = False

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.pawn, self.rect)


class ChessBoard(pg.sprite.Sprite):
    global IMAGE_SIZE

    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()

        self.screen = screen

        self.board = [
            [
                pg.image.load(
                    "img/chess_board/white_square.png"
                ).convert_alpha()
                if col % 2 == 0
                else pg.image.load(
                    "img/chess_board/black_square.png"
                ).convert_alpha()
                for col in range(8)
            ]
            if row % 2 == 0
            else [
                pg.image.load(
                    "img/chess_board/black_square.png"
                ).convert_alpha()
                if col % 2 == 0
                else pg.image.load(
                    "img/chess_board/white_square.png"
                ).convert_alpha()
                for col in range(8)
            ]
            for row in range(8)
        ]

        self.board_rect = [
            [
                self.board[row][col].get_rect(
                    topleft=(col * IMAGE_SIZE, row * IMAGE_SIZE)
                )
                for col in range(8)
            ]
            for row in range(8)
        ]

        self.black_pawns = [BlackPawn() for _ in range(8)]
        self.white_pawns = [WhitePawn() for _ in range(8)]
        self.black_knights = [BlackKnight() for _ in range(2)]
        self.white_knights = [WhiteKnight() for _ in range(2)]

    def draw(self):
        for board, board_rect in zip(self.board, self.board_rect):
            for square, square_rect in zip(board, board_rect):
                self.screen.blit(square, square_rect)

    def draw_black_pawns(self):
        for black_pawn in self.black_pawns:
            self.screen.blit(
                black_pawn.pawn, (black_pawn.rect.x, black_pawn.rect.y)
            )

    def draw_white_pawns(self):
        for square, white_pawn in zip(self.board[6], self.white_pawns):
            white_pawn.draw(square)

    def draw_black_knights(self):
        cols = [1, 6]
        for index, black_knight in enumerate(self.black_knights):
            black_knight.draw(self.board[0][cols[index]])

    def draw_white_knights(self):
        cols = [1, 6]
        for index, white_knight in enumerate(self.white_knights):
            white_knight.draw(self.board[7][cols[index]])

    def update(self, event_list: list[Event]):
        for row_index, row in enumerate(self.board):
            for col_index, _ in enumerate(row):
                for black_pawn in self.black_pawns:
                    for event in event_list:
                        if event.type == MOUSEBUTTONDOWN:
                            if black_pawn.clicked:
                                if self.board_rect[row_index][
                                    col_index
                                ].collidepoint(pg.mouse.get_pos()):
                                    black_pawn.rect.x = row_index * IMAGE_SIZE
                                    black_pawn.rect.y = col_index * IMAGE_SIZE


pg.init()


def main():
    size = 600, 500
    color = 255, 255, 255

    screen = pg.display.set_mode(size)

    chess_board = ChessBoard(screen)

    FPS = pg.time.Clock()

    while True:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                sys.exit()

        chess_board.update(event_list)

        for black_pawn in chess_board.black_pawns:
            black_pawn.update(event_list)

        screen.fill(color)

        chess_board.draw()
        chess_board.draw_black_pawns()
        # chess_board.draw_white_pawns()
        # chess_board.draw_black_knights()
        # chess_board.draw_white_knights()

        pg.display.flip()
        FPS.tick(60)


if __name__ == "__main__":
    main()
