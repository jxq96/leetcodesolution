class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        i = 0
        j = lenth
        for t in nums:
            if t == 0:
                i += 1
            elif t == 2:
                j -= 1
        for k in range(0, i):
            nums[k] = 0
        for k in range(j, lenth):
            nums[k] = 2
        for k in range(i, j):
            nums[k] = 1