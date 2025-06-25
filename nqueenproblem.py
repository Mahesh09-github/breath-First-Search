N = 8

def printSolution(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def isSafe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""

    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solveNQueens(board, row, n):
    """Use backtracking to solve the N-Queens problem."""
    if row == n:
        printSolution(board)
        return True  # To find only one solution, else remove this line

    result = False
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            result = solveNQueens(board, row + 1, n) or result
            board[row][col] = 0  # Backtrack

    return result

def nQueens(n):
    """Driver function to solve the N-Queens problem."""
    board = [[0] * n for _ in range(n)]
    if not solveNQueens(board, 0, n):
        print("No solution exists.")
    else:
        print("Solutions printed above.")

# Solve the 8-Queens problem
nQueens(8)
