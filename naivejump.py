class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        # I think this solution is really easy.
        # But TIME EXCEEDED
        dp = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            tmp = []
            for j in range(i):
                if nums[j] >= (i-j):
                    tmp.append(dp[j]+1)
            dp[i] = min(tmp)
        return dp[len(nums)-1]