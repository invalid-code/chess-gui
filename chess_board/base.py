import pygame as pg

from chess_board.types import IMAGE_SIZE


class BaseGroup(pg.sprite.Group):
    pass


class BaseSprite(pg.sprite.Sprite):
    def __init__(
        self,
        img_path: str,
        board_coordinate: tuple[int, int],
        dest: tuple[int, int],
    ) -> None:
        super().__init__()
        self.image = pg.image.load(img_path)
        self.transform_scale((IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.image.get_rect(topleft=dest)
        self.board_coordinate = board_coordinate

    def transform_scale(self, scale: tuple[int, int]):
        self.image = pg.transform.scale(self.image, scale)
