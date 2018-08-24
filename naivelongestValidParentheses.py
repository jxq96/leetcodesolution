class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenth = len(s)
        for i in reversed(range(lenth)):
            j = lenth - i
            for k in range(j):
                if self.isParentheses(s[k:k + i + 1]):
                    return i + 1
        return 0

    def isParentheses(self, s):
        if s == "":
            return True
        elif s[0] == ")":
            return False
        else:
            l = []
            l.append(s[0])
            for character in s[1:]:
                if character == "(":
                    l.append("(")
                else:
                    lenth = len(l)
                    if lenth == 0:
                        return False
                    else:
                        if l[lenth - 1] == "(":
                            l.pop(lenth - 1)
                        else:
                            l.append(")")
            return len(l) == 0