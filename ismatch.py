class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Dynamic Programing
        dp = [[False for col in range(len(s) + 1)]for row in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            pchar = p[i-1]
            dp[i][0] = dp[i-1][0] and pchar == "*"
            for j in range(1,len(s)+1):
                schar = s[j-1]
                if pchar == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and(pchar == "?" or pchar == schar)

        return dp[len(p)][len(s)]