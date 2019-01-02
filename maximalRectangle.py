class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        else:
            res = 0
            row = len(matrix)
            col = len(matrix[0])
            L = [0 for _ in range(col)]
            R = [col for _ in range(col)]
            H = [0 for _ in range(col)]
            for i in range(row):
                j = 0
                while j < col:
                    if matrix[i][j] == "1":
                        left = j
                        k = j + 1
                        while k < col and matrix[i][k] == "1":
                            k += 1
                        right = k
                        for k in range(left, right):
                            L[k] = max(L[k], left)
                            R[k] = min(R[k], right)
                            H[k] += 1
                            if (R[k] - L[k]) * H[k] > res:
                                res = (R[k] - L[k]) * H[k]
                        j = right - 1
                    else:
                        L[j] = 0
                        R[j] = col
                        H[j] = 0
                    j += 1
            return res