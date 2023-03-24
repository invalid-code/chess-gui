import pygame as pg
from pygame.sprite import Sprite


class Piece(Sprite):
    def __init__(
        self,
        board_coordinate: tuple[int, int] = (0, 0),
        pos: tuple[int, int] = (0, 0),
    ) -> None:
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect(topleft=pos)
        self.board_coordinate = board_coordinate
        self.clicked = False
        self.is_alive = True

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.image, self.rect)

    def __repr__(self) -> str:
        return f"Piece(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"
