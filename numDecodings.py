class Solution:
    def numDecodings(self, s: str) -> int:
        lengh = len(s)
        if lengh == 0 or s[0] == "0":
            return 0
        else:
            dp = [1 for _ in range(lengh)]
            dp[0] = 1
            for i in range(1, lengh):
                if s[i] == "0":
                    if "1" <= s[i-1] <= "2":
                        if i >= 2:
                            dp[i] = dp[i-2]
                        else:
                            dp[i] = 1
                    else:
                        return 0
                else:
                    if s[i-1] == "1" or s[i-1] == "2" and s[i] <= "6":
                        dp[i] = dp[i-1] + 1
                        if i >= 2:
                            dp[i] = dp[i] + dp[i-2] - 1
                    else:
                        dp[i] = dp[i-1]
            return dp[lengh-1]