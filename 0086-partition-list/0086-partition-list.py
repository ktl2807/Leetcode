# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        greater = ListNode(0)
        smaller = ListNode(0)
        g = greater
        s = smaller

        while head:
            if head.val >= x:
                greater.next = head
                greater = greater.next
            else:
                smaller.next = head
                smaller = smaller.next
            head = head.next
        smaller.next = g.next
        greater.next = None
        return s.next