from typing import TypedDict

import pygame as pg
from pygame.event import Event
from pygame.locals import MOUSEBUTTONDOWN

IMAGE_SIZE = 57


class Piece(pg.sprite.Sprite):
    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__()
        self.piece = pg.Surface((50, 50))
        self.rect = (
            self.piece.get_rect()
            if not pos
            else self.piece.get_rect(topleft=pos)
        )
        self.board_coordinate = board_coordinate
        self.clicked = False
        self.is_alive = True

    def draw(self, surface: pg.surface.Surface):
        surface.blit(self.piece, self.rect)

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = not self.clicked

    def __repr__(self) -> str:
        return f"{__class__}(piece={self.piece}, rect={self.rect}, board_coordinate={self.board_coordinate}, clicked={self.clicked}, is_alive={self.is_alive})"

    def __str__(self) -> str:
        return f"piece is {self.piece}\nrect is{self.rect}\nboard coordinate is{self.board_coordinate}\nclick is {self.clicked}\nalive is {self.is_alive}"


class Pawn(Piece):
    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.is_first = True


class BlackPawn(Pawn):
    name = "bp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.piece = pg.image.load("img/black_pawn.png").convert_alpha()

    def allowed_move(self, x: int, y: int):
        if self.is_first:
            if (
                self.board_coordinate[1] + 2 == y
                or self.board_coordinate[1] + 1 == y
                and self.board_coordinate[0] == x
            ):
                return True
        else:
            if (
                self.board_coordinate[1] + 1 == y
                and self.board_coordinate[0] == x
            ):
                return True
        return False

    def allowed_take(self, x: int, y: int):
        if (
            self.board_coordinate[0] + 1 == y
            and self.board_coordinate[0] + 1 == x
            or self.board_coordinate[0] - 1 == x
        ):
            return True
        return False


class WhitePawn(Pawn):
    name = "wp"

    def __init__(
        self, pos: tuple[int, int], board_coordinate: tuple[int, int]
    ) -> None:
        super().__init__(pos, board_coordinate)
        self.piece = pg.image.load("img/white_pawn.png").convert_alpha()

    def allowed_move(self, x: int, y: int):
        if self.is_first:
            if (
                self.board_coordinate[1] - 2 == y
                or self.board_coordinate[1] - 1 == y
                and self.board_coordinate[0] == x
            ):
                return True
        else:
            if (
                self.board_coordinate[1] - 1 == y
                and self.board_coordinate[0] == x
            ):
                return True
        return False

    def allowed_take(self, x: int, y: int):
        if (
            self.board_coordinate[0] + 1 == y
            and self.board_coordinate[0] + 1 == x
            or self.board_coordinate[0] - 1 == x
        ):
            return True
        return False


