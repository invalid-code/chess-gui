import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = (900, 600)

class Square(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(Square, self).__init__()
        self.surf = pg.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

class WhitePawn(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(WhitePawn, self).__init__()
        self.surf = pg.image.load("assets/w_pawn_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = i * 50
        self.rect.top = 300

class BlackPawn(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(BlackPawn, self).__init__()
        self.surf = pg.image.load("assets/b_pawn_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = i * 50
        self.rect.top = 50

class WhiteKnight(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(WhiteKnight, self).__init__()
        self.surf = pg.image.load("assets/w_knight_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 50
            self.rect.top = 350
        else:
            self.rect.left = 300
            self.rect.top = 350

class BlackKnight(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(BlackKnight, self).__init__()
        self.surf = pg.image.load("assets/b_knight_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 50
            self.rect.top = 0
        else:
            self.rect.left = 300
            self.rect.top = 0

class WhiteBishop(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(WhiteBishop, self).__init__()
        self.surf = pg.image.load("assets/w_bishop_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 100
            self.rect.top = 350
        else:
            self.rect.left = 250
            self.rect.top = 350

class BlackBishop(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(BlackBishop, self).__init__()
        self.surf = pg.image.load("assets/b_bishop_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 100
            self.rect.top = 0
        else:
            self.rect.left = 250
            self.rect.top = 0

class WhiteRook(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(WhiteRook, self).__init__()
        self.surf = pg.image.load("assets/w_rook_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 0
            self.rect.top = 350
        else:
            self.rect.left = 350
            self.rect.top = 350

class BlackRook(pg.sprite.Sprite):
    def __init__(self, i: int) -> None:
        super(BlackRook, self).__init__()
        self.surf = pg.image.load("assets/b_rook_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        if i == 0:
            self.rect.left = 0
            self.rect.top = 0
        else:
            self.rect.left = 350
            self.rect.top = 0

class WhiteQueen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteQueen, self).__init__()
        self.surf = pg.image.load("assets/w_queen_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = 150
        self.rect.top = 350

class BlackQueen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackQueen, self).__init__()
        self.surf = pg.image.load("assets/b_queen_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = 150

class WhiteKing(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteKing, self).__init__()
        self.surf = pg.image.load("assets/w_king_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = 200
        self.rect.top = 350

class BlackKing(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackKing, self).__init__()
        self.surf = pg.image.load("assets/b_king_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = 200

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    squares = [Square() for _ in range(32)]
    white_pawns = [WhitePawn(i) for i in range(8)]
    black_pawns = [BlackPawn(i) for i in range(8)]
    white_knights = [WhiteKnight(i) for i in range(2)]
    black_knights = [BlackKnight(i) for i in range(2)]
    white_bishops = [WhiteBishop(i) for i in range(2)]
    black_bishops = [BlackBishop(i) for i in range(2)]
    white_rooks = [WhiteRook(i) for i in range(2)]
    black_rooks = [BlackRook(i) for i in range(2)]
    white_queen = WhiteQueen()
    black_queen = BlackQueen()
    white_king = WhiteKing()
    black_king = BlackKing()
    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
            if event.type == pg.QUIT:
                game_running = False
        x_off = 0
        y_off = 0
        mirror = True
        for i, square in enumerate(squares):
            if i % 4 == 0 and i != 0:
                y_off += 1
                x_off = 0
                mirror = not mirror
            x_off_act = 50 * x_off * 2
            x_off += 1
            square.rect.top = y_off * 50
            square.rect.left = x_off_act if mirror else x_off_act + 50
            screen.blit(square.surf, square.rect)
        for white_pawn in white_pawns:
            screen.blit(white_pawn.surf, white_pawn.rect)
        for black_pawn in black_pawns:
            screen.blit(black_pawn.surf, black_pawn.rect)
        for white_knight in white_knights:
            screen.blit(white_knight.surf, white_knight.rect)
        for black_knight in black_knights:
            screen.blit(black_knight.surf, black_knight.rect)
        for white_bishop in white_bishops:
            screen.blit(white_bishop.surf, white_bishop.rect)
        for black_bishop in black_bishops:
            screen.blit(black_bishop.surf, black_bishop.rect)
        for white_rook in white_rooks:
            screen.blit(white_rook.surf, white_rook.rect)
        for black_rook in black_rooks:
            screen.blit(black_rook.surf, black_rook.rect)
        screen.blit(white_queen.surf, white_queen.rect)
        screen.blit(black_queen.surf, black_queen.rect)
        screen.blit(white_king.surf, white_king.rect)
        screen.blit(black_king.surf, black_king.rect)
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()