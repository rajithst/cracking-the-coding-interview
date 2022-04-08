# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # check if given two trees are identical
        def dfs(n1, n2):

            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is None:
                return False
            if n1 is None and n2 is not None:
                return False
            # recursively check if current nodes are identical and then check if subtrees are identical
            return n1.val == n2.val and dfs(n1.left, n2.left) and dfs(n1.right, n2.right)

        # recursively check if subtree starting from any given two nodes are identical
        def check(t1, t2):
            if t1 is None:
                return False
            if t2 is None:
                return True
            if dfs(t1, t2):
                return True

            return check(t1.left, t2) or check(t1.right, t2)

        return check(root, subRoot)
