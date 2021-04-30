import random

board = [" "," "," "," "," "," "," "," "," "," "] #10 spots because the first one is technically the 0th

def print_headerandboard():
    print ("""
          IIIIIIIIIIIII     IIIIIIIIIIIIIII         IIIIIIIIIII
                I                   I                   I
                I                   I                   I
                I                   I                   I
                I                   I                   I
                I IC                I AC                I OE


                           1 |2 |3
                           __|__|__
                           4 |5 |6
                           __|__|__
                           7 |8 |9
                             |  |
                 Write a number 1-9 to pick the spot you want to play
        """)

    print ("   |   |    ")
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print ("   |   |    ")
    print ("___ ___ ___ ")
    print ("   |   |    ")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print ("   |   |    ")
    print ("___ ___ ___ ")
    print ("   |   |    ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print ("   |   |    ")



while True:
    print_headerandboard()
    
    #input for X
    turn = "X"
    choice = int(input("Please choose an empty space for X: "))

    while board[choice] != " ":
        print("That space is taken, please take another one")
        choice = int(input("Please choose an empty space for "+turn+": "))
    if board[choice] == " " :
        board[choice] = "X"
     
    #Check for X Win
    if(board[1] == "X" and board[2] == "X" and board[3] == "X") or \
        (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
        (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
        (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
        (board[3] == "X" and board[6] == "X" and board[9] == "X")or \
        (board[1] == "X" and board[5] == "X" and board[9] == "X")or \
        (board[3] == "X" and board[5] == "X" and board[7] == "X"):
        print("X wins.")
        print_headerandboard()
        break
    
    #input for O
    turn = "O"
    print_headerandboard()
    
    choice = int(input("Please choose an empty space for O: "))

    while board[choice] != " ":
        print("That space is taken, please take another one")
        choice = int(input("Please choose an empty space for "+turn+": "))   
    if board[choice] == " ":
        board[choice] = "O"

   #Check for O Win

    if (board[1] == "O" and board[2] == "O" and board[3] == "O")or \
        (board[4] == "O" and board[5] == "O" and board[6] == "O")or \
        (board[7] == "O" and board[8] == "O" and board[9] == "O")or \
        (board[1] == "O" and board[4] == "O" and board[7] == "O")or \
        (board[2] == "O" and board[5] == "O" and board[8] == "O")or \
        (board[3] == "O" and board[6] == "O" and board[9] == "O")or \
        (board[1] == "O" and board[5] == "O" and board[9] == "O")or \
        (board[3] == "O" and board[5] == "O" and board[7] == "O"):
        print("O wins.")
        print_headerandboard()
        break

   
