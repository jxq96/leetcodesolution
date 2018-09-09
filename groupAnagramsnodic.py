class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # the solution is accepted, but it is really
        # not efficient
        res = []
        comp = []
        for str in strs:
            tmp = sorted(str)
            if tmp in comp:
                res[comp.index(tmp)].append(str)
            else:
                comp.append(tmp)
                res.append([str])
        return res