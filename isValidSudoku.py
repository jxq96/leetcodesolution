class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = sorted([board[i][j],
                              board[i][j + 1],
                              board[i][j + 2],
                              board[i + 1][j],
                              board[i + 1][j + 1],
                              board[i + 1][j + 2],
                              board[i + 2][j],
                              board[i + 2][j + 1],
                              board[i + 2][j + 2]])
                tmp.reverse()
                for k in range(8):
                    if tmp[k] == ".":
                        break
                    else:
                        if tmp[k] == tmp[k + 1]:
                            return False
        for i in range(9):
            for j in range(9):
                tmp = []
                itmp = i
                jtmp = j
                while jtmp < 9:
                    tmp.append(board[itmp][jtmp])
                    jtmp += 1
                tmp.sort()
                tmp.reverse()
                for k in range(len(tmp) - 1):
                    if tmp[k] == ".":
                        break
                    else:
                        if tmp[k] == tmp[k + 1]:
                            return False
                tmp = []
                jtmp = j
                while itmp < 9:
                    tmp.append(board[itmp][jtmp])
                    itmp += 1
                tmp.sort()
                tmp.reverse()
                for k in range(len(tmp) - 1):
                    if tmp[k] == ".":
                        break
                    else:
                        if tmp[k] == tmp[k + 1]:
                            return False
        return True