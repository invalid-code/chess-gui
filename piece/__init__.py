import pygame as pg
from pygame.sprite import Sprite

from chess_board.constants import IMAGE_SIZE


class Piece(Sprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int] = (0, 0),
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        super().__init__()
        self.image = pg.image.load(img_path)
        self.transform_scale((IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.board_coordinate = board_coordinate
        self.clicked = False
        self.is_alive = True

    def transform_scale(self, scale: tuple[int, int]):
        self.image = pg.transform.scale(self.image, scale)

    def __repr__(self) -> str:
        return f"Piece(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"
