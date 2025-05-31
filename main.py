from Board import Board
from Pieces import *
from asyncio import start_server
from contextlib import nullcontext
from operator import pos
from optparse import Values
import re
from browser import window, aio
j = window.jQuery


# Create a new application
#Initiera Board och rendera i webläsaren
board_wrapper = Board(8, 8)
j('body').html(str(board_wrapper))
board = board_wrapper.board
# j('Piece').on('click', f'#{pawn.id}', self.click)
j('square').click(print('diska'))

game_state = {
    'me': None,
    'opponent': None,
    'is_server': None,
    'move': None,
    'shared': {
        'player_1': '',
        'player_2': '',
        'game_over_message': ''
    }
}


'''def get_opponent_and_decide_game_runner(user, message):
# who is the server (= the creator of the channel)
  if 'created the channel' in message:
      name = message.split("'")[1]
      game_state['is_server'] = name == game_state['me']
  # who is the opponent (= the one that joined that is not me)
  if 'joined channel' in message:
      name = message.split(' ')[1]
      if name != game_state['me']:
          game_state['opponent'] = name


def on_network_message(timestamp, user, message):
  if user == 'system':
      get_opponent_and_decide_game_runner(user, message)
  # key_downs (only of interest to the server)
  global keys_down_me, keys_down_opponent
  if game_state['is_server']:
      if user == game_state['me'] and type(message) is list:
          keys_down_me = set(message)
      if user == game_state['opponent'] and type(message) is list:
          keys_down_opponent = set(message)
  # shared state (only of interest to the none-server)
  if type(message) is dict and not game_state['is_server']:
      game_state['shared'] = message
      render_board()'''


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
# rows, cols = (8, 8)
# board = [[0 for i in range(cols)] for j in range(rows)]



turn = 'white'  # Startar med vit spelare
playing = True
player_move = ''
player = 'black'

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


def set_board():
    global board
    board[col_remap['A']][row_remap['2']] = w_pawn_1
    board[col_remap['B']][row_remap['2']] = w_pawn_2
    board[col_remap['C']][row_remap['2']] = w_pawn_3
    board[col_remap['D']][row_remap['2']] = w_pawn_4
    board[col_remap['E']][row_remap['2']] = w_pawn_5
    board[col_remap['F']][row_remap['2']] = w_pawn_6
    board[col_remap['G']][row_remap['2']] = w_pawn_7
    board[col_remap['H']][row_remap['2']] = w_pawn_8
    board[col_remap['A']][row_remap['1']] = w_rook_1
    board[col_remap['B']][row_remap['1']] = w_knight_1
    board[col_remap['C']][row_remap['1']] = w_bishop_1
    board[col_remap['D']][row_remap['1']] = w_queen
    board[col_remap['E']][row_remap['1']] = w_king
    board[col_remap['F']][row_remap['1']] = w_bishop_2
    board[col_remap['G']][row_remap['1']] = w_knight_2
    board[col_remap['H']][row_remap['1']] = w_rook_2

    board[col_remap['A']][row_remap['7']] = b_pawn_1
    board[col_remap['B']][row_remap['7']] = b_pawn_2
    board[col_remap['C']][row_remap['7']] = b_pawn_3
    board[col_remap['D']][row_remap['7']] = b_pawn_4
    board[col_remap['E']][row_remap['7']] = b_pawn_5
    board[col_remap['F']][row_remap['7']] = b_pawn_6
    board[col_remap['G']][row_remap['7']] = b_pawn_7
    board[col_remap['H']][row_remap['7']] = b_pawn_8
    board[col_remap['A']][row_remap['8']] = b_rook_1
    board[col_remap['B']][row_remap['8']] = b_knight_1
    board[col_remap['C']][row_remap['8']] = b_bishop_1
    board[col_remap['D']][row_remap['8']] = b_queen
    board[col_remap['E']][row_remap['8']] = b_king
    board[col_remap['F']][row_remap['8']] = b_bishop_2
    board[col_remap['G']][row_remap['8']] = b_knight_2
    board[col_remap['H']][row_remap['8']] = b_rook_2


def temp_board_map():
    global board
    temp_list = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if issubclass(type(board[col][row]), Piece):
                print(board[col][row])
                temp_list.append((board[col][row]))
    print(temp_list)
    return temp_list


