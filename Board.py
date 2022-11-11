from random import random
from Pieces import *
from browser import window
j = window.jQuery

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
            <div class="board">{self.html_board}</div>
            <div class="board1">{str(w_pawn_1)}{str(w_pawn_2)}{str(w_pawn_3)}{str(w_pawn_4)}{str(w_pawn_5)}{str(w_pawn_6)}\
            {str(w_pawn_7)}{str(w_pawn_8)}{str(w_knight_1)}{str(w_knight_2)}{str(w_bishop_1)}{str(w_bishop_2)}{str(w_king)}\
            {str(w_queen)}{str(w_rook_1)}{str(w_rook_2)}\
            {str(b_pawn_1)}{str(b_pawn_2)}{str(b_pawn_3)}{str(b_pawn_4)}{str(b_pawn_5)}{str(b_pawn_6)}\
            {str(b_pawn_7)}{str(b_pawn_8)}{str(b_knight_1)}{str(b_knight_2)}{str(b_bishop_1)}{str(b_bishop_2)}{str(b_king)}\
            {str(b_queen)}{str(b_rook_1)}{str(b_rook_2)}\
            </div>
        '''
