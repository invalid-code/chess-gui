import pygame as pg

from .constants import IMAGE_SIZE


class Square(pg.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        square: pg.Surface,
    ) -> None:
        super().__init__()
        self.image = square
        self.rect = self.image.get_rect(topleft=pos)


class WhiteSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        white_square = pg.image.load(
            "img/chess_board/white_square.png"
        ).convert_alpha()
        super().__init__(pos, white_square)


class BlackSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        black_square = pg.image.load(
            "img/chess_board/black_square.png"
        ).convert_alpha()
        super().__init__(pos, black_square)


class Board(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [
                [
                    WhiteSquare((col * IMAGE_SIZE, row * IMAGE_SIZE))
                    if col % 2 == 0
                    else BlackSquare((col * IMAGE_SIZE, row * IMAGE_SIZE))
                    for col in range(8)
                ]
                if row % 2 == 0
                else [
                    BlackSquare((col * IMAGE_SIZE, row * IMAGE_SIZE))
                    if col % 2 == 0
                    else WhiteSquare((col * IMAGE_SIZE, row * IMAGE_SIZE))
                    for col in range(8)
                ]
                for row in range(8)
            ]
        )
