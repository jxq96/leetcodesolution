class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # recursion solution is TIME EXCEEDED.
        len1 = len(s)
        len2 = len(p)
        if len2 == 0:
            return len1 == 0
        elif len2 == 1:
            if p[0] == "*":
                return True
            elif p[0] == "?":
                return len1 == 1
            else:
                return len1 == 1 and p[0] == s[0]
        else:
            if p[0] != "*":
                if len1 == 0:
                    return False
                else:
                    return (s[0] == p[0] or p[0] == "?") and self.isMatch(s[1:], p[1:])
            else:
                tmp = s
                while len(tmp) > 0:
                    if self.isMatch(tmp, p[1:]):
                        return True
                    else:
                        tmp = tmp[1:]
                return self.isMatch(s, p[1:])