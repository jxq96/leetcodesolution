class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        num = len(board)
        for i in range(num):
            for j in range(num):
                if board[i][j] == '.':
                    for t in range(1, 10):
                        c = str(t)
                        if self.is_valid(board, c, i, j):
                            board[i][j] = c
                            if self.dfs(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board, c, row, col):
        num = len(board)
        # check row
        for m in range(num):
            if board[row][m] == c:
                return False

        # check column
        for n in range(num):
            if board[n][col] == c:
                return False

        # check block
        row_start = int(row / 3) * 3
        column_start = int(col / 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(column_start, column_start + 3):
                if board[i][j] == c:
                    return False
        return True