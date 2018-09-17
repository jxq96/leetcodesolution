class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 1
        else:
            a = m + n - 2
            b = min(m, n) - 1
            frac1 = 1
            frac2 = 1
            while b > 0:
                frac1 *= a
                frac2 *= b
                a -= 1
                b -= 1
            return frac1 // frac2