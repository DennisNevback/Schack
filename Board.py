from random import random
from Light import *


class Board:

    def __init__(self, x, y) -> list:
        self.col = x
        self.row = y
        self.id = 'id' + str(random()).split('.')[1]
        self.board = [[0 for i in range(self.col)] for j in range(self.row)]
        self.html_board = None
        for col in range(1, 9):
            for row in range(1, 9):
                if row % 2 == 0:
                    if col % 2 == 0:
                        color = 'white'
                    else:
                        color = 'black'
                else:
                    if col % 2 == 0:
                        color = 'black'
                    else:
                        color = 'white'
                self.html_board.append(f"""

                    <span class='square bg-{color}'>

                    </span>
                    """)
    # use __str__ to create
    # a html representation of a TrafficLight instance

    def __str__(self):
        return f"""
            <div class="board" id="{self.id}">
                {self}
            </div>
        """