def player_move_input(player_move):
    print(player_move)
    global playing
    global turn
    player_move = player_move.upper()
    if board[col_remap[player_move[0]]][row_remap[player_move[1]]] != 0 and turn == board[col_remap[player_move[0]]][row_remap[player_move[1]]].color:
        if re.match('[oO]-[Oo]$', player_move):
            rochad()
            print('rochad1 success')
        elif re.match('[oO]-[Oo]-[oO]', player_move):
            rochad()
            print('rochad success')
        elif re.match('[A-H][1-8]\s[A-H][1-8]', player_move):
            input_board(player_move)
            print('input sucess')
        elif re.match('end', player_move):
            playing = False
        else:
            print('Invalid input')
    elif board[col_remap[player_move[0]]][row_remap[player_move[1]]] == 0:
        print('That square is empty')
    else:
        print('Those are not your pieces')


window.player_move_input = player_move_input
window.clicked_piece = None



def render_board():
    global board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if issubclass(type(board[col][row]), Piece):
                print(str(board[col][row]), end=' ')
            else:
                if row % 2 == 0:
                    if col % 2 == 0:
                        print('■', end=' ')  # color= white
                    else:
                        print('□', end=' ')  # color=black
                else:
                    if col % 2 == 0:
                        print('□', end=' ')
                    else:
                        print('■', end=' ')
        print()

def update_board_html():
    j('body').html(str(board_wrapper))


def input_board(move):
    global board
    global turn
    start_square, end_square = move.split(' ')  # E2 D4
    start_square_col = col_remap[start_square[0]]  # E -> 4
    start_square_row = row_remap[start_square[1]]  # 2 -> 6
    end_square_col = col_remap[end_square[0]]  # D -> 3
    end_square_row = row_remap[end_square[1]]  # 4 -> 4
    if board[start_square_col][start_square_row].move(
        end_square_col, end_square_row, board):
        #Update piece position on the board
        #board[end_square_col][end_square_row].position = end_square
        #board[start_square_col][start_square_row].position = end_square
        window.clicked_piece.position = end_square
        #Testa uppdatera HTML brädet efter varje drag
        window.setTimeout(update_board_html,100)
        #Byt spelare
        turn = player_turn()


def rochad() -> None:
    global board
    if not board[0][7] == 0 and not board[0][7].moves and not board[4][7] == 0 and not board[4][7].moves:
        if not board[1][7] and not board[2][7] and not board[3][7]:
            board[1][7] = w_king
            board[2][7] = w_rook_1
            board[0][7] = 0
            board[4][7] = 0
    elif not board[7][7] == 0 and not board[7][7].moves and not board[4][7] == 0 and not board[4][7].moves:
        if not board[5][7] and not board[6][7]:
            board[6][7] = w_king
            board[5][7] = w_rook_1
            board[7][7] = 0
            board[4][7] = 0
    elif not board[0][0] == 0 and not board[0][0].moves and not board[4][0] == 0 and not board[4][0].moves:
        if not board[1][0] and not board[2][7] and not board[3][0]:
            board[1][0] = w_king
            board[2][0] = w_rook_1
            board[0][0] = 0
            board[4][0] = 0
    elif not board[7][0] == 0 and not board[7][0].moves and not board[4][0] == 0 and not board[4][0].moves:
        if not board[5][0] and not board[6][0]:
            board[6][0] = w_king
            board[5][0] = w_rook_1
            board[7][0] = 0
            board[4][0] = 0
    else:
        print('Castles not possbile')


def player_turn() -> str:
    global turn
    turn = 'black' if turn == 'white' else 'white'
    print(turn + "'s turn")
    return turn


def win() -> None:
    global playing
    white_state = False
    black_state = False
    for x in board:
        for y in x:
            Test = isinstance(y, King)
            if Test:
                if y.color == 'white':
                    white_state = True
                if y.color == 'black':
                    black_state = True
    if not black_state:
        playing = False
        print('White has won!')
    if not white_state:
        playing = False
        print('Black has won!')


def game_loop():
    print('\n Welcome to Chess, capture the enemy king to win the game!\n')
    set_board()
    render_board()
    print(turn + 's turn')


game_loop()
