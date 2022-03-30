# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursively check if the tree is a valid BST
        # Time Complexity: O(n)
        def dfs(node, upper, lower):
            if not node:
                return True
            # if the node is not in the range, return False
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, node.val, lower) and dfs(node.right, upper, node.val)

        return dfs(root, float("inf"), float("-inf"))
