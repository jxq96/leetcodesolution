class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this O(n) solution is referred from
        #  https://blog.csdn.net/Jaster_wisdom/article/details/80662037
        dp = nums.copy()
        maxsum = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + dp[i]
            if dp[i] > maxsum:
                maxsum = dp[i]
        return maxsum