# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque([(root,None)])

        #Logic is to at each level , do the levelSum - siblingSum
        
        while q : 
            childSumMap = defaultdict(int)  #parent to its childSum
            parentMap = {} #node to its parent
            curLevelSum = 0 
            for i in range(len(q)):
                node , parent = q.popleft()
                childSumMap[parent] += node.val 
                parentMap[node] = parent
                curLevelSum += node.val
                if node and node.right :     
                    q.append((node.right ,node))
            
                if node and node.left:
                    q.append((node.left,node))

            for node in parentMap:
                #This loop updates for each node in that level ! 
                node.val = curLevelSum - childSumMap[parentMap[node]]
                #childSum[parentofNode]
                #childSum ! 


        return root