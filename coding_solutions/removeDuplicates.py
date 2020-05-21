"""
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        if cur:
            while cur.next:

                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next

        return head