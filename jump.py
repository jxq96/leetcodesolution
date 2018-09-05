class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy Algorithm
        # referred from https://blog.csdn.net/evan123mg/article/details/46874705
        result = 0
        curreach = 0
        maxreach = 0
        for i in range(len(nums)):
            if curreach < i:
                result += 1
                curreach = maxreach
            maxreach = max(maxreach, nums[i]+i)
        return result