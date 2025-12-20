# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0 

        #In a palindrome , there can be atmost 1 odd frequency of elements

        # def dfs(curr):
        #     nonlocal odd
        #     if not curr : 
        #         #BAse calculates the number of palindrome found per path
        #         return 0 

        #     count[curr.val] += 1 
        #     #Basically if current value is even , then we got a odd value along the path 
        #     odd_change = 1 if count[curr.val] % 2 else -1
        #     #We add the odd_change here 
        #     odd += odd_change
        #     if not curr.left and not curr.right : 
        #         #Leaf node condition
        #         #if odd along path is this , then we have found a palindrome in this path 
        #         res = 1 if odd <= 1 else 0 
        #     else : 
        #         #Otherwise , we add up palindromes from different paths 
        #         res = dfs(curr.left) + dfs(curr.right)

        #     #We decrement odd and the frequency , to backtrack to previous node 
        #     count[curr.val] -= 1 
        #     odd -= odd_change

        #     #Then we return res
        #     return res 
        
        # return dfs(root)

        #Bitmask 
        def dfs(node, p):
            if not node:
                return 0

            p ^= (1 << node.val)

            if not node.left and not node.right:
                return 1 if p & (p - 1) == 0 else 0 
            return dfs(node.left, p) + dfs(node.right, p)

        return dfs(root, 0)