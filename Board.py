from random import random
from Pieces import *
from browser import window
j = window.jQuery
# nya
pawn = Pawn('A2', 'white')

w_pawn_1 = Pawn('A2', 'white')
w_pawn_2 = Pawn('B2', 'white')
w_pawn_3 = Pawn('C2', 'white')
w_pawn_4 = Pawn('D2', 'white')
w_pawn_5 = Pawn('E2', 'white')
w_pawn_6 = Pawn('F2', 'white')
w_pawn_7 = Pawn('G2', 'white')
w_pawn_8 = Pawn('H2', 'white')
w_knight_1 = Knight('B1', 'white')
w_knight_2 = Knight('G1', 'white')
w_bishop_1 = Bishop('C1', 'white')
w_bishop_2 = Bishop('F1', 'white')
w_rook_1 = Rook('A1', 'white')
w_rook_2 = Rook('H1', 'white')
w_queen = Queen('D1', 'white')
w_king = King('E1', 'white')

b_pawn_1 = Pawn('A7', 'black')
b_pawn_2 = Pawn('B7', 'black')
b_pawn_3 = Pawn('C7', 'black')
b_pawn_4 = Pawn('D7', 'black')
b_pawn_5 = Pawn('E7', 'black')
b_pawn_6 = Pawn('F7', 'black')
b_pawn_7 = Pawn('G7', 'black')
b_pawn_8 = Pawn('H7', 'black')
b_knight_1 = Knight('B8', 'black')
b_knight_2 = Knight('G8', 'black')
b_bishop_1 = Bishop('C8', 'black')
b_bishop_2 = Bishop('F8', 'black')
b_rook_1 = Rook('A8', 'blavk')
b_rook_2 = Rook('H8', 'black')
b_queen = Queen('D8', 'black')
b_king = King('E8', 'black')


class Board:

    def __init__(self, x, y) -> list:
        window.board = self
        self.col = x
        self.row = y
        self.id = 'id' + str(random()).split('.')[1]
        self.board = [[0 for i in range(self.col)]
                      for j in range(self.row)]
        self.html_board = f''
        if issubclass(type(self.board[1][1]), Piece):
            print(str(self.board[1][1]), end=' ')
        else:
            for row in range(x):
                for col in range(y):
                    if row % 2 == 0:
                        if col % 2 == 0:
                            self.html_board = self.html_board + \
                                f'<div class="square bg-x" id="{col}-{row}"></div>'
                        else:
                            self.html_board = self.html_board + \
                                f'<div class="square bg-y" id="{col}-{row}"></div>'
                    else:
                        if col % 2 == 0:
                            self.html_board = self.html_board + \
                                f'<div class="square bg-y" id="{col}-{row}"></div>'
                        else:
                            self.html_board = self.html_board + \
                                f'<div class="square bg-x" id="{col}-{row}"></div>'

    # use __str__ to create
    # a html representation of a TrafficLight instance

    def __str__(self):
        return f'''
            <div class="board">{str(square_a1)}{str(square_b1)}{str(square_c1)}{str(square_d1)}{str(square_e1)}{str(square_f1)}{str(square_g1)}{str(square_h1)}
            {str(square_a2)}{str(square_b2)}{str(square_c2)}{str(square_d2)}{str(square_e2)}{str(square_f2)}{str(square_g2)}{str(square_h2)}
            {str(square_a3)}{str(square_b3)}{str(square_c3)}{str(square_d3)}{str(square_e3)}{str(square_f3)}{str(square_g3)}{str(square_h3)}
            {str(square_a4)}{str(square_b4)}{str(square_c4)}{str(square_d4)}{str(square_e4)}{str(square_f4)}{str(square_g4)}{str(square_h4)}
            {str(square_a5)}{str(square_b5)}{str(square_c5)}{str(square_d5)}{str(square_e5)}{str(square_f5)}{str(square_g5)}{str(square_h5)}
            {str(square_a6)}{str(square_b6)}{str(square_c6)}{str(square_d6)}{str(square_e6)}{str(square_f6)}{str(square_g6)}{str(square_h6)}
            {str(square_a7)}{str(square_b7)}{str(square_c7)}{str(square_d7)}{str(square_e7)}{str(square_f7)}{str(square_g7)}{str(square_h7)}
            {str(square_a8)}{str(square_b8)}{str(square_c8)}{str(square_d8)}{str(square_e8)}{str(square_f8)}{str(square_g8)}{str(square_h8)}
            </div>
            <div class="board">{str(w_pawn_1)}{str(w_pawn_2)}{str(w_pawn_3)}{str(w_pawn_4)}{str(w_pawn_5)}{str(w_pawn_6)}\
            {str(w_pawn_7)}{str(w_pawn_8)}{str(w_knight_1)}{str(w_knight_2)}{str(w_bishop_1)}{str(w_bishop_2)}{str(w_king)}\
            {str(w_queen)}{str(w_rook_1)}{str(w_rook_2)}\
            {str(b_pawn_1)}{str(b_pawn_2)}{str(b_pawn_3)}{str(b_pawn_4)}{str(b_pawn_5)}{str(b_pawn_6)}\
            {str(b_pawn_7)}{str(b_pawn_8)}{str(b_knight_1)}{str(b_knight_2)}{str(b_bishop_1)}{str(b_bishop_2)}{str(b_king)}\
            {str(b_queen)}{str(b_rook_1)}{str(b_rook_2)}\
            </div>
        '''
    
    


