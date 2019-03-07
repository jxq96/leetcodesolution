class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        res.append([])
        flag = True
        length= len(nums)
        repeatSize = 0
        for i in range(length):
            size = len(res)
            if flag:
                for j in range(size):
                    tmp = res[j].copy()
                    tmp.append(nums[i])
                    res.append(tmp)
                if i + 1 < length:
                    if nums[i+1] == nums[i]:
                        flag = False
                        repeatSize = size
            else:
                for j in range(size-repeatSize, size):
                    tmp = res[j].copy()
                    if len(tmp)!=0:
                        tmp.append(nums[i])
                        res.append(tmp)
                if i + 1 < length:
                    if nums[i+1] != nums[i]:
                        flag = True
        return res