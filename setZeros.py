class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        else:
            rows = set()
            cols = set()
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        rows.add(i)
                        cols.add(j)
            for i in range(len(matrix)):
                for t in cols:
                    matrix[i][t] = 0
            for i in range(len(matrix[0])):
                for t in rows:
                    matrix[t][i] = 0