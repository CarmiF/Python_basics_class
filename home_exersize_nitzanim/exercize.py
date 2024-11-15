def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # בדיקה אם המספר כבר קיים בשורה
        for i in range(4):
            if board[row][i] == num:
                return False
        # בדיקה אם המספר כבר קיים בעמודה
        for i in range(4):
            if board[i][col] == num:
                return False
        # בדיקה אם המספר כבר קיים בתת לוח (2x2)
        subgrid_row, subgrid_col = 2 * (row // 2), 2 * (col // 2)
        for i in range(subgrid_row, subgrid_row + 2):
            for j in range(subgrid_col, subgrid_col + 2):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        for row in range(4):
            for col in range(4):
                if board[row][col] is None:  # תא ריק
                    for num in range(1, 5):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = None  # Undo
                    return False
        return True

    solve(board)
    return board
