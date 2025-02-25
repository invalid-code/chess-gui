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
    def __init__(self) -> None:
        super(WhitePawn, self).__init__()
        self.surf = pg.image.load("assets/w_pawn_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackPawn(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackPawn, self).__init__()
        self.surf = pg.image.load("assets/b_pawn_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class WhiteKnight(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteKnight, self).__init__()
        self.surf = pg.image.load("assets/w_knight_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackKnight(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackKnight, self).__init__()
        self.surf = pg.image.load("assets/b_knight_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class WhiteBishop(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteBishop, self).__init__()
        self.surf = pg.image.load("assets/w_bishop_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackBishop(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackBishop, self).__init__()
        self.surf = pg.image.load("assets/b_bishop_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class WhiteRook(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteRook, self).__init__()
        self.surf = pg.image.load("assets/w_rook_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackRook(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackRook, self).__init__()
        self.surf = pg.image.load("assets/b_rook_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class WhiteQueen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteQueen, self).__init__()
        self.surf = pg.image.load("assets/w_queen_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackQueen(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackQueen, self).__init__()
        self.surf = pg.image.load("assets/b_queen_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class WhiteKing(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(WhiteKing, self).__init__()
        self.surf = pg.image.load("assets/w_king_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

class BlackKing(pg.sprite.Sprite):
    def __init__(self) -> None:
        super(BlackKing, self).__init__()
        self.surf = pg.image.load("assets/b_king_png_128px.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    squares = [Square() for _ in range(32)]
    white_pawns = [WhitePawn() for _ in range(8)]
    black_pawns = [BlackPawn() for _ in range(8)]
    white_knights = [WhiteKnight() for _ in range(2)]
    black_knights = [BlackKnight() for _ in range(2)]
    white_bishops = [WhiteBishop() for _ in range(2)]
    black_bishops = [BlackBishop() for _ in range(2)]
    white_rooks = [WhiteRook() for _ in range(2)]
    black_rooks = [BlackRook() for _ in range(2)]
    white_queen = WhiteQueen()
    black_queen = BlackQueen()
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
            if i % 4 == 0:
                y_off += 1
                x_off = 0
                mirror = not mirror
            # print(x_off)
            if mirror:
                screen.blit(square.surf, (50 * (x_off * 2), y_off * 50))
            else:
                screen.blit(square.surf, ((50 * (x_off * 2)) + 50, y_off * 50))
            x_off += 1
        # break
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
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()