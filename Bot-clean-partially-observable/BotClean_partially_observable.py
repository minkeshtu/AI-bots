#!/bin/python3

# Function to return the next Move
def next_move(r, c, board): # r = row, c = column , board = playing board
    # To check dirty cell available in the observable area or not - yes/No = 1/0 respectively
    validator = 0 
    
    # To check the position of the dirty cell (d_r, d_c)
    for i in range(r-1,r+2):
        if i < 0 or i > (len(board)-1):
            continue
        for j in range(c-1,c+2):
            if j < 0 or j > (len(board)-1):
                continue
            if board[i][j] == 'd':
                d_r = i
                d_c = j
                validator = 1
                break
        else:
            continue
        break
    
    # dirty cell is not available in the observable area that's why bot will try to find out dirty cell
    # We need to make sure that bot should not stuck anywhere in the board because it's observable area is limited
    # otherwise we will lose the game, Hence, we need to move our bot in the entire board to find out the dirty cell.
    # But we also need to make sure that bot should take the optimal path to reduce the cleaning time
    if validator == 0:
        if r == 0:
            print('DOWN')
        elif c == len(board)-1:
            print('LEFT')
        elif r == len(board)-1:
            print('UP')
        elif c == 0:
            print('RIGHT')
        else:
            if (r < (len(board)-2)) and ((c != (len(board)-2)) or (((c == len(board)-2)) and r == 1)):
                if r > 1 and c != 1:
                    print('UP')
                else:
                    if c > 1:
                        print('LEFT')
                    else:
                        print('DOWN') 
            else:
                if c < len(board)-2:
                    print('RIGHT')
                else:
                    print('UP')
            
    # dirty cell is available in the observable area that's why bot will try to clean that cell
    # First bot will check it's own cell then it'll check same raw and then same column,
    # Furthermore we can divide our board into 4 parts from bot's position (raw and column),
    # bot will check each part one by one,
    # In the each part, We will choose the move according to the dirty cell position to make sure bot will take minimum steps to clean all cells
    else:
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


# Inputs
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)
