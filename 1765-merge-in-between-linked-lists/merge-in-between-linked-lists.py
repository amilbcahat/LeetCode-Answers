# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        count = 0 
        first = list1 
        while first and first.next and count != (a - 1): 
            first = first.next
            count += 1 

        count = 0 
        second = list1
        while second and second.next and count != (b): 
            second = second.next
            count += 1 

        first.next = list2

        p1 = list2 
        while p1 and p1.next: 
            p1 = p1.next 

        p1.next = second.next

        return list1