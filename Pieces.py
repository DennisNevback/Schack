from queue import Empty
from random import random
from browser import window
# from Board import Board
j = window.jQuery


col_remap = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
    # coordinate_remap('B'), 3)
}
row_remap = {
    '1': 7,
    '2': 6,
    '3': 5,
    '4': 4,
    '5': 3,
    '6': 2,
    '7': 1,
    '8': 0
    # coordinate_remap('B'), 3)
}
col_remap_css = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8
    # coordinate_remap('B'), 3)
}
row_remap_css = {
    '1': 8,
    '2': 7,
    '3': 6,
    '4': 5,
    '5': 4,
    '6': 3,
    '7': 2,
    '8': 1
    # coordinate_remap('B'), 3)
}


def pos_to_col(pos_x: str) -> int:
    return col_remap[pos_x]


def col_to_pos(col: int) -> str:
    return list(col_remap.keys())[list(col_remap.values()).index(col)]


def pos_to_row(pos_y: str) -> int:
    return row_remap[pos_y]


def row_to_pos(row: int) -> str:
    return list(row_remap.keys())[list(row_remap.values()).index(row)]


class Piece:
    valid_moves: list = []

    def __init__(self, position, color) -> None:
        self.moves = []
        self.position = position
        self.color = color
        self.icon = None
        self.id = 'id' + str(random()).split('.')[1]
        self.bind_events()
        self.counter_click_row = row_remap_css[self.position[1]]
        self.counter_click_col = col_remap_css[self.position[0]]
        self.test = f''

    def bind_events(self):
        # Ask jQuery to listen to clicks on the body
        # (the whole content of the window)
        # if a click is on something with my id (self.id)
        # then run my click method
        j('body').on('click', f'#{self.id}', self.click)

    # note all event handlers must accept the event object
    # (even if the don't use it)
    def click(self, event):
        self.test += self.position
        print(self.test)
        print(event.target.id)
        print(event.target.grid)
        self.counter_click_row = self.counter_click_row + 1
        j(f'#{self.id}').css('grid-row-start', f'{self.counter_click_row}')
        # j('body').on('mouseup', f'#{self.id}', (print('dadada'))

    def __str__(self):
        return f"""
            <div class="Piece {self.type}" style="grid-column-start:{col_remap_css[self.position[0]]}; grid-row-start:{row_remap_css[self.position[1]]};" id="{self.id}">
                {self.icon}
            </div>
        """

    def move(self, start: str, end: str, board: list[list[int]]):
        self.add_valid_moves(board)
        col = col_to_pos(start)
        row = row_to_pos(end)
        end_move = col + row
        if end_move in self.valid_moves:
            self.moves.append(f'{self.position} -> {col}{row}')
            board[start][end] = self
            board[self.pos_x][self.pos_y] = 0
            self.position = col + row
            print(f'updated pos {self.position}')
            print(self.moves)
        else:
            print('invalid move')

    def add_valid_moves(self, board: list[list[int]]):
        print('add moves piece')
        self.valid_moves.clear()
        self.pos_x = pos_to_col(self.position[0])
        self.pos_y = pos_to_row(self.position[1])
        print('Piece valid moves End')


class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♙', '♟')[color == 'white']
        self.type = 'pawn'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        print('add moves pawn')
        print(self.color)
        super().add_valid_moves(board)
        if self.color == 'white':
            if board[self.pos_x][self.pos_y - 1] == 0:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y-1))
        if self.color == 'black':
            if board[self.pos_x][self.pos_y + 1] == 0:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y+1))

        if self.color == 'white':
            if board[self.pos_x][self.pos_y - 2] == 0 and not self.moves:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y-2))
        if self.color == 'black':
            if board[self.pos_x][self.pos_y + 2] == 0 and not self.moves:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y+2))

        if self.color == 'white':
            if board[self.pos_x - 1][self.pos_y - 1] != 0 and board[self.pos_x - 1][self.pos_y - 1].color != self.color:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 1)+row_to_pos(self.pos_y - 1))
        if self.color == 'black':
            if board[self.pos_x - 1][self.pos_y + 1] != 0 and board[self.pos_x - 1][self.pos_y + 1].color != self.color:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 1)+row_to_pos(self.pos_y+1))

        if self.color == 'white':
            if -1 < self.pos_x < 7 and -1 < self.pos_y < 8:
                if board[self.pos_x + 1][self.pos_y - 1] != 0 and board[self.pos_x + 1][self.pos_y - 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 1)+row_to_pos(self.pos_y - 1))
        if self.color == 'black':
            if -1 < self.pos_x < 7 and -1 < self.pos_y < 8:
                if board[self.pos_x + 1][self.pos_y + 1] != 0 and board[self.pos_x + 1][self.pos_y + 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 1)+row_to_pos(self.pos_y + 1))
        print(f'valid moves: {str(self.valid_moves)}')


