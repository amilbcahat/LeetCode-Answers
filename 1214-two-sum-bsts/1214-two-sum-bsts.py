# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        nodes1 = []
        nodes2 = []
        
        def dfs(root, arr):
            if not root:
                return None 

            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)

        dfs(root1, nodes1)
        dfs(root2, nodes2)

        print(nodes1, nodes2)

        for n in nodes1: 
            # for t in nodes2: 
            #     if (n + t) == target:
            #         return True
            l = 0 
            r = len(nodes2) - 1
            while l <= r:
                mid = (l + r) // 2
                if nodes2[mid] + n == target:
                    return True 
                elif target > nodes2[mid] + n: 
                    l = mid + 1
                else:
                    r = mid - 1

        return False

        
            