class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        p = root
        stack = []
        res = []
        while p is not None or len(stack) != 0:
            while p is not None:
                stack.append(p)
                p = p.left
            if len(stack) != 0:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return resP