class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        count = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                if count == 2:
                    nums.remove(nums[index])
                else:
                    count += 1
                    index += 1
            else:
                count = 1
                index += 1
        return len(nums)