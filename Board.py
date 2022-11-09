from random import random
from Pieces import *
from browser import window
j = window.jQuery

pawn = Pawn('A1', 'white')


class Board:

    def __init__(self, x, y) -> list:
        self.col = x
        self.row = y
        self.id = 'id' + str(random()).split('.')[1]
        self.board = [[0 for i in range(self.col)]
                      for j in range(self.row)]
        self.html_board = []
        self.fill_board = []
        i = 0
        while i < 64:
            if i % 2 == 0:
                self.html_board.append(
                    f'<div class="square bg-white" id="{self.col}-{self.row}"></div>')
            else:
                self.html_board.append(
                    f'<div class="square bg-black" id="{self.col}-{self.row}"></div>')
            i += 1

            '''if issubclass(type(board[col][row]), Piece):
                print(str(board[col][row]), end=' ')
            else:
                if row % 2 == 0:
                    if col % 2 == 0:
                        j('.board').append(
                            f'<div class="square bg-white id="{col}-{row}"></div>')
                    else:
                        j('.board').append(
                            f'<div class="square bg-black id="{col}-{row}"></div>')
                else:
                    if col % 2 == 0:
                        j('.board').append(
                            f'<div class="square bg-black id="{col}-{row}"></div>')
                    else:
                        j('.board').append(
                            f'<div class="square bg-white id="{col}-{row}"></div>')


            if col % 2 == 0:
                j('.board').append(f'<div class="square bg-black id="{col}-{row}"></div>')
                i += 0'''

        '''for col in range(1, 9):
            for row in range(1, 9):
                if row % 2 == 0:
                    if col % 2 == 0:
                        color = 'white'
                        self.html_board.append(f"""
                    <span class='square bg-{color}'>
                    </span>
                    """)
                    else:
                        color = 'black'
                        self.html_board.append(f"""
                    <span class='square bg-{color}'>
                    </span>
                    """)
                else:
                    if col % 2 == 0:
                        color = 'black'
                        self.html_board.append(f"""
                    <span class='square bg-{color}'>
                    </span>
                    """)
                    else:
                        color = 'white'
                self.html_board.append(f"""
                    <span class='square bg-{color}'>
                   </span>
                    """)'''
    # use __str__ to create
    # a html representation of a TrafficLight instance

    def __str__(self):
        return f'''
            <div class="board">
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            <div class ="square bg-y"></div>
            <div class ="square bg-x"></div>
            </div >
            <div class="board1">
            <div class ="piece">{pawn.icon}</div>
            </div >
        '''
