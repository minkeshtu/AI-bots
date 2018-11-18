#!/bin/python3

# Function to return the next Move
def nextMove(r, c, board):  # r = row, c = column , board = playing board
    n = len(board)
    
    # To check the position of the dirty cell (d_r, d_c)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'd':
                d_r = i
                d_c = j
                break
        else:
            continue
        break
    
    
    # For cleaning, First bot will check it's own cell then it'll check same raw and then same column,
    # Furthermore we can divide our board into 4 parts from bot's position (raw and column),
    # bot will check each part one by one,
    # In the each part, We will choose the move according to the dirty cell position to make sure bot will take minimum steps to clean all cells
    if (c == d_c and r == d_r) :
        print('CLEAN')
    else :
        if r == d_r:
            if c < d_c:
                print('RIGHT')
            else:
                print('LEFT')

        elif c == d_c:
            if r > d_r:
                print('UP')
            else:
                print('DOWN')

        elif r < d_r:
            if c > d_c:
                if c - d_c >= d_r - r:
                    print('LEFT')
                else:
                    print('DOWN')
            else :
                if d_c - c >= d_r - r:
                    print('RIGHT')
                else:
                    print('DOWN')

        else :
            if c > d_c:
                if c - d_c >= r - d_r:
                    print('LEFT')
                else:
                    print('UP')
            else :
                if d_c - c >= r - d_r:
                    print('RIGHT')
                else:
                    print('UP')
                
    
# Imputs
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
