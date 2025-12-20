# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)

        #idea is to map the serialized string value of tree to the root of that serialization order
        #We can use any traversal here , but we use Preorder here 
        def dfs(node):
            if not node: 
            #Null value are actually whats important , to distinguish two subtress having same nodes , but different 
            #pathways !
                return "null"
            s = ",".join([str(node.val) , dfs(node.left) , dfs(node.right)])

            #The first duplicate entry is stored in the result 
            if len(subtrees[s]) == 1:
                res.append(node)

            #We map the serialized order to its node 
            subtrees[s].append(node)
            #Return the so far , serialized order 
            return s 

        res = []
        dfs(root)
        return res 