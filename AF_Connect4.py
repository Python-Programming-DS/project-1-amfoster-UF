#Project 1: Part B: Connect 4
#Created by: Ashley Foster (9/26/25)
#According to the Wikipedia page Connect Four (https://en.wikipedia.org/wiki/Connect_Four#),
#"is a game where players choose a color and then take turns dropping colored tokens into a six-row, seven-column
#vertically suspended grid... The objective of the game is to be the first to form a horizontal, vertical, or diagonal line
#of four of one's own tokens."

import random
import numpy as np

#Function to print the current state of the Connect Four board
def printBoard(board):
    for j in range(5,-1,-1):
        print(f"| {j+1} |",end = " ")
        for k in range(0,7):
            if k == 6:
                print(f"{board[j][k]} |")
            else:
                print(f"{board[j][k]} |",end=" ")
        print('-'*35)
    print("|R/C| a | b | c | d | e | f | g |")
    print('-'*35)

#Check win condition - four X's or O's in a vertical, horizontal, or diagonal line
def checkWin(board,turn):
    win = [turn]*4
    for row in range(len(board)):
        for col in range(len(board[0])):            
            #check for horizontal win condition
            if col <= len(board[0]) - 4:
                if [board[row][col+i] for i in range(4)] == win:
                    print(f"{turn} IS THE WINNER!!!")
                    printBoard(board)
                    return True
            #Check for vertical win condition
            if row <= len(board) - 4:
                if [board[row+i][col] for i in range(4)]== win:
                    print(f"{turn} IS THE WINNER!!!")
                    printBoard(board)
                    return True
            #Check for diagonal win conditions
            if row <= len(board) - 4 and col <=len(board[0]) - 4:
                if [board[row+i][col+i] for i in range(4)] == win:
                    print(f"{turn} IS THE WINNER!!!")
                    printBoard(board)
                    return True
            if row >= 3 and col <= len(board[0]) - 4:
                if [board[row-i][col+i] for i in range(4)] == win:
                    print(f"{turn} IS THE WINNER!!!")
                    printBoard(board)
                    return True
    return False

#Check to see if the input is valid -check avail pos and input bounds
def validate_entry(pos, board,turn,avail_pos):
    if pos[0] not in "abcdefg" or int(pos[1]) >= 7:
        print("Invalid entry: try again.")
        return False
    if pos[0] in avail_pos.keys():
        if int(pos[1]) != avail_pos[pos[0]]:
            print("Invalid entry: try again")
            return False
        else:
            avail_pos[pos[0]] += 1
        if avail_pos[pos[0]] > 6:
            avail_pos.pop(pos[0])
    return True

def avail_pos_str(avail_pos):
    print(f"Available positions are: [", end = "")
    for i in avail_pos.keys():
        if i == 'g':
            print(f"'{i}{avail_pos[i]}']")
        else: 
            print(f"'{i}{avail_pos[i]}', ", end = "")

def main():
    again = 'y'
    while again.lower() == 'y':
        #X always goes first
        turn = "X"
        print("New Game: X goes first.")
        print()
        #Initiate board
        board = np.zeros((6,7), dtype = str)
        board = [[" " for col in range(7)] for row in range(6)]
        printBoard(board)
        col_name = "abcdefg"
        avail_pos = {'a':1,'b':1,'c':1,'d':1, 'e':1, 'f':1,'g':1}
        
        while True:
            print(f"\n{turn}'s turn.")
            print(f"Where do you want your {turn} placed?")
            avail_pos_str(avail_pos)
            pos = input("Please enter column-letter and row-number (e.g., a1): ")
            #Check if the entry is valid
            if validate_entry(list(pos),board, turn,avail_pos):
                #if it is a valid entry, place the X or O
                for i in range(len(col_name)):
                    if col_name[i] == pos[0]:
                        board[int(pos[1])-1][i] = turn
                print("Thank you for your selection.")
                
                if checkWin(board,turn):
                    break
                printBoard(board)
            
                #Change turns
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
        #Ask if playing again
        again = input("\nAnother game (y/n)? ")

if __name__ == "__main__":
    main()
    print("Thank you for playing!")