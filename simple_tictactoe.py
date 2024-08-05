
from random import randrange
import random


def display_board(board):
# The function accepts one parameter containing the board's current status
# and prints it out to the console.
    print("+-------"*3+"+")
    print("|       "*3+"|")
    print("|   "+board[0][0] +"   |"+ "   "+board[0][1] +"   |"+ "   "+board[0][2] +"   |")
    print("|       "*3+"|")
    print("+-------"*3+"+")
    print("|       "*3+"|")
    print("|   "+board[1][0] +"   |"+ "   "+board[1][1] +"   |"+ "   "+board[1][2] +"   |")
    print("|       "*3+"|")
    print("+-------"*3+"+")
    print("|       "*3+"|")
    print("|   "+board[2][0] +"   |"+ "   "+board[2][1] +"   |"+ "   "+board[2][2] +"   |")
    print("|       "*3+"|")
    print("+-------"*3+"+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move > 0 and move < 10:
                if move in make_list_of_free_fields(board):
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == str(move):
                                board[i][j] = 'O'
                                return
                else:
                    print("That spot is taken! Enter another.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free.append(int(board[i][j]))
    return free


def victory_for(board, sign):
# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
        # Check rows for victory
    if (board[0][0] == board[0][1] == board[0][2] == sign):
        return True
    if (board[1][0] == board[1][1] == board[1][2] == sign):
        return True
    if (board[2][0] == board[2][1] == board[2][2] == sign):
        return True

    # Check columns for victory
    if (board[0][0] == board[1][0] == board[2][0] == sign):
        return True
    if (board[0][1] == board[1][1] == board[2][1] == sign):
        return True
    if (board[0][2] == board[1][2] == board[2][2] == sign):
        return True

    # Check diagonals for victory
    if (board[0][0] == board[1][1] == board[2][2] == sign):
        return True
    if (board[0][2] == board[1][1] == board[2][0] == sign):
        return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = random.choice(free_fields)
        for i in range(3):
            for j in range(3):
                if board[i][j] == str(move):
                    board[i][j] = 'X'
                    return
    print("No moves left for the computer.")



    print("hello world")

       
count = 1
board = [['1','2','3'],['4','X','6'],['7','8','9']]

display_board(board)
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("O wins!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("X wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
