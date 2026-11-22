from typing import Any

import pygame as pg
from pygame.event import Event

WIDTH, HEIGHT = (900, 600)


class Square(pg.sprite.Sprite):
    def __init__(
        self,
        *groups: pg.sprite.AbstractGroup[Any],
        fill: tuple[int, int, int] = (0, 0, 0),
        rank: int = 1,
        file: int = 1,
    ) -> None:
        super().__init__(*groups)
        self.image = pg.Surface((50, 50))
        self.image.fill(fill)
        self.rect = self.image.get_rect()
        self.rect.left = (file - 1) * 50
        self.rect.top = (rank - 1) * 50
        self.file = file
        self.rank = 9 - rank


class Squares(pg.sprite.Group[Square]):
    def __init__(self) -> None:
        super().__init__()
        for rank in range(1, 9):
            for file in range(1, 9):
                if rank % 2 == 0:
                    if file % 2 == 0:
                        self.add(
                            Square(self, fill=(255, 255, 255), file=file, rank=rank)
                        )
                    else:
                        self.add(Square(self, fill=(0, 0, 0), file=file, rank=rank))
                else:
                    if file % 2 == 0:
                        self.add(Square(self, fill=(0, 0, 0), file=file, rank=rank))
                    else:
                        self.add(
                            Square(self, fill=(255, 255, 255), file=file, rank=rank)
                        )


class Pawn(pg.sprite.Sprite):
    def __init__(
        self,
        *groups: pg.sprite.AbstractGroup[Any],
        image_file: str = "",
        file: int = 1,
        rank: int = 1,
    ) -> None:
        super().__init__(*groups)
        self.file = file
        self.rank = rank
        self.first_move = True
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        return (
            (self.first_move and move_rank == self.rank + 2)
            or move_rank == self.rank + 1
        ) and move_file == self.file

    def move(self, move_file: int, move_rank: int) -> None:
        if self.first_move:
            self.first_move = False
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return move_rank == self.rank + 1 and (
            move_file - 1 == self.file or move_file + 1 == self.file
        )


class Knight(pg.sprite.Sprite):
    def __init__(
        self,
        *groups: pg.sprite.AbstractGroup[Any],
        image_file: str = "",
        file: int = 1,
        rank: int = 1,
    ) -> None:
        super().__init__(*groups)
        self.file = file
        self.rank = rank
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        return (
            (
                move_rank == self.rank + 2
                and (move_file == self.file + 1 or move_file == self.file - 1)
            )
            or (
                move_rank == self.rank - 2
                and (move_file == self.file + 1 or move_file == self.file - 1)
            )
            or (
                move_file == self.file + 2
                and (move_rank == self.rank + 1 or move_rank == self.rank - 1)
            )
            or (
                move_file == self.file - 2
                and (move_rank == self.rank + 1 or move_rank == self.rank - 1)
            )
        )

    def move(self, move_file: int, move_rank: int) -> None:
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return self.allowed_move(move_file, move_rank)


class Bishop(pg.sprite.Sprite):
    def __init__(
        self,
        *groups: pg.sprite.AbstractGroup[Any],
        image_file: str = "",
        file: int = 1,
        rank: int = 1,
    ) -> None:
        super().__init__(*groups)
        self.file = file
        self.rank = rank
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        if move_file > self.file:
            if move_rank > self.rank:
                return move_file - self.file == move_rank - self.rank
            else:
                return move_file - self.file == self.rank - move_rank
        else:
            if move_rank > self.rank:
                return self.file - move_file == move_rank - self.rank
            else:
                return self.file - move_file == self.rank - move_rank

    def move(self, move_file: int, move_rank: int) -> None:
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return self.allowed_move(move_file, move_rank)


class Rook(pg.sprite.Sprite):
    def __init__(
        self,
        *groups: pg.sprite.AbstractGroup[Any],
        image_file: str = "",
        file: int = 1,
        rank: int = 1,
    ) -> None:
        super().__init__(*groups)
        self.file = file
        self.rank = rank
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        return move_file == self.file or move_rank == self.rank

    def move(self, move_file: int, move_rank: int) -> None:
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return self.allowed_move(move_file, move_rank)


class Queen(Rook, Bishop):
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        self.file = file
        self.rank = rank
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50
        self.is_taken = False

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        return Rook.allowed_move(self, move_file, move_rank) or Bishop.allowed_move(
            self, move_file, move_rank
        )

    def move(self, move_file: int, move_rank: int) -> None:
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return self.allowed_move(move_file, move_rank)


