class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        end = (n+1) // 2
        now = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(end):
            for j in range(i, n-i):
                res[i][j] = now
                now += 1
            for j in range(i+1, n-i):
                res[j][n-i-1] = now
                now += 1
            if n - i - 1 > i:
                for j in reversed(range(i, n-i-1)):
                    res[n-i-1][j] = now
                    now += 1
                for j in reversed((range(i+1, n - i - 1))):
                    res[j][i] = now
                    now += 1
            else:
                break
        return res