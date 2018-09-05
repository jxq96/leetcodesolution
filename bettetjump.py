class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This solution is better than the naivejump function
        # but still TIME EXCEEDED
        dp = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            k = 0
            count = 0
            tmp = dp[i-1]
            for t in reversed(range(i)):
                if dp[t] != tmp:
                    count += 1
                    tmp = dp[t]
                    if count == 2:
                        k = t
                        break
            mini = 10000  # just let it a big number
            for j in reversed(range(k, i)):
                if nums[j] >= (i - j):
                    if dp[j] + 1 < mini:
                        mini = dp[j] + 1
            dp[i] = mini
        return dp[len(nums) - 1]