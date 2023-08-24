# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        greater = deque([])
        smaller = deque([])
        dummy = newList = ListNode(0)
        
        while head:
            if head.val >= x:
                greater.append(head)
            else:
                smaller.append(head)
            head = head.next
        if smaller:
            newList.next = smaller[0]
        else:
            newList.next = greater[0]
        
        newList = newList.next
        dummy.next = pre = newList
        for i in range(1, len(smaller)):
            
            newList.next = smaller[i]
            newList = newList.next
        
        for i in greater:
            newList.next = i
            newList = newList.next
        newList.next = None
        return dummy.next
