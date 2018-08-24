class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this solution is referred from
        # https://blog.csdn.net/pengjian444/article/details/79737141
        stack = []
        tmp = [0] * len(s)
        for (i,c) in enumerate(s):
            if c == ")":
                if len(stack) == 0:
                    stack.append((c, i))
                else:
                    if stack[-1][0] == "(":
                        element = stack.pop()
                        tmp[element[1]] = 1
                        tmp[i] = 1
                    else:
                        stack.append((c, i))
            else:
                stack.append((c, i))
        maxcount = 0
        count = 0
        for i in tmp:
            if i == 0:
                count = 0
            else:
                count += 1
                if count > maxcount:
                    maxcount = count
        return maxcount