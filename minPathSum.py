class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        else:
            dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            dp[0][0] = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if i == 0 and j > 0:
                        dp[i][j] = dp[i][j-1]+grid[i][j]
                    elif j == 0 and i > 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    elif i != 0 and j != 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            return dp[len(grid)-1][len(grid[0])-1]