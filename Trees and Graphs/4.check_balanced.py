# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if not left_height[0] or not right_height[0]:
                return [False, 0]
            diff = abs(left_height[1] - right_height[1])
            if diff > 1:
                return [False, 0]
            return [True, max(left_height[1], right_height[1]) + 1]

        v = dfs(root)
        return v[0]
