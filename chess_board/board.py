from typing import Optional

from .base import BaseGroup, BaseSprite
from .types import IMAGE_SIZE


class Square(BaseSprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int],
        pos: tuple[int, int],
    ) -> None:
        super().__init__(img_path, board_coordinate, pos)


class Board(BaseGroup):
    def __init__(self):
        super().__init__(
            [
                [
                    Square(
                        "img/chess_board/white_square.png",
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                        (col, row),
                    )
                    if col % 2 == 0
                    else Square(
                        "img/chess_board/black_square.png",
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                        (col, row),
                    )
                    for col in range(8)
                ]
                if row % 2 == 0
                else [
                    Square(
                        "img/chess_board/black_square.png",
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                        (col, row),
                    )
                    if col % 2 == 0
                    else Square(
                        "img/chess_board/white_square.png",
                        (col * IMAGE_SIZE, row * IMAGE_SIZE),
                        (col, row),
                    )
                    for col in range(8)
                ]
                for row in range(8)
            ]
        )

        self.board_repr = [["" for _ in range(8)] for _ in range(8)]

    def sprites(self) -> list[Square]:
        return super().sprites()

    def get_clicked_square(self, pos: tuple[int, int]) -> Optional[Square]:
        for square in self.sprites():
            if square.rect.collidepoint(pos):
                return square
        return None
