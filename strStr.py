class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "":
            if needle == "":
                return 0
            else:
                return -1
        if needle == "":
            return 0
        lenth = len(haystack)
        cmplen = len(needle)
        tmp = needle[0]
        for i in range(lenth):
            if haystack[i] == tmp:
                if haystack[i:i+cmplen] == needle:
                    return i
        return -1