class Square:
    def __init__(self, position, color) -> None:
        self.position = position
        self.color = color
        self.id = f's{position}'
        self.bind_events()

    def __str__(self):
        return f'''
        <div class="Square-{self.color}" style="grid-column-start:{col_remap_css[self.position[0]]}; grid-row-start:{row_remap_css[self.position[1]]};" id="{self.id}">
        </div>
        '''

    def bind_events(self):
        # Ask jQuery to listen to clicks on the body
        # (the whole content of the window)
        # if a click is on something with my id (self.id)
        # then run my click method
        j('body').on('click', f'#{self.id}', self.click)

    # note all event handlers must accept the event object
    # (even if the don't use it)
    def click(self, event):
        window.player_move_input(
            window.clicked_piece.position + " " + self.position)
        print(f'Click test {window.clicked_piece.position}')
        window.clicked_piece = None


square_a1 = Square('A1', 'Black')
square_b1 = Square('B1', 'White')
square_c1 = Square('C1', 'Black')
square_d1 = Square('D1', 'White')
square_e1 = Square('E1', 'Black')
square_f1 = Square('F1', 'White')
square_g1 = Square('G1', 'Black')
square_h1 = Square('H1', 'White')

square_a2 = Square('A2', 'White')
square_b2 = Square('B2', 'Black')
square_c2 = Square('C2', 'White')
square_d2 = Square('D2', 'Black')
square_e2 = Square('E2', 'White')
square_f2 = Square('F2', 'Black')
square_g2 = Square('G2', 'White')
square_h2 = Square('H2', 'Black')

square_a3 = Square('A3', 'Black')
square_b3 = Square('B3', 'White')
square_c3 = Square('C3', 'Black')
square_d3 = Square('D3', 'White')
square_e3 = Square('E3', 'Black')
square_f3 = Square('F3', 'White')
square_g3 = Square('G3', 'Black')
square_h3 = Square('H3', 'White')

square_a4 = Square('A4', 'White')
square_b4 = Square('B4', 'Black')
square_c4 = Square('C4', 'White')
square_d4 = Square('D4', 'Black')
square_e4 = Square('E4', 'White')
square_f4 = Square('F4', 'Black')
square_g4 = Square('G4', 'White')
square_h4 = Square('H4', 'Black')

square_a5 = Square('A5', 'Black')
square_b5 = Square('B5', 'White')
square_c5 = Square('C5', 'Black')
square_d5 = Square('D5', 'White')
square_e5 = Square('E5', 'Black')
square_f5 = Square('F5', 'White')
square_g5 = Square('G5', 'Black')
square_h5 = Square('H5', 'White')

square_a6 = Square('A6', 'White')
square_b6 = Square('B6', 'Black')
square_c6 = Square('C6', 'White')
square_d6 = Square('D6', 'Black')
square_e6 = Square('E6', 'White')
square_f6 = Square('F6', 'Black')
square_g6 = Square('G6', 'White')
square_h6 = Square('H6', 'Black')

square_a7 = Square('A7', 'Black')
square_b7 = Square('B7', 'White')
square_c7 = Square('C7', 'Black')
square_d7 = Square('D7', 'White')
square_e7 = Square('E7', 'Black')
square_f7 = Square('F7', 'White')
square_g7 = Square('G7', 'Black')
square_h7 = Square('H7', 'White')

square_a8 = Square('A8', 'White')
square_b8 = Square('B8', 'Black')
square_c8 = Square('C8', 'White')
square_d8 = Square('D8', 'Black')
square_e8 = Square('E8', 'White')
square_f8 = Square('F8', 'Black')
square_g8 = Square('G8', 'White')
square_h8 = Square('H8', 'Black')
