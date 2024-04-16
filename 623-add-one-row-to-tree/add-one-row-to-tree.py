# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #For Edge Case 
        dummy = TreeNode(val)
        if depth == 1 : 
            dummy.left = root 
            return dummy 
            

        def dfs(cur , d):
            if not cur : 
                return None 

            if d == depth - 1:
                #Add a row 
                tmpRight = cur.right 
                tmpLeft = cur.left 
                cur.right = TreeNode(val)
                cur.left = TreeNode(val)
                cur.right.right = tmpRight
                cur.left.left = tmpLeft 

            else : 
                cur.left = dfs(cur.left , d + 1)
                cur.right = dfs(cur.right , d + 1)

            return cur 

        return dfs(root , 1)