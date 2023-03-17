#!/usr/bin/env python
import sys

import pygame as pg

from chess_board.chess_board import ChessBoard

# from pygame import Color

pg.init()

SIZE = 600, 500
WHITE = 255, 255, 255


def main():
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("chess clone")

    chess_board = ChessBoard(screen)

    CLOCK = pg.time.Clock()

    while True:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        chess_board.update(event_list)

        for black_pawn in chess_board.black_pawns:
            black_pawn.update(event_list)

        for white_pawn in chess_board.white_pawns:
            white_pawn.update(event_list)

        screen.fill(WHITE)

        chess_board.draw()
        chess_board.draw_black_pawns()
        chess_board.draw_white_pawns()

        pg.display.flip()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
