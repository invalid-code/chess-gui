#!/usr/bin/env python
import sys
from typing import Tuple

import pygame as pg
from pygame.event import Event
from pygame.locals import MOUSEBUTTONDOWN

IMAGE_SIZE = 57
SIZE = 600, 500
WHITE = 255, 255, 255


class Piece(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.piece = pg.Surface((50, 50))
        self.rect = self.piece.get_rect()
        self.clicked = False

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.piece, self.rect)

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = not self.clicked


class BlackPawn(Piece):
    def __init__(self, pos: Tuple[int, int]) -> None:
        super().__init__()
        self.piece = pg.image.load("img/black_pawn.png").convert_alpha()
        self.rect = self.piece.get_rect(topleft=pos)
        self.clicked = False


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
            BlackPawn((index * IMAGE_SIZE, IMAGE_SIZE)) for index in range(8)
        ]

    def draw(self):
        for boardi, board in enumerate(self.board):
            for squarei, square in enumerate(board):
                self.screen.blit(square, self.board_rect[boardi][squarei])

    def draw_black_pawns(self):
        for black_pawn in self.black_pawns:
            self.screen.blit(black_pawn.piece, black_pawn.rect)

    def get_square(self):
        for rowi, row in enumerate(self.board_rect):
            for coli, col in enumerate(row):
                if col.collidepoint(pg.mouse.get_pos()):
                    return rowi * IMAGE_SIZE, coli * IMAGE_SIZE

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = self.get_square()
                if mouse_pos:
                    self.update_black_pawns(mouse_pos)

    def update_black_pawns(self, pos: Tuple[int, int]):
        for black_pawn in self.black_pawns:
            if black_pawn.clicked:
                black_pawn.rect.top, black_pawn.rect.left = pos
                black_pawn.clicked = not black_pawn.clicked


pg.init()


def main():
    screen = pg.display.set_mode(SIZE)

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

        screen.fill(WHITE)

        chess_board.draw()
        chess_board.draw_black_pawns()

        pg.display.flip()
        FPS.tick(60)


if __name__ == "__main__":
    main()
