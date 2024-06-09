# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        cur = head  

        #Just notice the ordering 
        # 1. Cur moves forward
        # 2. Temp.next = prev
        # 3 .Prev increments by equalling to temp  ! 

        while cur : 
            temp = cur 
            cur = cur.next 
            temp.next = prev 
            prev = temp 
        
        return prev 