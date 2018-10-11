class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # referred from https://www.jianshu.com/p/ce80b4c07c22
        target_hash = dict()
        source_hash = dict()
        symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in symbol:
            target_hash[i] = 0
            source_hash[i] = 0
        for i in t:
            target_hash[i] += 1
        found = 0
        begin = -1
        end = len(s)
        minlen = len(s)
        start = 0
        targetlenth = len(t)
        for i in range(len(s)):
            source_hash[s[i]] += 1
            if source_hash[s[i]] <= target_hash[s[i]]:
                found += 1
            if found == targetlenth:
                while start < i and source_hash[s[start]] > target_hash[s[start]]:
                    source_hash[s[start]] -= 1
                    start += 1
                if i - start < minlen:
                    minlen = i - start
                    begin = start
                    end = i
                source_hash[s[start]] -= 1
                start += 1
                found -= 1
        if begin == -1:
            return ""
        else:
            return s[begin:end+1]