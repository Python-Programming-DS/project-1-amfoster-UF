#Project 1: Part A: Tic-Tac-Toe
#Created by: Ashley Foster (9/26/25)
#According to the Wikipedia page: Tic-Tac-Toe (https://en.wikipedia.org/wiki/Tic-tac-toe), 
#is a game for two players where each player takes turns marking a 3 x 3 grid, one with X's and the other with O's.
#A player wins when there are three X's or O's in a row, column, or on a diagonal. If the board is filled
#and no one has one, the game is considered a draw!

import random
import numpy as np

#Function to print the current state of the tic-tac-toe board
def printBoard(board):
    #board variable is list of available positions (or unavailable) and if filled with X or O
    print("-"*18)
    print("|R/C| 0 | 1 | 2 |")
    print("-"*18)
    print(f"| 0 | {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("-"*18)
    print(f"| 1 | {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("-"*18)
    print(f"| 2 | {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("-"*18)

#Check to see if user input is valid. 
#i.e. correct row/col numbers, has box been filled previously?
def validate_entry(pos,board,turn):
    if pos[0] >=3 or pos[1] >=3:
        print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
        return False
    if board[pos[0]][pos[1]] == 'O' or board[pos[0]][pos[1]] == 'X':
        print(f"That cell is already taken.\nPlease make another selection.")
        return False 
    return True

#Check to see if board is filled
def checkFull(board, turn):
    #If the board is not filled, keep going
    for row in range(len(board)):
        for col in range(len(board[row])):
            if str(board[row][col]) != ' ':
                return False  
    #If the board is filled, and no win condition has triggered:
            else:
                print(f"DRAW! NOBODY WINS!")
                printBoard(board)
                return True

#check win condition - vertical, horizontal, diagonal - 8 combos
def checkWin(board,turn):
    win_condition = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]
    win = [turn,turn,turn]
    for condition in win_condition:
        if condition == win:
            print(f"{turn} IS THE WINNER!!!")
            printBoard(board)
            return True
    return False
            
def main():
    again = 'y'
    while again.lower() == 'y':
        #Decide who goes first
        turn = random.choice(['X','O'])
        if turn == 'X':
            print("New Game: X goes first.")
        else: 
            print("New Game: O goes first.")
        print()
        #initiate board
        board = np.zeros((3,3),dtype = str)
        board = [[" " for col in range(7)] for row in range(6)]
        printBoard(board)
        while True:
            print(f"\n{turn}'s turn.")
            print(f"Where do you want your {turn} placed?")
            print("Please enter row number and column number separated by a comma.")
            pos = [int(ii) for ii in input().split(sep = ',')]
            print(f"You have entered row #{pos[0]} \n\t  and column #{pos[1]}")
            #Check if the entry is valid
            if validate_entry(pos,board,turn):
                board[pos[0]][pos[1]] = turn
                print("Thank you for your selection.")
                #Now, check if a win condition has been met
                if checkWin(board,turn):
                    break #leave while loop
                #Or if the board is full - AKA a draw
                elif checkFull(board,turn):
                    break #Leave While loop
                printBoard(board)
                
            #Change turns
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"

        #Ask if playing again?
        print("\nAnother game? Enter Y or y for yes.")
        again = input("")
#Initiate game
if __name__ == "__main__":
    main()
    print("Thank you for playing!")