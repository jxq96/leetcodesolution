class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # this solution remains to be completed
        # it's not hard but tedious
        count = []
        tmp = 0
        start = 0
        res = []
        for i in words:
            if start + len(i) + 1 <= maxWidth:
                tmp += 1
                start += len(i) + 1
            elif start + len(i) == maxWidth:
                tmp += 1
                count.append(tmp)
                start = 0
                tmp = 0
            else:
                count.append(tmp)
                tmp = 1
                start = len(i) + 1
        if 0 < start <= maxWidth:
            count.append(tmp)
        m = 0
        n = 0
        for i in range(len(count)):
            width = 0
            for j in range(count[i]):
                width += len(words[k])
                m += 1
            tmp1 = (maxWidth-width) % count[i]
            tmp2 = (maxWidth-width)//count[i]
            tmpstring = ""
            for k in range(count[i]):
                tmpstring += words[n]
                n += 1
                if k < tmp1:
                    tmp3 = " "*(tmp2+1)
                    tmpstring += tmp3
                else:
                    tmp3 = " "*tmp2
                    tmpstring += tmp3
            res.append(tmpstring)

        return res