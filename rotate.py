class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix) == 1:
            return
        else:
            row = len(matrix)
            for i in range(int(row / 2)):
                rowlen = row - 2*i - 1
                for j in range(i, i + rowlen):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[row - j - 1][i]
                    matrix[row - j - 1][i] = matrix[row - i - 1][row - j - 1]
                    matrix[row - i - 1][row - j - 1] = matrix[j][row - i - 1]
                    matrix[j][row - i - 1] = tmp

            return