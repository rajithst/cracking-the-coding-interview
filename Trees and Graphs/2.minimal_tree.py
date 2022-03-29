# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # minimal height means, the tree is balanced
        # since array is sorted, we can use the middle element as the root.
        # then we can divide the array into left and right sub-arrays
        # and recursively build the left and right subtrees.
        # Time Complexity: O(n) where n is the length of the array
        # Space Complexity: O(n) where n is the length of the array.

        def dfs(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)
            return root

        return dfs(0, len(nums) - 1)
