import pygame as pg

from .constants import IMAGE_SIZE


class Square(pg.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        square: pg.Surface,
        board_coordinate: tuple[int, int],
    ) -> None:
        super().__init__()
        self.image = square
        self.rect = self.image.get_rect(topleft=pos)
        self.board_coordinate = board_coordinate


class WhiteSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
        board_coordinate: tuple[int, int] = (0, 0),
    ) -> None:
        white_square = pg.image.load(
            "img/chess_board/white_square.png"
        ).convert_alpha()
        super().__init__(pos, white_square, board_coordinate)


class BlackSquare(Square):
    def __init__(
        self,
        pos: tuple[int, int] = (0, 0),
        board_coordinate: tuple[int, int] = (0, 0),
    ) -> None:
        black_square = pg.image.load(
            "img/chess_board/black_square.png"
        ).convert_alpha()
        super().__init__(pos, black_square, board_coordinate)


class Board(pg.sprite.Group):
    def __init__(self):
        super().__init__(
            [
                [
                    WhiteSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    if col % 2 == 0
                    else BlackSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    for col in range(8)
                ]
                if row % 2 == 0
                else [
                    BlackSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    if col % 2 == 0
                    else WhiteSquare(
                        (col * IMAGE_SIZE, row * IMAGE_SIZE), (col, row)
                    )
                    for col in range(8)
                ]
                for row in range(8)
            ]
        )

        self.board_repr = [["" for _ in range(8)] for _ in range(8)]

    def start_board_repr(self, pieces: Pieces):
        pass
