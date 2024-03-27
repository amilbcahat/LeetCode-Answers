# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #Left child -> 2 * ParentNodeVal  
        #Right child -> 2 * ParentNodeVal + 1
        #Awesome Solution #
        q = deque([(root , 1 )])
        res = 1 #At root level , width is one 
        while q: 
            levelSize = len(q)
            start = end = 0
            
            for i in range(levelSize ):
                node , val = q.popleft()
                
                if node.left : 
                    #index left child 
                    q.append((node.left , val * 2 ))
                if node.right : 
                    #index right child 
                    q.append((node.right , (val * 2 ) + 1))

                #Take leftmost and rightmost value at each level
                if i == 0 : 
                    start = val 
                elif i == levelSize  - 1 : 
                    end = val 

            res = max(end - start + 1, res)
            
        return res

        


