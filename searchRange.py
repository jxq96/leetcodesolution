class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = end = self.semifind(nums,target)
        if start == -1:
            return [-1, -1]
        else:
            while start > 0 and nums[start-1] == target:
                start -= 1
            lenth = len(nums) - 1
            while end < lenth and nums[end+1] == target:
                end += 1
            return [start, end]

    def semifind(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1