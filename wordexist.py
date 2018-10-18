class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False
        else:
            flag = [[False for _ in range(len(board[0]))]
                    for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        flag[i][j] = True
                        if self.search(board, word, flag, 1, i, j):
                            return True
                        else:
                            flag[i][j] = False
            return False

    def search(self, board, word, flag, index, i, j):
        if index == len(word):
            return True
        else:
            if i > 0 and flag[i -
                              1][j] == False and board[i -
                                                       1][j] == word[index]:  # can go up
                flag[i - 1][j] = True
                if self.search(board, word, flag, index + 1, i - 1, j):
                    return True
                else:
                    flag[i - 1][j] = False
            if j + 1 < len(board[0]) and flag[i][j +
                                                 1] == False and board[i][j + 1] == word[index]:  # can go right
                flag[i][j + 1] = True
                if self.search(board, word, flag, index + 1, i, j + 1):
                    return True
                else:
                    flag[i][j + 1] = False
            if j > 0 and flag[i][j -
                                 1] == False and board[i][j -
                                                          1] == word[index]:  # can go left
                flag[i][j - 1] = True
                if self.search(board, word, flag, index + 1, i, j - 1):
                    return True
                else:
                    flag[i][j - 1] = False
            if i + \
                    1 < len(board) and flag[i + 1][j] == False and board[i + 1][j] == word[index]:  # can go down
                flag[i + 1][j] = True
                if self.search(board, word, flag, index + 1, i + 1, j):
                    return True
                else:
                    flag[i + 1][j] = False
            return False