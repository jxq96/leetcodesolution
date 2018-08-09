class Solution:
    def magicalString(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            s = "122"
            index = 2
            tmplen = len(s)
            while tmplen < n:
                length = tmplen - 1
                ch = s[length]
                if s[index] == "1":
                    if ch == "1":
                        s += "2"
                    else:
                        s +="1"
                else:
                    if ch == "1":
                        s += 2*"2"
                    else:
                        s +=2*"1"
                index += 1
                tmplen = len(s)

            num = s[:n].count('1')
            print(s[:n])
            return num
