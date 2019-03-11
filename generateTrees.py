class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [0 for _ in range(n+1)]
            dp[0] = 1
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n+1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1]*dp[i-j]
            return dp[n]

    def generateTrees(self, n: int) -> [TreeNode]:
        if n == 0:
            return []
        else:
            nodes = [i+1 for i in range(n)]
            return self.recur(nodes)

    def recur(self, nodes: [int]) -> [TreeNode]:
        if len(nodes) == 0:
            return [None]
        else:
            res = []
            for i in range(len(nodes)):
                tmp = nodes[i]
                tmpres1 = self.recur(nodes[0:i])
                tmpres2 = self.recur(nodes[i+1:])
                for left in tmpres1:
                    for right in tmpres2:
                        tmpnode = TreeNode(tmp)
                        tmpnode.left = left
                        tmpnode.right = right
                        res.append(tmpnode)
            return res