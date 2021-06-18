#Pythons function to add lots of space to clear the board

from IPython.display import clear_output
clear_output()

#displaying a board - the actual board will be displayed later  
#need board to have 10 elements so we can index 1-9

def display_board(board):
    clear_output()
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])

#Choose your marker from a player input

def player_input():
    marker = ''
    
    player_1_name = input("Player 1, what is your name? ")
    player_2_name = input("Player 2, what is your name? ")

    while not (marker == 'X' or marker == 'O'):
        marker = input('{}: Do you want to be X or O? '.format(player_1_name)).upper()

    if marker == 'X':
        print("{} you are X, which means {}, you are O".format(player_1_name, player_2_name))
        return ('X', 'O', player_1_name, player_2_name)
    else:
        print("{} you are O, which means {}, you are X".format(player_1_name, player_2_name))
        return ('O', 'X', player_1_name, player_2_name)

#function that takes in a board list object, the marker, the desired board position, and puts the marker at that position

def place_marker(board, marker, position):

  board[position] = marker

#win check function - determine whether placing a marker there has won the game or not - all solutions

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

#function to randomly decide which player goes first

import random

def choose_first():
    
    flip = random.randint(0,1)
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'


#function to return true or false if there is a space where the person is wanting to go

def space_check(board, position):
    
    return board[position] == ' '

#function to see if the board is full, if so and no one has won - it's a tie game

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    return True


#function that asks for a players position, checks if it is a free position, then return that position 

def player_choice(board, name):
    
    accepted = False
    position = 0
    while accepted == False:
        position = int(input(name +", Choose a position (1-9): "))
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            print("Thats not a valid position, {}!".format(name))
        else:
            accepted = True
    return position 

#function that asks if the players want to replay    

def replay():
    
    choice = input("Play again? Enter Y or N ")
    return choice.upper() == "Y"

 ######GAME LOGIC######

print("Welcome to X and Os!")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker, p1_name, p2_name = player_input()
    turn = choose_first()
    if turn == "Player 1":
      print(p1_name + ' will go first.')
    else:
      print(p2_name + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            print("{}, it's your turn!".format(p1_name))
            display_board(theBoard)
            position = player_choice(theBoard, p1_name)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations {}! You have won the game!'.format(p1_name))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print("{}, it's your turn!".format(p2_name))
            display_board(theBoard)
            position = player_choice(theBoard, p2_name)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('{} has won!'.format(p2_name))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break