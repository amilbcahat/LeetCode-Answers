# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        def recur_remove(cur_node): 
            if cur_node: 
                recur_remove(cur_node.next)

                if cur_node.next and cur_node.next.val == val: 
                    cur_node.next = cur_node.next.next

                return cur_node
            
            return None
        recur_remove(dummy)

        return dummy.next