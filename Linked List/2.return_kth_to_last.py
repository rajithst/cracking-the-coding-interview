# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the length of linked list
        linked_list_len = 0
        root = head
        while root:
            root = root.next
            linked_list_len += 1

        # if linked list length is one and n is 1, return None
        if linked_list_len == 1 and n == 1:
            return None

        # check how many nodes should visit,before remove the nth node
        # if nth node is head node,modify head and return new linked list
        process_count = linked_list_len - n
        if process_count == 0:
            head = head.next
            return head

        # otherwise,traverse till nth node
        prev = None
        current = head
        for _ in range(process_count):
            prev = current
            if current.next:
                current = current.next

        # if nth node has next node (which means not tail node)
        # remove nth node by change previous node's pointer
        # otherwise make previous node's pointer to None
        if current.next:
            prev.next = current.next
        else:
            prev.next = None
        return head
