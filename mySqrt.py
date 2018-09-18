class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1000:
            y = 0
            while y <= x:
                tmp = y * y
                if tmp == x:
                    return y
                elif tmp < x < tmp + 2 * y + 1:
                    return y
                else:
                    y += 1
        else:
            low = 0
            high = x
            y = (low + high) // 2
            while True:
                tmp = y * y
                if tmp == x or tmp + 2 * y + 1 > x > tmp:
                    return y
                elif tmp > x:
                    high = y
                    y = (low + high) // 2
                else:
                    low = y
                    y = (low + high) // 2