class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, cur):
            res.append(cur[:])

            for j in range(i, n):
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()

        dfs(0, [])
        return res
            
