class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        a = [i for i in range(1, n+1)]
        res = []
        for i in range(1, n+1):
            fac = math.factorial(n - i)
            mod = k % fac
            index = k // fac
            if mod != 0:
                res.append(str(a[index]))
                a.remove(a[index])
            else:
                res.append(str(a[index-1]))
                a.remove(a[index-1])
            k = mod
        return "".join(res)