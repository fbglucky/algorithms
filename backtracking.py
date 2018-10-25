board_size = 4
board_example = [[False for x in range(board_size)] for y in range(board_size)]


def n_queens():
    recursive_n_queens(board_example, 0)


def recursive_n_queens(board, row):
    if row == len(board):
        # done, print the result
        display_board(board)
    else:
        for col in range(len(board)):
            if is_safe(board, row, col):
                place_queen(board, row, col)
                # move to the next row
                recursive_n_queens(board, row + 1)
                # if we get here, backtrack
                remove_queen(board, row, col)


def display_board(board):
    print(board)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[x][y]"""
    if True in board[row] or True in column(board, col) or True in get_diagonals(board, row, col):
        return False
    return True


def column(board, col):
    return [r[col] for r in board]


def is_same_diagonal(x1, y1, x2, y2):
    x_distance = x1 - x2
    y_distance = y1 - y2

    return abs(x_distance) == abs(y_distance)


def get_diagonals(board, row, col):
    return [board[i][j] for i in range(row) for j in range(len(board)) if is_same_diagonal(row, col, i, j)]


def place_queen(board, row, col):
    board[row][col] = True


def remove_queen(board, row, col):
    board[row][col] = False


n_queens()