class Move(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: None


class Take(TypedDict):
    updated_pos: tuple[int, int]
    is_taking: bool
    taken_piece: WhitePawn | BlackPawn


class ChessBoard(pg.sprite.Sprite):
    global IMAGE_SIZE

    def __init__(self, screen: pg.surface.Surface) -> None:
        super().__init__()
        # // moving and taking buggy at best

        self.screen = screen
        white_square = pg.image.load(
            "img/chess_board/white_square.png"
        ).convert_alpha()
        black_square = pg.image.load(
            "img/chess_board/black_square.png"
        ).convert_alpha()

        self.board = [
            [
                white_square if col % 2 == 0 else black_square
                for col in range(8)
            ]
            if row % 2 == 0
            else [
                black_square if col % 2 == 0 else white_square
                for col in range(8)
            ]
            for row in range(8)
        ]

        self.board_rect = [
            [
                col.get_rect(topleft=(coli * IMAGE_SIZE, rowi * IMAGE_SIZE))
                for coli, col in enumerate(row)
            ]
            for rowi, row in enumerate(self.board)
        ]

        self.black_pawns = [
            BlackPawn((index * IMAGE_SIZE, IMAGE_SIZE), (index, 1))
            for index in range(8)
        ]

        self.white_pawns = [
            WhitePawn((index * IMAGE_SIZE, IMAGE_SIZE * 6), (index, 6))
            for index in range(8)
        ]

        self.board_repr: list[list[str | None]] = []
        for rowi in range(8):
            row = []
            for _ in range(8):
                if rowi == 1:
                    row.append(BlackPawn.name)
                elif rowi == 6:
                    row.append(WhitePawn.name)
                else:
                    row.append(None)
            self.board_repr.append(row)

    def draw(self):
        for board, board_rect in zip(self.board, self.board_rect):
            for square, square_rect in zip(board, board_rect):
                self.screen.blit(square, square_rect)

    def draw_black_pawns(self):
        for black_pawn in self.black_pawns:
            self.screen.blit(black_pawn.piece, black_pawn.rect)

    def draw_white_pawns(self):
        for white_pawn in self.white_pawns:
            self.screen.blit(white_pawn.piece, white_pawn.rect)

    def is_moving(self, new_pos: tuple[int, int]) -> bool:
        if not self.board_repr[new_pos[1]][new_pos[0]]:
            return True
        return False

    def square_pos(self) -> tuple[int, int] | None:
        for rowi, row in enumerate(self.board_rect):
            for coli, col in enumerate(row):
                if col.collidepoint(pg.mouse.get_pos()):
                    return (coli, rowi)

    def captured_piece(self):
        for black_pawn, white_pawn in zip(self.black_pawns, self.white_pawns):
            if black_pawn.rect.collidepoint(pg.mouse.get_pos()):
                return black_pawn
            if white_pawn.rect.collidepoint(pg.mouse.get_pos()):
                return white_pawn

    def active_piece(self):
        for black_pawn, white_pawn in zip(self.black_pawns, self.white_pawns):
            if black_pawn.clicked:
                return black_pawn
            if white_pawn.clicked:
                return white_pawn

    def move(
        self, new_pos: tuple[int, int], piece: WhitePawn | BlackPawn
    ) -> Move:
        if piece.is_first:
            piece.is_first = False
        self.board_repr[piece.board_coordinate[1]][
            piece.board_coordinate[0]
        ] = None
        self.board_repr[new_pos[1]][new_pos[0]] = piece.name
        piece.board_coordinate = new_pos
        return {
            "updated_pos": (new_pos[0] * IMAGE_SIZE, new_pos[1] * IMAGE_SIZE),
            "is_taking": False,
            "taken_piece": None,
        }

    def take(
        self,
        piece: WhitePawn | BlackPawn,
        taken_piece: WhitePawn | BlackPawn,
    ) -> Take:
        if piece.is_first:
            piece.is_first = False
        self.board_repr[piece.board_coordinate[1]][
            piece.board_coordinate[0]
        ] = None
        self.board_repr[taken_piece.board_coordinate[0]][
            taken_piece.board_coordinate[1]
        ] = piece.name
        piece.board_coordinate = taken_piece.board_coordinate
        return {
            "updated_pos": (taken_piece.rect.left, taken_piece.rect.top),
            "is_taking": True,
            "taken_piece": taken_piece,
        }

    def update_piece(
        self,
        new_pos: tuple[int, int],
        piece: BlackPawn | WhitePawn,
        is_taking: bool,
        taken_piece: WhitePawn | BlackPawn | None = None,
    ):
        if is_taking:
            if taken_piece is None:
                return
            taken_piece.piece.fill((0, 0, 0, 0))
        piece.rect.left, piece.rect.top = new_pos

    def update(self, event_list: list[Event]):
        for event in event_list:
            if event.type == MOUSEBUTTONDOWN:
                clicked_piece = self.active_piece()
                clicked_square = self.square_pos()
                print(clicked_piece)
                if clicked_piece is None:
                    return
                print(clicked_square)
                if clicked_square is None:
                    return

                print(self.is_moving(clicked_square))
                if self.is_moving(clicked_square):
                    print(
                        not clicked_piece.allowed_move(
                            clicked_square[0], clicked_square[1]
                        )
                    )
                    if not clicked_piece.allowed_move(
                        clicked_square[0], clicked_square[1]
                    ):
                        return
                    updated_pos = self.move(clicked_square, clicked_piece)
                    print(updated_pos)
                else:
                    print(
                        not clicked_piece.allowed_take(
                            clicked_square[0], clicked_square[1]
                        )
                    )
                    if not clicked_piece.allowed_take(
                        clicked_square[0], clicked_square[1]
                    ):
                        return
                    taken_piece = self.captured_piece()
                    print(taken_piece)
                    if taken_piece is None:
                        return
                    updated_pos = self.take(clicked_piece, taken_piece)
                    print(updated_pos)
                self.update_piece(
                    updated_pos["updated_pos"],
                    clicked_piece,
                    updated_pos["is_taking"],
                    taken_piece=updated_pos["taken_piece"],
                )
                clicked_piece.clicked = not clicked_piece.clicked
                print(clicked_piece)
