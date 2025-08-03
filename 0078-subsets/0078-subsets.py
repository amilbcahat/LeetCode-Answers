class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #subsets https://leetcode.com/problems/subsets/solutions/5190785/python-bit-manipulation-code-walkthrough-step-by-step-with-comments
        n = len(nums)
        ans = []
        for num in range(1 << n): 
            subsets = []
            for i in range(n): 
                if (num & (1 << i)) != 0: 
                    subsets.append(nums[i])
            ans.append(subsets)

        return ans

        # n = len(nums)
        # res = []
        # def dfs(i, cur):
        #     res.append(cur[:])

        #     for j in range(i, n):
        #         cur.append(nums[j])
        #         dfs(j + 1, cur)
        #         cur.pop()

        # dfs(0, [])
        # return res
            
