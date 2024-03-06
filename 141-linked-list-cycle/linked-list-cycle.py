# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head 
        second = head 

        while first and second and first.next : 
            first = first.next.next
            second = second.next 
            if (first == second):
                return True

        return False 
