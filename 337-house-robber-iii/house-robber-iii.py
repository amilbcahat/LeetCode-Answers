# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #Two Directly linked means , cant be parent or child of parent 

        def dfs(node):
            if not node : 
                return [0 , 0]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            #At index 1 , contains value withoutRoot thats why we take that according to condition in the problem 
            withRoot = node.val + leftPair[1] + rightPair[1]
            #Max Of both children (containing tuples of both cases)
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot , withoutRoot] #Pair returning 

        return max(dfs(root))
            