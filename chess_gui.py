#!/usr/bin/env python
import sys

import pygame as pg

from chess_board import ChessBoard

# from Players import player

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
                if chess_board.is_moving:
                    chess_board.is_player_piece()
                    move = chess_board.get_move_pos(event.pos)
                    if not move:
                        continue
                    if not chess_board.is_piece_allowed_move(
                        move.board_coordinate
                    ):
                        chess_board.not_allowed_move()
                        continue
                    if not chess_board.is_taking_own_pieces(move):
                        chess_board.not_allowed_move()
                        continue
                    chess_board.set_is_taking(move)
                    chess_board.ui_move(move.board_coordinate)
                    chess_board.back_move(move.board_coordinate)
                    chess_board.change_turn()
                else:
                    chess_board.get_clicked_piece(event.pos)

        screen.fill(WHITE)

        chess_board.draw()
        chess_board.draw_pieces()

        pg.display.flip()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
