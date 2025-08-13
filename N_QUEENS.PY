def is_safe(board, row, col, n):    
    for i in range(row):
        if board[i][col] == 1:
            return False 
        
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True  

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0 

    return False

def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()


def n_queens(n):    
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    
    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print(-1)

n = int(input())
n_queens(n)