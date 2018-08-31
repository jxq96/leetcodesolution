class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        i = 1
        while i < n:
            tmp = s
            s = ""
            lenth = len(tmp) - 1
            count = 1
            j = 0
            while j < lenth:
                if tmp[j] == tmp[j+1]:
                    count += 1
                else:
                    s += str(count)
                    s += tmp[j]
                    count = 1
                j += 1
            s += str(count)+tmp[j]
            i += 1
        return s