class Bishop(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♗', '♝')[color == 'white']
        self.type = 'bishop'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        print('add moves bishop')
        super().add_valid_moves(board)
        print('cleared -adding new moves')
        print(self.pos_x)
        print(self.pos_y)
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values:  # example
            if self.pos_x - value > -1 and self.pos_y - value > -1:
                if board[self.pos_x-value][self.pos_y-value] != 0:
                    if board[self.pos_x-value][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y-value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y-value))

        for value in values:  # example
            if self.pos_x + value < 8 and self.pos_y - value > -1:
                if board[self.pos_x+value][self.pos_y-value] != 0:
                    if board[self.pos_x+value][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y-value))
                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y-value))

        for value in values:  # example
            if self.pos_x - value > -1 and self.pos_y + value < 8:
                if board[self.pos_x-value][self.pos_y+value] != 0:
                    if board[self.pos_x-value][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y+value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y+value))

        for value in values:  # example
            if self.pos_x + value < 8 and self.pos_y + value < 8:
                if board[self.pos_x+value][self.pos_y+value] != 0:
                    if board[self.pos_x+value][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y+value))
                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y+value))
        print('bishop end')
        print(self.valid_moves)


class Rook(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♖', '♜')[color == 'white']
        self.type = 'rook'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        super().add_valid_moves(board)
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values:  # example
            if self.pos_x + value < 8:
                if board[self.pos_x+value][self.pos_y] != 0:
                    if board[self.pos_x+value][self.pos_y].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y))
        for value in values:  # example
            if self.pos_x - value > -1:
                if board[self.pos_x-value][self.pos_y] != 0:
                    if board[self.pos_x-value][self.pos_y].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y))
        for value in values:  # example
            if self.pos_y + value < 8:
                if board[self.pos_x][self.pos_y+value] != 0:
                    if board[self.pos_x][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x)+row_to_pos(self.pos_y+value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y+value))
        for value in values:  # example
            if self.pos_y - value > -1:
                if board[self.pos_x][self.pos_y - value] != 0:
                    if board[self.pos_x][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x)+row_to_pos(self.pos_y-value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y-value))


class Queen(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♕', '♛')[color == 'white']
        self.type = 'queen'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        super().add_valid_moves(board)
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values:  # example
            if self.pos_x + value < 8:
                if board[self.pos_x+value][self.pos_y] != 0:
                    if board[self.pos_x+value][self.pos_y].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y))
        for value in values:  # example
            if self.pos_x - value > -1:
                if board[self.pos_x-value][self.pos_y] != 0:
                    if board[self.pos_x-value][self.pos_y].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y))
        for value in values:  # example
            if self.pos_y + value < 8:
                if board[self.pos_x][self.pos_y+value] != 0:
                    if board[self.pos_x][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x)+row_to_pos(self.pos_y+value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y+value))
        for value in values:  # example
            if self.pos_y - value > -1:
                if board[self.pos_x][self.pos_y - value] != 0:
                    if board[self.pos_x][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x)+row_to_pos(self.pos_y-value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y-value))

        for value in values:  # example
            if self.pos_x - value > -1 and self.pos_y - value > -1:
                if board[self.pos_x-value][self.pos_y-value] != 0:
                    if board[self.pos_x-value][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y-value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y-value))

        for value in values:  # example
            if self.pos_x + value < 8 and self.pos_y - value > -1:
                if board[self.pos_x+value][self.pos_y-value] != 0:
                    if board[self.pos_x+value][self.pos_y-value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y-value))
                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y-value))

        for value in values:  # example
            if self.pos_x - value > -1 and self.pos_y + value < 8:
                if board[self.pos_x-value][self.pos_y+value] != 0:
                    if board[self.pos_x-value][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x-value)+row_to_pos(self.pos_y+value))

                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-value)+row_to_pos(self.pos_y+value))

        for value in values:  # example
            if self.pos_x + value < 8 and self.pos_y + value < 8:
                if board[self.pos_x+value][self.pos_y+value] != 0:
                    if board[self.pos_x+value][self.pos_y+value].color != self.color:
                        self.valid_moves.append(col_to_pos(
                            self.pos_x+value)+row_to_pos(self.pos_y+value))
                    break
                else:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+value)+row_to_pos(self.pos_y+value))


