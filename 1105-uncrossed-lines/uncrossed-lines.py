class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        #Variation of Longest Common Subsequence#
        cache = {}        
        def dfs(i , j):
            if i >= len(nums1) or j >= len(nums2):
                return 0 

            if (i , j) in cache : 
                return cache[(i , j)]

            res1 = float("-inf")

            if nums1[i] == nums2[j]:
                res1 = 1 + dfs(i + 1 , j + 1)

            res2 = dfs(i + 1 , j)
            res3 = dfs(i , j + 1)

            cache[(i , j)] = max(res1 , res2 , res3)

            return cache[(i , j)] 

        return dfs(0 , 0)