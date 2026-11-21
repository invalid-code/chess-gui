import pygame as pg

WIDTH, HEIGHT = (900, 600)


class Square(pg.sprite.Sprite):
    def __init__(self, fill: tuple[int, int, int], rank: int, file: int) -> None:
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(fill)
        self.rect = self.image.get_rect()
        self.rect.left = (file - 1) * 50
        self.rect.top = (rank - 1) * 50
        self.file = file
        self.rank = 9 - rank


class Squares(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        for rank in range(1, 9):
            for file in range(1, 9):
                if rank % 2 == 0:
                    if file % 2 == 0:
                        self.add(Square((255, 255, 255), file, rank))
                    else:
                        self.add(Square((0, 0, 0), file, rank))
                else:
                    if file % 2 == 0:
                        self.add(Square((0, 0, 0), file, rank))
                    else:
                        self.add(Square((255, 255, 255), file, rank))


class Pawn(pg.sprite.Sprite):
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        super().__init__()
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

    def allowed_take(self, move: tuple[int, int]) -> bool:
        return True  # TODO


class Knight(pg.sprite.Sprite):
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        super().__init__()
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
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        super().__init__()
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
    def __init__(self, image_file: str, file: int, rank: int) -> None:
        super().__init__()
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


class WhitePawns(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.add(Pawn("assets/w_pawn_png_128px.png", 5, 2))


class WhiteKnights(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.add(Knight("assets/w_knight_png_128px.png", 7, 1))


class WhiteBishops(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.add(Bishop("assets/w_bishop_png_128px.png", 6, 1))


class WhiteRooks(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.add(Rook("assets/w_rook_png_128px.png", 8, 1))


Piece = Pawn | Knight | Bishop | Rook | Queen | King


def check_horizontal(
    selected_piece: Rook,
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
    selected_piece: Rook,
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
                and selected_piece.rank < whitewhite_bishop_pawn.rank
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
    game_running = True
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
                    if selected_piece.allowed_move(move_file, move_rank):
                        is_moving_occupied = False
                        is_moving_blocked = False
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
                        if isinstance(selected_piece, Bishop):
                            pass

                        if isinstance(selected_piece, Rook):
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
                            for white_pawn in white_pawns:
                                if selected_piece == white_pawn:
                                    continue
                                if (
                                    white_pawn.file == move_file
                                    or white_pawn.rank > selected_piece.rank
                                ):
                                    is_moving_blocked = True
                                    break
                            for white_knight in white_knights:
                                if (
                                    white_knight.file == move_file
                                    and white_knight.rank > selected_piece.rank
                                ):
                                    is_moving_blocked = True
                                    break
                            for white_bishop in white_bishops:
                                if (
                                    white_bishop.file == move_file
                                    and white_bishop.rank > selected_piece.rank
                                ):
                                    is_moving_blocked = True
                                    break
                            for white_rook in white_rooks:
                                if (
                                    white_rook.file == move_file
                                    and white_rook.rank > selected_piece.rank
                                ):
                                    is_moving_blocked = True
                                    break
                            if (
                                white_queen.file == move_file
                                and white_queen.rank > selected_piece.rank
                            ):
                                is_moving_blocked = True
                            if (
                                white_king.file == move_file
                                and white_king.rank > selected_piece.rank
                            ):
                                is_moving_blocked = True
                        if is_moving_occupied:
                            print(
                                f"piece ({selected_piece.file}, {selected_piece.rank}) tried to moved to occupied square ({white_pawn.file}, {white_pawn.rank})"
                            )
                            selected_piece = None
                            continue
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
                else:
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
        screen.blit(white_queen.image, white_queen.rect)
        screen.blit(white_king.image, white_king.rect)
        pg.display.flip()
    print("Goodbye!")
    pg.quit()


if __name__ == "__main__":
    main()
