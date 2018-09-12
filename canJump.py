class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach = nums[0]
        lenth = len(nums) - 1
        for i in range(len(nums)):
            if maxreach < i:
                return False
            elif maxreach >= lenth:
                return True
            else:
                if i + nums[i] > maxreach:
                    maxreach = i + nums[i]
        return maxreach >= lenth