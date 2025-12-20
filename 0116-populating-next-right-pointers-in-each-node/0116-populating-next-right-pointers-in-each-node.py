"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #nxt here means nxt level to start from!

        cur, nxt = root, root.left if root else None 
        while cur and nxt: 
            cur.left.next = cur.right

            if cur.next: 
                cur.right.next = cur.next.left

            cur = cur.next 
            if not cur: 
                cur = nxt
                nxt = cur.left 

        return root

        # q = deque([root])

        # while q: 
        #     size = len(q)
        #     for i in range(len(q)): 
        #         node = q.popleft()
                
        #         if i < size - 1: 
        #         # This check is important. We don't want to
        #         # establish any wrong connections. The queue will
        #         # contain nodes from 2 levels at most at any
        #         # point in time. This check ensures we only
        #         # don't establish next pointers beyond the end
        #         # of a level
        #             node.next = q[0]

        #         if node and node.left : 
        #             q.append(node.left)
        #         if node and node.right: 
        #             q.append(node.right)

        # return root