import math
import random as rand
import time
from random import randint

import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = (900, 600)

class WhitePawn(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhitePawn, self).__init__()
        self.image = pg.image.load("assets/w_pawn_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = i * 50
        self.rect.top = 300 if white_pieces else 50

class BlackPawn(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackPawn, self).__init__()
        self.image = pg.image.load("assets/b_pawn_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = i * 50
        self.rect.top = 300 if not white_pieces else 50

class WhiteKnight(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteKnight, self).__init__()
        self.image = pg.image.load("assets/w_knight_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 50 if i == 0 else 300
        self.rect.top = 350 if white_pieces else 0

class BlackKnight(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackKnight, self).__init__()
        self.image = pg.image.load("assets/b_knight_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 50 if i == 0 else 300
        self.rect.top = 350 if not white_pieces else 0

class WhiteBishop(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteBishop, self).__init__()
        self.image = pg.image.load("assets/w_bishop_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 100 if i == 0 else 250
        self.rect.top = 350 if white_pieces else 0

class BlackBishop(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackBishop, self).__init__()
        self.image = pg.image.load("assets/b_bishop_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 100 if i == 0 else 250
        self.rect.top = 350 if not white_pieces else 0

class WhiteRook(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteRook, self).__init__()
        self.image = pg.image.load("assets/w_rook_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 0 if i == 0 else 350
        self.rect.top = 350 if white_pieces else 0

class BlackRook(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackRook, self).__init__()
        self.image = pg.image.load("assets/b_rook_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 0 if i == 0 else 350
        self.rect.top = 350 if not white_pieces else 0

class WhiteQueen(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(WhiteQueen, self).__init__()
        self.image = pg.image.load("assets/w_queen_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 150
        self.rect.top = 350 if white_pieces else 0

class BlackQueen(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(BlackQueen, self).__init__()
        self.image = pg.image.load("assets/b_queen_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 150
        self.rect.top = 350 if not white_pieces else 0

class WhiteKing(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(WhiteKing, self).__init__()
        self.image = pg.image.load("assets/w_king_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 350 if white_pieces else 0

class BlackKing(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(BlackKing, self).__init__()
        self.image = pg.image.load("assets/b_king_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 350 if not white_pieces else 0

class WhitePawns(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class BlackPawns(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class WhiteKnights(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class BlackKnights(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class WhiteBishops(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class BlackBishops(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class WhiteRooks(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

class BlackRooks(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

Piece = WhitePawn | BlackPawn | WhiteKnight | BlackKnight | WhiteBishop | BlackBishop | WhiteRook | BlackRook | WhiteQueen | BlackQueen | WhiteKing | BlackKing

def main(): 
    rand.seed(time.time())
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    selected_piece: None | Piece = None
    white_pieces = bool(randint(0, 1))
    white_square = pg.Surface((50, 50))
    white_square.fill((255, 255, 255))
    black_square = pg.Surface((50, 50))
    black_square.fill((0, 0, 0))
    white_pawns = WhitePawns()
    for i in range(8):
        white_pawns.add(WhitePawn(i, white_pieces))
    black_pawns = BlackPawns()
    for i in range(8):
        black_pawns.add(BlackPawn(i, white_pieces))
    white_knights = WhiteKnights()
    for i in range(2):
        white_knights.add(WhiteKnight(i, white_pieces))
    black_knights = BlackKnights()
    for i in range(2):
        black_knights.add(BlackKnight(i, white_pieces))
    white_bishops = WhiteBishops()
    for i in range(2):
        white_bishops.add(WhiteBishop(i, white_pieces))
    black_bishops = BlackBishops()
    for i in range(2):
        black_bishops.add(BlackBishop(i, white_pieces))
    white_rooks = WhiteRooks()
    for i in range(2):
        white_rooks.add(WhiteRook(i, white_pieces))
    black_rooks = BlackRooks()
    for i in range(2):
        black_rooks.add(BlackRook(i, white_pieces))    
    white_queen = WhiteQueen(white_pieces)
    black_queen = BlackQueen(white_pieces)
    white_king = WhiteKing(white_pieces)
    black_king = BlackKing(white_pieces)
    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = int(event.dict["pos"][0]), int(event.dict["pos"][1])
                if selected_piece is not None:
                    board_rank, board_file = int(x/50), int(y/50)
                    selected_piece.rect.left = board_rank * 50
                    selected_piece.rect.top = board_file * 50
                    selected_piece = None
                else:
                    if white_pieces:
                        for white_pawn in white_pawns:
                            if white_pawn.rect.collidepoint(x, y):
                                selected_piece = white_pawn
                                break
                        for white_knight in white_knights:
                            if selected_piece is not None:
                                break
                            if white_knight.rect.collidepoint(x, y):
                                selected_piece = white_knight
                        for white_bishop in white_bishops:
                            if selected_piece is not None:
                                break
                            if white_bishop.rect.collidepoint(x, y):
                                selected_piece = white_bishop
                        for white_rook in white_rooks:
                            if selected_piece is not None:
                                break
                            if white_rook.rect.collidepoint(x, y):
                                selected_piece = white_rook
                        if selected_piece is None:
                            if white_queen.rect.collidepoint(x, y):
                                selected_piece = white_queen
                            if selected_piece is not None:
                                pass
                            elif white_king.rect.collidepoint(x, y):
                                selected_piece = white_king
                    else:
                        for black_pawn in black_pawns:
                            if black_pawn.rect.collidepoint(x, y):
                                selected_piece = black_pawn
                                break
                        for black_knight in black_knights:
                            if selected_piece is not None:
                                break
                            if black_knight.rect.collidepoint(x, y):
                                selected_piece = black_knight
                        for black_bishop in black_bishops:
                            if selected_piece is not None:
                                break
                            if black_bishop.rect.collidepoint(x, y):
                                selected_piece = black_bishop
                        for black_rook in black_rooks:
                            if selected_piece is not None:
                                break
                            if black_rook.rect.collidepoint(x, y):
                                selected_piece = black_rook
                        if selected_piece is None:
                            if black_queen.rect.collidepoint(x, y):
                                selected_piece = black_queen
                            if selected_piece is not None:
                                pass
                            elif black_king.rect.collidepoint(x, y):
                                selected_piece = black_king
            if event.type == pg.QUIT:
                game_running = False
        for i in range(8):
            for j in range(8):
                if white_pieces:
                    if i % 2 == 0:
                        if j % 2 == 0:
                            screen.blit(white_square, (j*50, i*50))
                        else:
                            screen.blit(black_square, (j*50, i*50))
                    else:
                        if j % 2 == 0:
                            screen.blit(black_square, (j*50, i*50))
                        else:
                            screen.blit(white_square, (j*50, i*50))
                else:
                    if i % 2 == 0:
                        if j % 2 == 0:
                            screen.blit(black_square, (j*50, i*50))
                        else:
                            screen.blit(white_square, (j*50, i*50))
                    else:
                        if j % 2 == 0:
                            screen.blit(white_square, (j*50, i*50))
                        else:
                            screen.blit(black_square, (j*50, i*50))
        white_pawns.draw(screen)
        black_pawns.draw(screen)
        white_knights.draw(screen)
        black_knights.draw(screen)
        white_bishops.draw(screen)
        black_bishops.draw(screen)
        white_rooks.draw(screen)
        black_rooks.draw(screen)
        screen.blit(white_queen.image, white_queen.rect)
        screen.blit(black_queen.image, black_queen.rect)
        screen.blit(white_king.image, white_king.rect)
        screen.blit(black_king.image, black_king.rect)
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()