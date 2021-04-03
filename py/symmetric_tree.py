class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:

        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        
        return recur(root.left, root.right) if root else True