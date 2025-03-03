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
        if white_pieces:
            self.coordinate = [i, 2]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return (move[1] == self.coordinate[1]+1 and move[0] == self.coordinate[0]) and white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces

class BlackPawn(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackPawn, self).__init__()
        self.image = pg.image.load("assets/b_pawn_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = i * 50
        self.rect.top = 300 if not white_pieces else 50
        if not white_pieces:
            self.coordinate = [8-i, 7]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return (move[1] == self.coordinate[1]-1 and move[0] == self.coordinate[0]) and not white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces

class WhiteKnight(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteKnight, self).__init__()
        self.image = pg.image.load("assets/w_knight_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 50 if i == 0 else 300
        self.rect.top = 350 if white_pieces else 0
        if white_pieces:
            self.coordinate = [2 if i == 0 else 7, 1]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces and self.coordinate[0] - 2 == move[0] and (self.coordinate[1] - 1 == move[1] or self.coordinate[1] + 1 == move[1])

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class BlackKnight(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackKnight, self).__init__()
        self.image = pg.image.load("assets/b_knight_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 50 if i == 0 else 300
        self.rect.top = 350 if not white_pieces else 0
        if not white_pieces:
            self.coordinate = [7 if i == 0 else 2, 8]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return not white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class WhiteBishop(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteBishop, self).__init__()
        self.image = pg.image.load("assets/w_bishop_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 100 if i == 0 else 250
        self.rect.top = 350 if white_pieces else 0
        if white_pieces:
            self.coordinate = [3 if i == 0 else 6, 1]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class BlackBishop(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackBishop, self).__init__()
        self.image = pg.image.load("assets/b_bishop_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 100 if i == 0 else 250
        self.rect.top = 350 if not white_pieces else 0
        if not white_pieces:
            self.coordinate = [6 if i == 0 else 3, 8]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return not white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class WhiteRook(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(WhiteRook, self).__init__()
        self.image = pg.image.load("assets/w_rook_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 0 if i == 0 else 350
        self.rect.top = 350 if white_pieces else 0
        if white_pieces:
            self.coordinate = [1 if i == 0 else 8, 1]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces and (self.coordinate[0] == move[0] or self.coordinate[1] == move[1])

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class BlackRook(pg.sprite.Sprite):
    def __init__(self, i: int, white_pieces: bool) -> None:
        super(BlackRook, self).__init__()
        self.image = pg.image.load("assets/b_rook_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 0 if i == 0 else 350
        self.rect.top = 350 if not white_pieces else 0
        if not white_pieces:
            self.coordinate = [8 if i == 0 else 1, 8]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces and (self.coordinate[0] == move[0] or self.coordinate[1] == move[1])

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class WhiteQueen(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(WhiteQueen, self).__init__()
        self.image = pg.image.load("assets/w_queen_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 150
        self.rect.top = 350 if white_pieces else 0
        if white_pieces:
            self.coordinate = [4, 1]
        self.is_taken = False

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class BlackQueen(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(BlackQueen, self).__init__()
        self.image = pg.image.load("assets/b_queen_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 150
        self.rect.top = 350 if not white_pieces else 0
        if not white_pieces:
            self.coordinate = [4, 8]
        self.is_taken = False

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class WhiteKing(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(WhiteKing, self).__init__()
        self.image = pg.image.load("assets/w_king_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 350 if white_pieces else 0
        if white_pieces:
            self.coordinate = [5, 1]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces and ((self.coordinate[0] - 1 == move[0] or self.coordinate[0] + 1 == move[0]) or (self.coordinate[1] - 1 == move[1] or self.coordinate[1] + 1 == move[1]))

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

class BlackKing(pg.sprite.Sprite):
    def __init__(self, white_pieces: bool) -> None:
        super(BlackKing, self).__init__()
        self.image = pg.image.load("assets/b_king_png_128px.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 350 if not white_pieces else 0
        if not white_pieces:
            self.coordinate = [5, 8]

    def allowed_move(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return white_pieces and ((self.coordinate[0] - 1 == move[0] or self.coordinate[0] + 1 == move[0]) or (self.coordinate[1] - 1 == move[1] or self.coordinate[1] + 1 == move[1]))

    def allowed_take(self, white_pieces: bool, move: tuple[int, int]) -> bool:
        return self.allowed_move(white_pieces, move)

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
PieceGroup = WhitePawns | BlackPawns | WhiteKnights | BlackKnights | WhiteBishops | BlackBishops | WhiteRooks | BlackRooks | WhiteQueen | BlackQueen | WhiteKing | BlackKing

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
                    taken_piece: Piece | None = None
                    taken_piece_group: PieceGroup | None = None 
                    board_file, board_rank = int(x/50), int(y/50)
                    board_file_shadow, board_rank_shadow = board_file, board_rank+1
                    is_taking = False
                    if white_pieces:
                        board_rank_shadow = 8 - board_rank
                        for black_pawn in black_pawns:
                            if black_pawn.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = black_pawn
                                taken_piece_group = black_pawns
                                break
                        for black_knight in black_knights:
                            if not is_taking:
                                break
                            if black_knight.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = black_knight
                                taken_piece_group = black_knights
                                break
                        for black_bishop in black_bishops:
                            if not is_taking:
                                break
                            if black_bishop.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = black_bishop
                                taken_piece_group = black_bishops
                                break
                        for black_rook in black_rooks:
                            if not is_taking:
                                break
                            if black_rook.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = black_rook
                                taken_piece_group = black_rooks
                                break
                        if not is_taking:
                            if black_queen.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = black_queen
                                taken_piece_group = black_queen
                            if not is_taking:
                                pass
                            elif black_king.rect.collidepoint(x, y):
                                print("Can't take king")
                                continue
                    else:
                        board_file_shadow = 8 - board_file
                        for white_pawn in white_pawns:
                            if white_pawn.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = white_pawn
                                taken_piece_group = white_pawn
                                break
                        for white_knight in white_knights:
                            if not is_taking:
                                break
                            if white_knight.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = white_knight
                                taken_piece_group = white_knight
                                break
                        for white_bishop in white_bishops:
                            if not is_taking:
                                break
                            if white_bishop.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = white_bishop
                                taken_piece_group = white_bishop
                                break
                        for white_rook in white_rooks:
                            if not is_taking:
                                break
                            if white_rook.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = white_rook
                                taken_piece_group = white_rook
                                break
                        if not is_taking:
                            if white_queen.rect.collidepoint(x, y):
                                is_taking = True
                                taken_piece = white_queen
                                taken_piece_group = white_queen
                            if not is_taking:
                                pass
                            elif white_king.rect.collidepoint(x, y):
                                print("Can't take king")
                                continue
                    move = (board_file_shadow, board_rank_shadow)
                    if not selected_piece.allowed_move(white_pieces, move) and not is_taking:
                        print("piece not allowed")
                        selected_piece = None
                        continue
                    elif not selected_piece.allowed_take(white_pieces, move) and is_taking:
                        print(not selected_piece.allowed_take(white_pieces, move), is_taking)
                        print("piece not allowed to take")
                        selected_piece = None
                        continue
                    selected_piece.rect.left = board_file * 50
                    selected_piece.rect.top = board_rank * 50
                    selected_piece.coordinate = list(move)
                    selected_piece = None
                    if is_taking and taken_piece_group is not None and taken_piece is not None:
                        if (isinstance(taken_piece_group, WhiteQueen) or isinstance(taken_piece_group, BlackQueen)) and (isinstance(taken_piece, WhiteQueen) or isinstance(taken_piece, BlackQueen)):
                            taken_piece_group.is_taken = True
                        elif (isinstance(taken_piece_group, WhiteKing) or isinstance(taken_piece_group, WhiteKing)) and (isinstance(taken_piece, WhiteKing) or isinstance(taken_piece, BlackKing)):
                            pass
                        else:
                            taken_piece_group.remove(taken_piece)
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
        if not white_queen.is_taken:
            screen.blit(white_queen.image, white_queen.rect)
        if not black_queen.is_taken:
            screen.blit(black_queen.image, black_queen.rect)
        screen.blit(white_king.image, white_king.rect)
        screen.blit(black_king.image, black_king.rect)
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()