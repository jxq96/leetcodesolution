class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        else:
            res = []
            rowlenth = len(matrix)
            collenth = len(matrix[0])
            end = ((min(rowlenth,collenth)+1) // 2)
            for i in range(end):
                res.extend([matrix[i][j] for j in range(i, collenth - i)])
                res.extend([matrix[j][collenth - i - 1]
                            for j in range(i + 1, rowlenth - i)])
                if rowlenth - i - 1 > i:
                    res.extend([matrix[rowlenth - i - 1][j]
                                for j in reversed(range(i, collenth - i - 1))])
                else:
                    break
                if i < collenth - i - 1:
                    res.extend([matrix[j][i]
                                for j in reversed(range(i + 1, rowlenth - i - 1))])
                else:
                    break

            return res