class King(Rook, Bishop):
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        self.file = file
        self.rank = rank
        self.image = pg.image.load(image_file).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_move(self, move_file: int, move_rank: int) -> bool:
        return (
            abs(move_file - self.file) <= 1 and abs(move_rank - self.rank) <= 1
        ) and (
            Rook.allowed_move(self, move_file, move_rank)
            or Bishop.allowed_move(self, move_file, move_rank)
        )

    def move(self, move_file: int, move_rank: int) -> None:
        self.file = move_file
        self.rank = move_rank
        self.rect.left = (self.file - 1) * 50
        self.rect.top = (8 - self.rank) * 50

    def allowed_take(self, move_file: int, move_rank: int) -> bool:
        return self.allowed_move(move_file, move_rank)


class WhitePawns(pg.sprite.Group[Pawn]):
    def __init__(self) -> None:
        super().__init__()
        for file in range(1, 9):
            self.add(
                Pawn(self, image_file="assets/w_pawn_png_128px.png", file=file, rank=2)
            )


class WhiteKnights(pg.sprite.Group[Knight]):
    def __init__(self) -> None:
        super().__init__()
        for file in [2, 7]:
            self.add(
                Knight(
                    self, image_file="assets/w_knight_png_128px.png", file=file, rank=1
                )
            )


class WhiteBishops(pg.sprite.Group[Bishop]):
    def __init__(self) -> None:
        super().__init__()
        for file in [3, 6]:
            self.add(
                Bishop(
                    self, image_file="assets/w_bishop_png_128px.png", file=file, rank=1
                )
            )


class WhiteRooks(pg.sprite.Group[Rook]):
    def __init__(self) -> None:
        super().__init__()
        for file in [1, 8]:
            self.add(
                Rook(self, image_file="assets/w_rook_png_128px.png", file=file, rank=1)
            )


class BlackPawns(pg.sprite.Group[Pawn]):
    def __init__(self) -> None:
        super().__init__()
        for file in range(1, 9):
            self.add(
                Pawn(self, image_file="assets/b_pawn_png_128px.png", file=file, rank=7)
            )


class BlackKnights(pg.sprite.Group[Knight]):
    def __init__(self) -> None:
        super().__init__()
        for file in [2, 7]:
            self.add(
                Knight(
                    self, image_file="assets/b_knight_png_128px.png", file=file, rank=8
                )
            )


class BlackBishops(pg.sprite.Group[Bishop]):
    def __init__(self) -> None:
        super().__init__()
        for file in [3, 6]:
            self.add(
                Bishop(
                    self, image_file="assets/b_bishop_png_128px.png", file=file, rank=8
                )
            )


class BlackRooks(pg.sprite.Group[Rook]):
    def __init__(self) -> None:
        super().__init__()
        for file in [1, 8]:
            self.add(
                Rook(self, image_file="assets/b_rook_png_128px.png", file=file, rank=8)
            )


Piece = Pawn | Knight | Bishop | Rook | Queen | King
TakeablePiece = Pawn | Knight | Bishop | Rook | Queen
TakeablePieceGroup = BlackPawns | BlackKnights | BlackBishops | BlackRooks


