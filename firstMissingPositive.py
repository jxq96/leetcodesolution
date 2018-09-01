class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this method does not satisfy the requirements
        # because this method has O(nlogn) time complexity
        nums.sort()
        i = 0
        lenth = len(nums)
        # skip all non-positive numbers
        while i < lenth and nums[i]<=0:
            i += 1
        marker = 1
        lenth -= 1
        while i < lenth:
            if marker != nums[i]:
                return marker
            else:
                i += 1
                if nums[i] != marker:
                    marker += 1
        if marker == nums[lenth]:
            return marker + 1
        else:
            return marker