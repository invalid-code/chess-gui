from typing import Optional

import pygame as pg

from chess_board.constants import IMAGE_SIZE, PieceType


class Piece(pg.sprite.Sprite):
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

    def set_board_repr(self, board: list[list[str]], name: str):
        x, y = self.board_coordinate
        board[y][x] = name

    def __repr__(self) -> str:
        return f"Piece(piece={self.image}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.image}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"


class Pieces(pg.sprite.Group):
    def sprites(self) -> list[PieceType]:
        return super().sprites()

    def start_board_repr(self, board: list[list[str]]):
        for piece in self.sprites():
            piece.set_board_repr(board, piece.name)

    def is_clicked(self, pos: tuple[int, int]) -> Optional[PieceType]:
        for piece in self.sprites():
            if piece.rect.collidepoint(pos):
                return piece
        return None