def check_horizontal(
    selected_piece: Rook | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    if selected_piece.file < move_file:
        # going right
        for white_pawn in white_pawns:
            if white_pawn.rank == move_rank and (
                white_pawn.file < move_file and selected_piece.file < white_pawn.file
            ):
                is_moving_blocked = True
                break
        for white_knight in white_knights:
            if white_knight.rank == move_rank and (
                white_knight.file < move_file
                and selected_piece.file < white_knight.file
            ):
                is_moving_blocked = True
                break
        for white_bishop in white_bishops:
            if white_bishop.rank == move_rank and (
                white_bishop.file < move_file
                and selected_piece.file < white_bishop.file
            ):
                is_moving_blocked = True
                break
        for white_rook in white_rooks:
            if selected_piece == white_rook:
                continue
            if white_rook.rank == move_rank and (
                white_rook.file < move_file and selected_piece.file < white_rook.file
            ):
                is_moving_blocked = True
                break
        if white_queen.rank == move_rank and (
            white_queen.file < move_file and selected_piece.file < white_queen.file
        ):
            is_moving_blocked = True
        if white_king.rank == move_rank and (
            white_king.file < move_file and selected_piece.file < white_king.file
        ):
            is_moving_blocked = True
    else:
        # going left
        for white_pawn in white_pawns:
            if white_pawn.rank == move_rank and (
                white_pawn.file > move_file and selected_piece.file > white_pawn.file
            ):
                is_moving_blocked = True
                break
        for white_knight in white_knights:
            if white_knight.rank == move_rank and (
                white_knight.file > move_file
                and selected_piece.file > white_knight.file
            ):
                is_moving_blocked = True
                break
        for white_bishop in white_bishops:
            if white_bishop.rank == move_rank and (
                white_bishop.file > move_file
                and selected_piece.file > white_bishop.file
            ):
                is_moving_blocked = True
                break
        for white_rook in white_rooks:
            if selected_piece == white_rook:
                continue
            if white_rook.rank == move_rank and (
                white_rook.file > move_file and selected_piece.file > white_rook.file
            ):
                is_moving_blocked = True
                break
        if white_queen.rank == move_rank and (
            white_queen.file > move_file and selected_piece.file > white_queen.file
        ):
            is_moving_blocked = True
        if white_king.rank == move_rank and (
            white_king.file > move_file and selected_piece.file > white_king.file
        ):
            is_moving_blocked = True
    return is_moving_blocked


def check_vertical(
    selected_piece: Rook | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    if selected_piece.rank < move_rank:
        # going up
        for white_pawn in white_pawns:
            if white_pawn.file == move_file and (
                white_pawn.rank < move_rank and selected_piece.rank < white_pawn.rank
            ):
                is_moving_blocked = True
                break
        for white_knight in white_knights:
            if white_knight.file == move_file and (
                white_knight.rank < move_rank
                and selected_piece.rank < white_knight.rank
            ):
                is_moving_blocked = True
                break
        for white_bishop in white_bishops:
            if white_bishop.file == move_file and (
                white_bishop.rank < move_rank
                and selected_piece.rank < white_bishop.rank
            ):
                is_moving_blocked = True
                break
        for white_rook in white_rooks:
            if selected_piece == white_rook:
                continue
            if white_rook.file == move_file and (
                white_rook.rank < move_rank and selected_piece.rank < white_rook.rank
            ):
                is_moving_blocked = True
                break
        if white_queen.file == move_file and (
            white_queen.rank < move_rank and selected_piece.rank < white_queen.rank
        ):
            is_moving_blocked = True
        if white_king.file == move_file and (
            white_king.rank < move_rank and selected_piece.rank < white_king.rank
        ):
            is_moving_blocked = True
    else:
        # going down
        for white_pawn in white_pawns:
            if white_pawn.file == move_file and (
                white_pawn.rank > move_rank and selected_piece.rank > white_pawn.rank
            ):
                is_moving_blocked = True
                break
        for white_knight in white_knights:
            if white_knight.file == move_file and (
                white_knight.rank > move_rank
                and selected_piece.rank > white_knight.rank
            ):
                is_moving_blocked = True
                break
        for white_bishop in white_bishops:
            if white_bishop.file == move_file and (
                white_bishop.rank > move_rank
                and selected_piece.rank > white_bishop.rank
            ):
                is_moving_blocked = True
                break
        for white_rook in white_rooks:
            if selected_piece == white_rook:
                continue
            if white_rook.file == move_file and (
                white_rook.rank > move_rank and selected_piece.rank > white_rook.rank
            ):
                is_moving_blocked = True
                break
        if white_queen.file == move_file and (
            white_queen.rank > move_rank and selected_piece.rank > white_queen.rank
        ):
            is_moving_blocked = True
        if white_king.file == move_file and (
            white_king.rank > move_rank and selected_piece.rank > white_king.rank
        ):
            is_moving_blocked = True
    return is_moving_blocked


def check_lower_left(
    selected_piece: Bishop | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    for white_pawn in white_pawns:
        if (white_pawn.rank < move_rank and white_pawn.file > move_file) and (
            selected_piece.rank < white_pawn.rank
            and selected_piece.file > white_pawn.file
        ):
            is_moving_blocked = True
            break
    for white_knight in white_knights:
        if (white_knight.rank < move_rank and white_knight.file > move_file) and (
            selected_piece.rank < white_knight.rank
            and selected_piece.file > white_knight.file
        ):
            is_moving_blocked = True
            break
    for white_bishop in white_bishops:
        if selected_piece == white_bishop:
            continue
        if (white_bishop.rank < move_rank and white_bishop.file > move_file) and (
            selected_piece.rank < white_bishop.rank
            and selected_piece.file > white_bishop.file
        ):
            is_moving_blocked = True
            break
    for white_rook in white_rooks:
        if (white_rook.rank < move_rank and white_rook.file > move_file) and (
            selected_piece.rank < white_rook.rank
            and selected_piece.file > white_rook.file
        ):
            is_moving_blocked = True
            break
    if (white_queen.rank < move_rank and white_queen.file > move_file) and (
        selected_piece.rank < white_queen.rank
        and selected_piece.file > white_queen.file
    ):
        is_moving_blocked = True
    if (white_king.rank < move_rank and white_king.file > move_file) and (
        selected_piece.rank < white_king.rank and selected_piece.file > white_king.file
    ):
        is_moving_blocked = True
    return is_moving_blocked


def check_upper_left(
    selected_piece: Bishop | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    for white_pawn in white_pawns:
        if (white_pawn.rank > move_rank and white_pawn.file < move_file) and (
            selected_piece.rank > white_pawn.rank
            and selected_piece.file < white_pawn.file
        ):
            is_moving_blocked = True
            break
    for white_knight in white_knights:
        if (white_knight.rank > move_rank and white_knight.file < move_file) and (
            selected_piece.rank > white_knight.rank
            and selected_piece.file < white_knight.file
        ):
            is_moving_blocked = True
            break
    for white_bishop in white_bishops:
        if selected_piece == white_bishop:
            continue
        if (white_bishop.rank > move_rank and white_bishop.file < move_file) and (
            selected_piece.rank > white_bishop.rank
            and selected_piece.file < white_bishop.file
        ):
            is_moving_blocked = True
            break
    for white_rook in white_rooks:
        if (white_rook.rank > move_rank and white_rook.file < move_file) and (
            selected_piece.rank > white_rook.rank
            and selected_piece.file < white_rook.file
        ):
            is_moving_blocked = True
            break
    if (white_queen.rank > move_rank and white_queen.file < move_file) and (
        selected_piece.rank > white_queen.rank
        and selected_piece.file < white_queen.file
    ):
        is_moving_blocked = True
    if (white_king.rank > move_rank and white_king.file < move_file) and (
        selected_piece.rank > white_king.rank and selected_piece.file < white_king.file
    ):
        is_moving_blocked = True
    return is_moving_blocked


def check_lower_right(
    selected_piece: Bishop | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    for white_pawn in white_pawns:
        if (white_pawn.rank > move_rank and white_pawn.file > move_file) and (
            selected_piece.rank > white_pawn.rank
            and selected_piece.file > white_pawn.file
        ):
            is_moving_blocked = True
            break
    for white_knight in white_knights:
        if (white_knight.rank > move_rank and white_knight.file > move_file) and (
            selected_piece.rank > white_knight.rank
            and selected_piece.file > white_knight.file
        ):
            is_moving_blocked = True
            break
    for white_bishop in white_bishops:
        if selected_piece == white_bishop:
            continue
        if (white_bishop.rank > move_rank and white_bishop.file > move_file) and (
            selected_piece.rank > white_bishop.rank
            and selected_piece.file > white_bishop.file
        ):
            is_moving_blocked = True
            break
    for white_rook in white_rooks:
        if (white_rook.rank > move_rank and white_rook.file > move_file) and (
            selected_piece.rank > white_rook.rank
            and selected_piece.file > white_rook.file
        ):
            is_moving_blocked = True
            break
    if (white_queen.rank > move_rank and white_queen.file > move_file) and (
        selected_piece.rank > white_queen.rank
        and selected_piece.file > white_queen.file
    ):
        is_moving_blocked = True
    if (white_king.rank > move_rank and white_king.file > move_file) and (
        selected_piece.rank > white_king.rank and selected_piece.file > white_king.file
    ):
        is_moving_blocked = True
    return is_moving_blocked


def check_upper_right(
    selected_piece: Bishop | Queen,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
    move_rank: int,
):
    is_moving_blocked = False
    for white_pawn in white_pawns:
        if (white_pawn.rank < move_rank and white_pawn.file < move_file) and (
            selected_piece.rank < white_pawn.rank
            and selected_piece.file < white_pawn.file
        ):
            is_moving_blocked = True
            break
    for white_knight in white_knights:
        if (white_knight.rank < move_rank and white_knight.file < move_file) and (
            selected_piece.rank < white_knight.rank
            and selected_piece.file < white_knight.file
        ):
            is_moving_blocked = True
            break
    for white_bishop in white_bishops:
        if selected_piece == white_bishop:
            continue
        if (white_bishop.rank < move_rank and white_bishop.file < move_file) and (
            selected_piece.rank < white_bishop.rank
            and selected_piece.file < white_bishop.file
        ):
            is_moving_blocked = True
            break
    for white_rook in white_rooks:
        if (white_rook.rank < move_rank and white_rook.file < move_file) and (
            selected_piece.rank < white_rook.rank
            and selected_piece.file < white_rook.file
        ):
            is_moving_blocked = True
            break
    if (white_queen.rank < move_rank and white_queen.file < move_file) and (
        selected_piece.rank < white_queen.rank
        and selected_piece.file < white_queen.file
    ):
        is_moving_blocked = True
    if (white_king.rank < move_rank and white_king.file < move_file) and (
        selected_piece.rank < white_king.rank and selected_piece.file < white_king.file
    ):
        is_moving_blocked = True
    return is_moving_blocked


def select_piece(
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    event: Event,
) -> Piece | None:
    selected_piece = None
    for white_pawn in white_pawns:
        if white_pawn.rect.collidepoint(event.pos):
            selected_piece = white_pawn
            break
    for white_knight in white_knights:
        if white_knight.rect.collidepoint(event.pos):
            selected_piece = white_knight
            break
    for white_bishop in white_bishops:
        if white_bishop.rect.collidepoint(event.pos):
            selected_piece = white_bishop
            break
    for white_rook in white_rooks:
        if white_rook.rect.collidepoint(event.pos):
            selected_piece = white_rook
            break
    if white_queen.rect.collidepoint(event.pos):
        selected_piece = white_queen
    if white_king.rect.collidepoint(event.pos):
        selected_piece = white_king
    return selected_piece


def check_is_check(
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    black_king: King,
) -> bool:
    is_check = False
    for white_pawn in white_pawns:
        if white_pawn.allowed_take(black_king.file, black_king.rank):
            is_check = True
            break
    for white_knight in white_knights:
        if white_knight.allowed_take(black_king.file, black_king.rank):
            is_check = True
            break
    for white_bishop in white_bishops:
        if white_bishop.allowed_take(black_king.file, black_king.rank):
            is_check = True
            break
    for white_rook in white_rooks:
        if white_rook.allowed_take(black_king.file, black_king.rank):
            is_check = True
            break
    if white_queen.allowed_take(black_king.file, black_king.rank):
        is_check = True
    return is_check


def check_pawn_blocked(
    selected_piece: Piece,
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    move_file: int,
):
    is_moving_blocked = False
    for white_pawn in white_pawns:
        if selected_piece == white_pawn:
            continue
        if white_pawn.file == move_file or white_pawn.rank > selected_piece.rank:
            is_moving_blocked = True
            break
    for white_knight in white_knights:
        if white_knight.file == move_file and white_knight.rank > selected_piece.rank:
            is_moving_blocked = True
            break
    for white_bishop in white_bishops:
        if white_bishop.file == move_file and white_bishop.rank > selected_piece.rank:
            is_moving_blocked = True
            break
    for white_rook in white_rooks:
        if white_rook.file == move_file and white_rook.rank > selected_piece.rank:
            is_moving_blocked = True
            break
    if white_queen.file == move_file and white_queen.rank > selected_piece.rank:
        is_moving_blocked = True
    if white_king.file == move_file and white_king.rank > selected_piece.rank:
        is_moving_blocked = True
    return is_moving_blocked


def check_moving_occupied(
    white_pawns: WhitePawns,
    white_knights: WhiteKnights,
    white_bishops: WhiteBishops,
    white_rooks: WhiteRooks,
    white_queen: Queen,
    white_king: King,
    event: Event,
):
    is_moving_occupied = False
    for white_pawn in white_pawns:
        if white_pawn.rect.collidepoint(event.pos):
            is_moving_occupied = True
            break
    for white_knight in white_knights:
        if white_knight.rect.collidepoint(event.pos):
            is_moving_occupied = True
            break
    for white_bishop in white_bishops:
        if white_bishop.rect.collidepoint(event.pos):
            is_moving_occupied = True
            break
    for white_rook in white_rooks:
        if white_rook.rect.collidepoint(event.pos):
            is_moving_occupied = True
            break
    if white_queen.rect.collidepoint(event.pos):
        is_moving_occupied = True
    if white_king.rect.collidepoint(event.pos):
        is_moving_occupied = True
    return is_moving_occupied


def check_taken(
    black_pawns: BlackPawns,
    black_knights: BlackKnights,
    black_bishops: BlackBishops,
    black_rooks: BlackRooks,
    black_queen: Queen,
    move_file: int,
    move_rank: int,
) -> tuple[bool, TakeablePiece | None, TakeablePieceGroup | None]:
    is_taking = False
    taken_piece: TakeablePiece | None = None
    taken_piece_group: TakeablePieceGroup | None = None
    for black_pawn in black_pawns:
        if black_pawn.file == move_file and black_pawn.rank == move_rank:
            taken_piece = black_pawn
            taken_piece_group = black_pawns
            is_taking = True
    for black_knight in black_knights:
        if black_knight.file == move_file and black_knight.rank == move_rank:
            taken_piece = black_knight
            taken_piece_group = black_knights
            is_taking = True
    for black_bishop in black_bishops:
        if black_bishop.file == move_file and black_bishop.rank == move_rank:
            taken_piece = black_bishop
            taken_piece_group = black_bishops
            is_taking = True
    for black_rook in black_rooks:
        if black_rook.file == move_file and black_rook.rank == move_rank:
            taken_piece = black_rook
            taken_piece_group = black_rooks
            is_taking = True
    if black_queen.file == move_file and black_queen.rank == move_rank:
        taken_piece = black_queen
        is_taking = True
    return is_taking, taken_piece, taken_piece_group


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    selected_piece: None | Piece = None
    squares = Squares()
    white_pawns = WhitePawns()
    white_knights = WhiteKnights()
    white_bishops = WhiteBishops()
    white_rooks = WhiteRooks()
    white_queen = Queen("assets/w_queen_png_128px.png", 4, 1)
    white_king = King("assets/w_king_png_128px.png", 5, 1)
    black_pawns = BlackPawns()
    black_knights = BlackKnights()
    black_bishops = BlackBishops()
    black_rooks = BlackRooks()
    black_queen = Queen("assets/b_queen_png_128px.png", 4, 8)
    black_king = King("assets/b_king_png_128px.png", 5, 8)
    game_running = True
    is_check = False
    is_checkmate = False
    while game_running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if selected_piece:
                    move_file: int = 0
                    move_rank: int = 0
                    for square in squares:
                        if square.rect.collidepoint(event.pos):
                            move_file = square.file
                            move_rank = square.rank
                            break
                    is_taking, taken_piece, taken_piece_group = check_taken(
                        black_pawns,
                        black_knights,
                        black_bishops,
                        black_rooks,
                        black_queen,
                        move_file,
                        move_rank,
                    )
                    if is_taking and selected_piece.allowed_take(move_file, move_rank):
                        if taken_piece_group is not None:
                            match (taken_piece_group, taken_piece):
                                case (BlackPawns(), Pawn()):
                                    taken_piece_group.remove(taken_piece)
                                case (BlackKnights(), Knight()):
                                    taken_piece_group.remove(taken_piece)
                                case (BlackBishops(), Bishop()):
                                    taken_piece_group.remove(taken_piece)
                                case (BlackRooks(), Rook()):
                                    taken_piece_group.remove(taken_piece)
                                case _:
                                    pass
                        if isinstance(taken_piece, Queen):
                            taken_piece.is_taken = True
                        selected_piece.move(move_file, move_rank)
                    elif selected_piece.allowed_move(move_file, move_rank):
                        is_moving_blocked = False
                        is_moving_occupied = check_moving_occupied(
                            white_pawns,
                            white_knights,
                            white_bishops,
                            white_rooks,
                            white_queen,
                            white_king,
                            event,
                        )
                        if is_moving_occupied:
                            print(
                                f"piece ({selected_piece.file}, {selected_piece.rank}) tried to moved to occupied square ({move_file}, {move_rank})"
                            )
                            selected_piece = None
                            continue
                        if isinstance(selected_piece, (Bishop, Queen)):
                            if (
                                selected_piece.rank < move_rank
                                and selected_piece.file < move_file
                            ):
                                is_moving_blocked = check_upper_right(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )
                            elif (
                                selected_piece.rank < move_rank
                                and selected_piece.file > move_file
                            ):
                                is_moving_blocked = check_lower_left(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )
                            elif (
                                selected_piece.rank > move_rank
                                and selected_piece.file > move_file
                            ):
                                is_moving_blocked = check_lower_right(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )
                            else:
                                is_moving_blocked = check_upper_left(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )

                        if isinstance(selected_piece, (Rook, Queen)):
                            if selected_piece.file == move_file:
                                is_moving_blocked = check_vertical(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )

                            if selected_piece.rank == move_rank:
                                is_moving_blocked = check_horizontal(
                                    selected_piece,
                                    white_pawns,
                                    white_knights,
                                    white_bishops,
                                    white_rooks,
                                    white_queen,
                                    white_king,
                                    move_file,
                                    move_rank,
                                )

                        if (
                            isinstance(selected_piece, Pawn)
                            and selected_piece.first_move
                        ):
                            is_moving_blocked = check_pawn_blocked(
                                selected_piece,
                                white_pawns,
                                white_knights,
                                white_bishops,
                                white_rooks,
                                white_queen,
                                white_king,
                                move_file,
                            )
                        if is_moving_blocked:
                            print(
                                f"piece ({selected_piece.file}, {selected_piece.rank}) tried to across pieces"
                            )
                            selected_piece = None
                            continue
                        print(
                            f"moving ({selected_piece.file}, {selected_piece.rank}) to ({move_file}, {move_rank})"
                        )
                        selected_piece.move(move_file, move_rank)
                    else:
                        print(
                            f"piece ({selected_piece.file}, {selected_piece.rank}) tried to move to ({move_file}, {move_rank})"
                        )
                    selected_piece = None
                    is_check = check_is_check(
                        white_pawns,
                        white_knights,
                        white_bishops,
                        white_rooks,
                        white_queen,
                        black_king,
                    )
                    if is_check:
                        if black_king.file == 1 and black_king.rank == 1:
                            no_escape_squares: int = 3
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                for black_pawn in black_pawns:
                                    if (
                                        black_pawn.file
                                        == black_king.file + possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if (
                                        black_knight.file
                                        == black_king.file + possible_move_file
                                        and black_knight.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if (
                                        black_bishop.file
                                        == black_king.file + possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if (
                                        black_rook.file
                                        == black_king.file + possible_move_file
                                        and black_rook.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                if (
                                    black_queen.file
                                    == black_king.file + possible_move_file
                                    and black_queen.rank
                                    == black_king.rank + possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                    continue
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.file == 1 and black_king.rank == 8:
                            no_escape_squares = 3
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                for black_pawn in black_pawns:
                                    if (
                                        black_pawn.file
                                        == black_king.file + possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if (
                                        black_knight.file
                                        == black_king.file + possible_move_file
                                        and black_knight.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if (
                                        black_bishop.file
                                        == black_king.file + possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if (
                                        black_rook.file
                                        == black_king.file + possible_move_file
                                        and black_rook.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                if (
                                    black_queen.file
                                    == black_king.file + possible_move_file
                                    and black_queen.rank
                                    == black_king.rank - possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                    continue
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.file == 8 and black_king.rank == 1:
                            no_escape_squares = 3
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                for black_pawn in black_pawns:
                                    if (
                                        black_pawn.file
                                        == black_king.file - possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if (
                                        black_knight.file
                                        == black_king.file - possible_move_file
                                        and black_knight.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if (
                                        black_bishop.file
                                        == black_king.file - possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if (
                                        black_rook.file
                                        == black_king.file - possible_move_file
                                        and black_rook.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                if (
                                    black_queen.file
                                    == black_king.file - possible_move_file
                                    and black_queen.rank
                                    == black_king.rank + possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                    continue
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.file == 8 and black_king.rank == 8:
                            no_escape_squares = 3
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                for black_pawn in black_pawns:
                                    if (
                                        black_pawn.file
                                        == black_king.file - possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if (
                                        black_knight.file
                                        == black_king.file - possible_move_file
                                        and black_knight.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if (
                                        black_bishop.file
                                        == black_king.file - possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if (
                                        black_rook.file
                                        == black_king.file - possible_move_file
                                        and black_rook.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        should_continue = True
                                        break
                                if should_continue:
                                    continue
                                if (
                                    black_queen.file
                                    == black_king.file - possible_move_file
                                    and black_queen.rank
                                    == black_king.rank - possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                    continue
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.file == 1:
                            no_escape_squares = 5
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                first_occupied = False
                                second_occupied = False
                                for black_pawn in black_pawns:
                                    if not first_occupied and (
                                        black_pawn.file
                                        == black_king.file + possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_pawn.file
                                            == black_king.file - possible_move_file
                                            and black_pawn.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if not first_occupied and (
                                        black_knight.file
                                        == black_king.file + possible_move_file
                                        and black_knight.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_knight.file
                                            == black_king.file - possible_move_file
                                            and black_knight.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if not first_occupied and (
                                        black_bishop.file
                                        == black_king.file + possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_bishop.file
                                            == black_king.file - possible_move_file
                                            and black_bishop.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if not first_occupied and (
                                        black_rook.file
                                        == black_king.file + possible_move_file
                                        and black_rook.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_rook.file
                                            == black_king.file - possible_move_file
                                            and black_rook.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                if not first_occupied and (
                                    black_queen.file
                                    == black_king.file + possible_move_file
                                    and black_queen.rank
                                    == black_king.rank + possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                if (
                                    not second_occupied
                                    and possible_move_rank > 0
                                    and (
                                        black_queen.file
                                        == black_king.file - possible_move_file
                                        and black_queen.rank
                                        == black_king.rank - possible_move_rank
                                    )
                                ):
                                    no_escape_squares -= 1
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.file == 8:
                            no_escape_squares = 5
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                first_occupied = False
                                second_occupied = False
                                for black_pawn in black_pawns:
                                    if not first_occupied and (
                                        black_pawn.file
                                        == black_king.file - possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_pawn.file
                                            == black_king.file - possible_move_file
                                            and black_pawn.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if not first_occupied and (
                                        black_knight.file
                                        == black_king.file - possible_move_file
                                        and black_knight.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_knight.file
                                            == black_king.file - possible_move_file
                                            and black_knight.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if not first_occupied and (
                                        black_bishop.file
                                        == black_king.file - possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_bishop.file
                                            == black_king.file - possible_move_file
                                            and black_bishop.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if not first_occupied and (
                                        black_rook.file
                                        == black_king.file - possible_move_file
                                        and black_rook.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_rank > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_rank > 0
                                        and (
                                            black_rook.file
                                            == black_king.file - possible_move_file
                                            and black_rook.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                if not first_occupied and (
                                    black_queen.file
                                    == black_king.file - possible_move_file
                                    and black_queen.rank
                                    == black_king.rank + possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                if (
                                    not second_occupied
                                    and possible_move_rank > 0
                                    and (
                                        black_queen.file
                                        == black_king.file - possible_move_file
                                        and black_queen.rank
                                        == black_king.rank - possible_move_rank
                                    )
                                ):
                                    no_escape_squares -= 1
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.rank == 1:
                            no_escape_squares = 5
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                first_occupied = False
                                second_occupied = False
                                for black_pawn in black_pawns:
                                    if not first_occupied and (
                                        black_pawn.file
                                        == black_king.file + possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_pawn.file
                                            == black_king.file - possible_move_file
                                            and black_pawn.rank
                                            == black_king.rank + possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if not first_occupied and (
                                        black_knight.file
                                        == black_king.file + possible_move_file
                                        and black_knight.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_knight.file
                                            == black_king.file - possible_move_file
                                            and black_knight.rank
                                            == black_king.rank + possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if not first_occupied and (
                                        black_bishop.file
                                        == black_king.file + possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_bishop.file
                                            == black_king.file - possible_move_file
                                            and black_bishop.rank
                                            == black_king.rank + possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if not first_occupied and (
                                        black_rook.file
                                        == black_king.file + possible_move_file
                                        and black_rook.rank
                                        == black_king.rank + possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_rook.file
                                            == black_king.file - possible_move_file
                                            and black_rook.rank
                                            == black_king.rank + possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                if not first_occupied and (
                                    black_queen.file
                                    == black_king.file + possible_move_file
                                    and black_queen.rank
                                    == black_king.rank + possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                if (
                                    not second_occupied
                                    and possible_move_file > 0
                                    and (
                                        black_queen.file
                                        == black_king.file - possible_move_file
                                        and black_queen.rank
                                        == black_king.rank + possible_move_rank
                                    )
                                ):
                                    no_escape_squares -= 1
                            if no_escape_squares == 0:
                                is_checkmate = True
                        elif black_king.rank == 8:
                            no_escape_squares = 5
                            for possible_move_file, possible_move_rank in [
                                (0, 1),
                                (1, 0),
                                (1, 1),
                            ]:
                                should_continue = False
                                first_occupied = False
                                second_occupied = False
                                for black_pawn in black_pawns:
                                    if not first_occupied and (
                                        black_pawn.file
                                        == black_king.file + possible_move_file
                                        and black_pawn.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_pawn.file
                                            == black_king.file - possible_move_file
                                            and black_pawn.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_knight in black_knights:
                                    if not first_occupied and (
                                        black_knight.file
                                        == black_king.file + possible_move_file
                                        and black_knight.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_knight.file
                                            == black_king.file - possible_move_file
                                            and black_knight.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_bishop in black_bishops:
                                    if not first_occupied and (
                                        black_bishop.file
                                        == black_king.file + possible_move_file
                                        and black_bishop.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_bishop.file
                                            == black_king.file - possible_move_file
                                            and black_bishop.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                for black_rook in black_rooks:
                                    if not first_occupied and (
                                        black_rook.file
                                        == black_king.file + possible_move_file
                                        and black_rook.rank
                                        == black_king.rank - possible_move_rank
                                    ):
                                        no_escape_squares -= 1
                                        if possible_move_file > 0:
                                            first_occupied = True
                                        else:
                                            should_continue = True
                                            break
                                    if (
                                        not second_occupied
                                        and possible_move_file > 0
                                        and (
                                            black_rook.file
                                            == black_king.file - possible_move_file
                                            and black_rook.rank
                                            == black_king.rank - possible_move_rank
                                        )
                                    ):
                                        no_escape_squares -= 1
                                        second_occupied = True
                                        if first_occupied:
                                            should_continue = True
                                            break
                                if should_continue:
                                    continue
                                if not first_occupied and (
                                    black_queen.file
                                    == black_king.file + possible_move_file
                                    and black_queen.rank
                                    == black_king.rank - possible_move_rank
                                ):
                                    no_escape_squares -= 1
                                if (
                                    not second_occupied
                                    and possible_move_file > 0
                                    and (
                                        black_queen.file
                                        == black_king.file - possible_move_file
                                        and black_queen.rank
                                        == black_king.rank - possible_move_rank
                                    )
                                ):
                                    no_escape_squares -= 1
                            if no_escape_squares == 0:
                                is_checkmate = True

                        if is_checkmate:
                            print("you won")
                else:
                    selected_piece = select_piece(
                        white_pawns,
                        white_knights,
                        white_bishops,
                        white_rooks,
                        white_queen,
                        white_king,
                        event,
                    )
                    if selected_piece:
                        print(
                            f"piece at ({selected_piece.file}, {selected_piece.rank}) selected"
                        )
                    else:
                        print("no piece selected")
            if event.type == pg.QUIT:
                game_running = False
        squares.update()
        squares.draw(screen)
        white_pawns.update()
        white_pawns.draw(screen)
        white_knights.update()
        white_knights.draw(screen)
        white_bishops.update()
        white_bishops.draw(screen)
        white_rooks.update()
        white_rooks.draw(screen)
        if not white_queen.is_taken:
            screen.blit(white_queen.image, white_queen.rect)
        screen.blit(white_king.image, white_king.rect)
        black_pawns.update()
        black_pawns.draw(screen)
        black_knights.update()
        black_knights.draw(screen)
        black_bishops.update()
        black_bishops.draw(screen)
        black_rooks.update()
        black_rooks.draw(screen)
        if not black_queen.is_taken:
            screen.blit(black_queen.image, black_queen.rect)
        screen.blit(black_king.image, black_king.rect)
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()
