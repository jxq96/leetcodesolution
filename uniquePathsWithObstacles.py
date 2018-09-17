class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        rowlen = len(obstacleGrid)
        collen = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp = [0 for _ in range(collen)]
            dp[0] = 1
            for i in range(rowlen):
                for j in range(collen):
                    if obstacleGrid[i][j] == 1:
                        dp[j] = 0
                    elif j > 0:
                        dp[j] += dp[j-1]
            return dp[collen-1]