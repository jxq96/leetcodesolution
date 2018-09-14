class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = len(s) - 1
        while index >=0:
            if s[index] == " ":
                index -= 1
            else:
                break
        start = index
        while start >=0:
            if s[start] == " ":
                break
            else:
                start -= 1
        return index - start