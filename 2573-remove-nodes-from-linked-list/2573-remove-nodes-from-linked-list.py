# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #We used a space and also a new LinkedList 
        #That we will improve here
        stack = []
        # Stack + LinkedList Nodes Patterns
        cur = head
        while cur : 
            while stack and stack[-1].val < cur.val:
                stack.pop()
            
            if stack: 
                stack[-1].next = cur 
            stack.append(cur)
            cur = cur.next 

        return stack[0] if stack else None

        #Naive use Monotonic Stack 
        # dummy = ListNode(-1)

        # stack = []
        # cur = head 

        # while cur: 
        #     while stack and stack[-1] < cur.val :
        #         stack.pop()
        #     stack.append(cur.val)
        #     cur = cur.next 

        # p1 = dummy
        # for node in stack:
        #     node = ListNode(node)
        #     p1.next = node
        #     p1 = p1.next

        # return dummy.next