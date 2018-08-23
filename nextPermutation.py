class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        for i in reversed(range(lenth)):
            if i > 0:
                if nums[i-1] < nums[i]:
                    index = i
                    mini = nums[i]
                    flag = nums[i-1]
                    for j in range(i,lenth):
                        if flag < nums[j] < mini :
                            mini = nums[j]
                            index = j
                    tmp = nums[i-1]
                    nums[i-1] = mini
                    nums[index] = tmp
                    nums[i:] = sorted(nums[i:])
                    return
            else:
                nums.reverse()
                return