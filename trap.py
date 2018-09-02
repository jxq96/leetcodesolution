class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # this solution is referred from
        # https://www.cnblogs.com/felixfang/p/3713197.html
        lenth = len(height)
        if lenth <= 2:
            return 0
        else:
            maxheight = max(height)
            maxindex = height.index(maxheight)
        water = 0
        root = height[0]
        for i in range(maxindex):
            if root < height[i]:
                root = height[i]
            else:
                water += (root - height[i])
        root = height[lenth-1]
        for i in reversed(range(maxindex,lenth)):
            if root < height[i]:
                root = height[i]
            else:
                water += (root - height[i])
        return water