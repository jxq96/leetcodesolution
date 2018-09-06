class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        else:
            nums.sort()
            result = []
            result.append(nums.copy())
            end = [k for k in reversed(nums)]
            tmp = nums.copy()
            while True:
                if tmp == end:
                    break
                self.nextPermutation(tmp)
                result.append(tmp.copy())

            return result

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        for i in reversed(range(lenth)):
            if i > 0:
                if nums[i - 1] < nums[i]:
                    index = i
                    mini = nums[i]
                    flag = nums[i - 1]
                    for j in range(i, lenth):
                        if flag < nums[j] < mini:
                            mini = nums[j]
                            index = j
                    tmp = nums[i - 1]
                    nums[i - 1] = mini
                    nums[index] = tmp
                    nums[i:] = sorted(nums[i:])
                    return
            else:
                nums.reverse()
                return