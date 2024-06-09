# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive 
        def dfs(cur , prev):
            if cur is None : 
                return prev 

            else : 
                nxt = cur.next 
                cur.next = prev 
                return dfs(nxt , cur)

        return dfs(head , None)
        # Iterative 
        # prev = None 
        # cur = head  

        # #Just notice the ordering 
        # # 1. Cur moves forward
        # # 2. Temp.next = prev
        # # 3 .Prev increments by equalling to temp  ! 

        # while cur : 
        #     temp = cur 
        #     cur = cur.next 
        #     temp.next = prev 
        #     prev = temp 
        
        # return prev 

