# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, cur: Optional[ListNode]) -> Optional[ListNode]:
        if not cur: 
            return None
        if not cur.next: 
            return cur 

        next_node = cur.next
        next_start = next_node.next 
        next_node.next = cur 
        cur.next = self.swapPairs(next_start)
        return next_node