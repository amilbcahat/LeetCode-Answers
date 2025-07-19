# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None: 
            return l2 
        elif l2 is None: 
            return l1
        elif l2.val < l1.val: 
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else: 
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
