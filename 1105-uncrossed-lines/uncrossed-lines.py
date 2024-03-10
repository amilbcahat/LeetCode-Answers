class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        #Memory Optimized DP Solution
        prev = [0] * (len(nums2) + 1)

        for i in range(len(nums1)):
            dp = [0] * (len(nums2) + 1)
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = 1 + prev[j]
                else:
                    dp[j + 1] = max(
                        dp[j],
                        prev[j + 1]
                    )
            prev = dp

        return prev[-1]
        #Pure DP 
        # dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j] : 
        #             dp[i + 1][j + 1] = 1 + dp[i][j]
        #         else:
        #             dp[i + 1][j + 1] = max(
        #                 dp[i][j + 1], #top
        #                 dp[i + 1][j] #left
        #             )

        # return dp[len(nums1)][len(nums2)]

        #Variation of Longest Common Subsequence#
        # cache = {}        Space - O(n * m) TC - 2^(n + m)
        # def dfs(i , j):
        #     if i >= len(nums1) or j >= len(nums2):
        #         return 0 

        #     if (i , j) in cache : 
        #         return cache[(i , j)]

        #     res1 = float("-inf")

        #     if nums1[i] == nums2[j]:
        #         cache[(i , j)] = 1 + dfs(i + 1 , j + 1)
        #     else:
        #         cache[(i , j)] = max(dfs(i + 1 , j) , dfs(i , j + 1))

        #     return cache[(i , j)] 

        # return dfs(0 , 0)