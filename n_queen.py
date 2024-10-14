def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if j >= n:
            break
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        print_board(board)  # Print the board configuration
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place the queen
            res = solve_n_queens_util(board, row + 1, n) or res
            board[row][col] = '.'  # Backtrack

    return res

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]  # Create an empty board
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists")

def main():
    n = int(input("Enter the number of queens (N): "))
    solve_n_queens(n)

if __name__ == "__main__":
    main()
