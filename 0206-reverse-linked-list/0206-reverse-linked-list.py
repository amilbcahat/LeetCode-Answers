# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursion
        if not head: 
            return None

        root = head
        newHead = None
        def dfs(node): 
            nonlocal root, newHead
            if not node: 
                return None 

            print(node.val)
            child = dfs(node.next)

            if child: 
                child.next = node
            else: 
                newHead = node
            
            if node == root: 
                root.next = None

            return node

        dfs(root)
        # return head
        return newHead

