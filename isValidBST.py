class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.recursion(root.left, float("-inf"), root.val) and self.recursion(root.right, root.val, float("inf"))

    def recursion(self, node:TreeNode, lowerbound, upperbound) -> bool:
        if node is None:
            return True
        else:
            if node.val <= lowerbound or node.val >= upperbound:
                return False
            else:
                return self.recursion(node.left, lowerbound, node.val) and self.recursion(node.right, node.val, upperbound)