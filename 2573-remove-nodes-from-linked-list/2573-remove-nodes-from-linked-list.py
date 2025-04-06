# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Use Monotonic Stack 
        dummy = ListNode(-1)

        stack = []
        cur = head 

        while cur: 
            while stack and stack[-1] < cur.val :
                stack.pop()
            stack.append(cur.val)
            cur = cur.next 

        p1 = dummy
        for node in stack:
            node = ListNode(node)
            p1.next = node
            p1 = p1.next

        return dummy.next