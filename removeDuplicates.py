class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth = len(nums)
        if lenth == 0:
            return 0
        else:
            tmp = nums[lenth-1]
            index = lenth - 2
            while index >= 0:
                if nums[index] == tmp:
                    nums.remove(tmp)
                    index = index - 1
                else:
                    break
            i = 0
            j = 1
            while nums[i] != tmp:
                if nums[j] == nums[i]:
                    nums.remove(nums[j])
                else:
                    i = j
                    j = j + 1
            return len(nums)