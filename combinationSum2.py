class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.anslist = []
        self.DFS(candidates, target, 0, [])
        return Solution.anslist

    def DFS(self, candidates, target, start, valuelist):
        if target == 0:
            if valuelist not in Solution.anslist:
                return Solution.anslist.append(valuelist)
            else:
                return Solution.anslist
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target -
                     candidates[i], i+1, valuelist +
                     [candidates[i]])