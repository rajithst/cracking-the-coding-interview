"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        # If node has right subtree, then the successor is the leftmost node of the right subtree
        # If node has no right subtree, then the successor is the first ancestor of node that is a left child
        # Time Complexity: O(h) where h is the height of the tree
        # Space Complexity: O(1)
        def get_left_most_child(node):
            current = node
            while current.left:
                current = current.left
            return current

        # if given node doesn't have a right child
        # next node should visit is,first parent node that came to current node using a left branch
        def get_right_most_parent(node):
            current = node
            while current.parent and current.parent.right == current:
                current = current.parent
            return current.parent

        if node.right:
            return get_left_most_child(node.right)
        return get_right_most_parent(node)