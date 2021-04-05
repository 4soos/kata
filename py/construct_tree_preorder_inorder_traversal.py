from typing import List

class TreeNode:

    def __init__(self, val: int = None, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def build_tree_recursion(self, preoder: List[int], inorder: List[int]) -> TreeNode:

        def help(preoder, inorder) -> TreeNode:
            if not preoder: return TreeNode(val=None, left=None, right=None)

            # get root node and it's index in inorder
            root = TreeNode(preoder[0])
            root_idx = inorder.index(root.val)
            
            # divid
            root.left = help(preoder=preoder[1:root_idx], inorder=inorder[0:root_idx])
            root.right = help(preoder=preoder[root_idx+1:], inorder=inorder[root_idx+1:])

            return root

        return help(preoder, inorder)

    def build_tree_(self, preoder: List[int], inorder: List[int]) -> TreeNode:

        root = TreeNode(val=None, left=None, right=None)

        return root
