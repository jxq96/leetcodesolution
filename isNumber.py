class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # referred from https://zhuanlan.zhihu.com/p/20042325
        try:
            float(s.strip())
            return True
        except:
            return False
        