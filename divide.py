class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1 :
            return 2**31 - 1
        else:
            m = abs(dividend)
            n = abs(divisor)
            sign = 1
            if dividend >= 0 and divisor < 0 or dividend < 0 and divisor >0:
               sign = -1
            if n == 1:
                if sign == 1:
                    return m
                else:
                    return  -m
            else:
                result = 0
                while m >= n:
                    t = n
                    p = 1
                    while m >= t<<1:
                        t = t << 1
                        p = p << 1
                    result = result + p
                    m = m - t
                if sign == 1:
                    return result
                else:
                    return -result