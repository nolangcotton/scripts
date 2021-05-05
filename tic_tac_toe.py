#!/usr/local/bin/python3
import sys
import click as c
'''
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
'''
c.clear()
#--------------------------------------
# Blank board to start, set turns to 0
#--------------------------------------
board        = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn_num     = 1
player       = ''
player_pair  = {'x':'P1', 'o':'P2'}

#--------------------------------------
#   Print Board
#--------------------------------------
def print_board(board):
    print('\nPrinting board: ')
    print('{} | {} | {}'.format(board[0],board[1],board[2]))
    print('---------')
    print('{} | {} | {}'.format(board[3],board[4],board[5]))
    print('---------')
    print('{} | {} | {}'.format(board[6],board[7],board[8]))

#--------------------------------------
#   Update board based on player input
#--------------------------------------
def update_board(board, posn, piece):
    if board[posn-1] == ' ':
        board[posn-1] = piece
    else:
        print('ERROR: space already chosen. Turn forfeited')
    return board

#--------------------------------------
#   Give users option to replay
#--------------------------------------
def replay():
    while True:
        replay_char = input('Would you like to play again (Y|N): ')
        replay_char.lower
        if replay_char == 'y':
            return True
        elif replay_char == 'n':
            return False
        else:
            print('ERROR: Invalid input: ' + replay_char)
            continue

def reset_board():
    board        = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn_num     = 1
    player       = ''
    return board, turn_num, player

#--------------------------------------
#   Validate board for winner 
#--------------------------------------
def check_for_winner(board, turn_num, player):
    if (board[0] != ' ' and board[0] == board[1] and board[1] == board[2] and board[0]) or (board[0] != ' ' and board[0] == board[3] and board[3] == board[6]):
        print('Congrats there is a winner')
        print_board(board)
        if replay():
            board, turn_num, player = reset_board()
        else:
            print('Goodbye!')
            sys.exit(0)
    elif (board[3] != ' ' and board[3] == board[4] and board[3] == board[5]) or (board[1] != ' ' and board[1] == board[4] and board[4] == board[7]):
        print('Congrats there is a winner')
        print_board(board)
        if replay():
            board, turn_num, player = reset_board()
        else:
            print('Goodbye!')
            sys.exit(0)
    elif (board[6] != ' ' and board[6] == board[7] and board[7] == board[8]) or (board[2] != ' ' and board[2] == board[5] and board[5] == board[8]):
        print('Congrats there is a winner')
        print_board(board)
        if replay():
            board, turn_num, player = reset_board()
        else:
            print('Goodbye!')
            sys.exit(0)
    elif ' ' not in board:
        print('Tie Game!')
        print_board(board)
        sys.exit(1)
    else:
        print('No winner yet...')

    return board, turn_num, player 
    
#--------------------------------------
#   Infinite Game Loop Until Winner
#--------------------------------------
while True:

    #--------------------------------------
    #   Print updated board
    #--------------------------------------
    print_board(board)

    #--------------------------------------
    #  Set piece
    #--------------------------------------
    if turn_num % 2 != 0:
        player = 'P1'
        piece  = 'x'
    elif turn_num % 2 == 0:
        player = 'P2'
        piece  = 'o'

    #--------------------------------------
    #   Get player input & update board
    #--------------------------------------
    print('Hello player: ' + player + ' turn number: ' + str(turn_num) + ' piece: ' + piece)
    posn  = int(input('Enter the position you want to take (1-9): '))
    board = update_board(board, posn, piece)
    
    #--------------------------------------
    #   See if someone won
    #--------------------------------------
    turn_num += 1
    board, turn_num, player = check_for_winner(board, turn_num, player)
    
