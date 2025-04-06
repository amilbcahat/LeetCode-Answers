# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Most Efficient !!
        #Traverse right to left by maintaining a max 
        #and check if curmax has been beaten , then add, else keep removing , less nodes
        #The main intuition is when we go from left to right , we dont know whats at right of node to compare, but when we go from right to left , we know what is at right 

        def reverse(head):
            prev , cur = None, head
            while cur: 
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp

            return prev

        
        rhead  = reverse(head)
        cur_max = rhead.val
        cur = rhead
        while cur.next: 
            if cur_max > cur.next.val: 
                cur.next = cur.next.next
            else : 
                cur_max = cur.next.val
                cur = cur.next 

        return reverse(rhead)


        #We used a space and also a new LinkedList 
        #That we will improve here
        # stack = []
        # # Stack + LinkedList Nodes Patterns
        # cur = head
        # while cur : 
        #     while stack and stack[-1].val < cur.val:
        #         stack.pop()
            
        #     if stack: 
        #         stack[-1].next = cur 
        #     stack.append(cur)
        #     cur = cur.next 

        # return stack[0] if stack else None

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