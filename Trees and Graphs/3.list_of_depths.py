# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # define a queue and a list to store the results
        # if the root is None, return an empty list
        # otherwise, add the root to the queue
        # while the queue is not empty:
        # perform a level order traversal, and add the result to the list
        # time complexity: O(n) where n is the number of nodes in the tree
        # space complexity: O(n) where n is the number of nodes in the tree
        results = []
        if not root:
            return results

        q = deque()
        q.append(root)

        while q:

            level_length = len(q)
            level_arr = []

            for _ in range(level_length):
                node = q.popleft()
                level_arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            results.append(level_arr)
        return results
