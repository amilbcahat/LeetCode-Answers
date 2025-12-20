# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Iterator:
    def __init__(self, root):
        self.stack = []
        while root: 
            self.stack.append(root)
            root = root.left

    def next(self):
        pop = self.stack.pop()
        ans = pop
        if pop.right:
            pop = pop.right
            while pop:
                self.stack.append(pop)
                pop = pop.left
        return ans.val

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = Iterator(root)
        while k: 
            elem = inorder.next()
            k -= 1 

        return elem

        

        # res = None
        # def inorder(node) : 
        #     nonlocal k 
        #     nonlocal res
        #     if not node : 
        #         return 
            
        #     inorder(node.left)
        #     k -= 1 
        #     if k == 0 : 
        #         res = node.val
        #         print(node)
        #         return 
        #     inorder(node.right)

        # inorder(root)

        # print(res)
        # return res