#!/usr/bin/env python
import sys

import pygame as pg

from chess_board import ChessBoard

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
            if event.type == pg.MOUSEBUTTONDOWN:
                chess_board.handle_input(event)

        screen.fill(WHITE)

        chess_board.draw()

        pg.display.flip()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
