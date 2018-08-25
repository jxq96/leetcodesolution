class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        axis = self.findaxis(nums)
        if axis is None:
            if len(nums) == 0:
                return -1
            else:
                if target > nums[-1] or target < nums[0]:
                    return -1
                else:
                    return self.semifind(nums,target)
        else:
            if target >= nums[0]:
                return self.semifind(nums[0:axis+1], target)
            else:
                tmp = self.semifind(nums[axis+1:], target)
                if tmp == -1:
                    return -1
                else:
                    return tmp + axis + 1

    def semifind(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def findaxis(self, nums):
        lenth = len(nums)
        if lenth == 0:
            return None
        else:
            flag = nums[0]
            low = 0
            high = lenth - 1
            j = int((low + high) / 2)
            while low < high:
                if low < j < high:
                    if nums[j] > nums[j + 1] and nums[j] > nums[j - 1]:
                        return j
                    else:
                        if nums[j] > flag:
                            low = j
                            j = int((low + high) / 2)
                        else:
                            high = j
                            j = int((low + high) / 2)
                elif j == low:
                    if nums[j] > nums[j + 1]:
                        return j
                    else:
                        j = int((low + high) / 2)
                        if j == low:
                            break
                else:
                    if nums[j] < nums[j - 1]:
                        return j - 1
                    else:
                        j = int((low + high) / 2)
                        if j == high:
                            break