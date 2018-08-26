class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        index, flag = self.semifind(nums, target)
        if flag:
            return index
        else:
            if nums[index] > target:
                return index
            else:
                return index + 1

    def semifind(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid, True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return mid, False