# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        res = []
        totalSum = 0
        p1 = start = ListNode(-1)
        while cur : 
            if cur.val == 0 and totalSum != 0 :
                p1.next = ListNode(totalSum)
                p1 = p1.next
                totalSum = 0
            totalSum += cur.val 
            cur = cur.next  

        return start.next