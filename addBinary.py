class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)
        c = [0 for _ in range(max(lenb, lena)+1)]
        lenaminuslenb = lena - lenb
        if lenaminuslenb > 0:
            while lenaminuslenb > 0:
                b = "0" + b
                lenaminuslenb -= 1
        elif lenaminuslenb < 0:
            while lenaminuslenb < 0:
                a = "0" + a
                lenaminuslenb += 1
        for i in range(len(a)):
            c[i+1] = int(a[i]) + int(b[i])
        for i in reversed(range(1, len(c))):
            if c[i] > 1:
                c[i-1] += c[i] // 2
                c[i] = c[i] % 2
        if c[0] == 0:
            c = c[1:]
        res = ""
        for i in c:
            res += str(i)
        return res