class King(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♔', '♚')[color == 'white']
        self.type = 'king'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        super().add_valid_moves(board)
        if self.pos_x + 1 < 8:
            if board[self.pos_x+1][self.pos_y] != 0:
                if board[self.pos_x+1][self.pos_y].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x+1)+row_to_pos(self.pos_y))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x+1)+row_to_pos(self.pos_y))

        if self.pos_x - 1 > -1:
            if board[self.pos_x-1][self.pos_y] != 0:
                if board[self.pos_x-1][self.pos_y].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x-1)+row_to_pos(self.pos_y))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x-1)+row_to_pos(self.pos_y))

        if self.pos_y + 1 < 8:
            if board[self.pos_x][self.pos_y + 1] != 0:
                if board[self.pos_x][self.pos_y+1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y + 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y+1))

        if self.pos_y - 1 > -1:
            if board[self.pos_x][self.pos_y - 1] != 0:
                if board[self.pos_x][self.pos_y-1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x)+row_to_pos(self.pos_y - 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x)+row_to_pos(self.pos_y-1))


class Knight(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.icon = ('♘', '♞')[color == 'white']
        self.type = 'knight'

    def add_valid_moves(self, board: list[list[int]]) -> None:
        super().add_valid_moves(board)
        if self.pos_x + 2 < 8 and self.pos_y + 1 < 8:
            if board[self.pos_x + 2][self.pos_y + 1] != 0:
                if board[self.pos_x + 2][self.pos_y + 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 2)+row_to_pos(self.pos_y + 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x + 2)+row_to_pos(self.pos_y + 1))

        if self.pos_x + 2 < 8 and self.pos_y - 1 > -1:
            if board[self.pos_x + 2][self.pos_y - 1] != 0:
                if board[self.pos_x + 2][self.pos_y - 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 2)+row_to_pos(self.pos_y - 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x + 2)+row_to_pos(self.pos_y - 1))

        if self.pos_x - 2 > -1 and self.pos_y + 1 < 8:
            if board[self.pos_x - 2][self.pos_y + 1] != 0:
                if board[self.pos_x - 2][self.pos_y + 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x - 2)+row_to_pos(self.pos_y + 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 2)+row_to_pos(self.pos_y + 1))

        if self.pos_x - 2 > -1 and self.pos_y - 1 > -1:
            if board[self.pos_x - 2][self.pos_y - 1] != 0:
                if board[self.pos_x - 2][self.pos_y - 1].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x - 2)+row_to_pos(self.pos_y - 1))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 2)+row_to_pos(self.pos_y - 1))

        if self.pos_x + 1 < 8 and self.pos_y + 2 < 8:
            if board[self.pos_x + 1][self.pos_y + 2] != 0:
                if board[self.pos_x + 1][self.pos_y + 2].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 1)+row_to_pos(self.pos_y + 2))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x + 1)+row_to_pos(self.pos_y + 2))

        if self.pos_x - 1 > -1 and self.pos_y + 2 < 8:
            if board[self.pos_x - 1][self.pos_y + 2] != 0:
                if board[self.pos_x - 1][self.pos_y + 2].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x - 1)+row_to_pos(self.pos_y + 2))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 1)+row_to_pos(self.pos_y + 2))

        if self.pos_x + 1 < 8 and self.pos_y - 2 > -1:
            if board[self.pos_x + 1][self.pos_y - 2] != 0:
                if board[self.pos_x + 1][self.pos_y - 2].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x + 1)+row_to_pos(self.pos_y - 2))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x + 1)+row_to_pos(self.pos_y - 2))

        if self.pos_x - 1 > -1 and self.pos_y - 2 > -1:
            if board[self.pos_x - 1][self.pos_y - 2] != 0:
                if board[self.pos_x - 1][self.pos_y - 2].color != self.color:
                    self.valid_moves.append(col_to_pos(
                        self.pos_x - 1)+row_to_pos(self.pos_y - 2))

            else:
                self.valid_moves.append(col_to_pos(
                    self.pos_x - 1)+row_to_pos(self.pos_y - 2))


class Light:

    # constructor
    def __init__(self, color, my_traffic_light):
        # create a unique id
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        # transfer arguments to attributes
        self.color = color
        self.my_traffic_light = my_traffic_light
        # bind events
        self.bind_events()

    def bind_events(self):
        # Ask jQuery to listen to clicks on the body
        # (the whole content of the window)
        # if a click is on something with my id (self.id)
        # then run my click method
        j('body').on('click', f'#{self.id}', self.click)

    # note all event handlers must accept the event object
    # (even if the don't use it)
    def click(self, event):
        # Dim all lights in my traffic light
        j(f'#{self.my_traffic_light.id} .light').css('opacity', 0.3)
        # Undim me
        j(f'#{self.id}').css('opacity', 1)
