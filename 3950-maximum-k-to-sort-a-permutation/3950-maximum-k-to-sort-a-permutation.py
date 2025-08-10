class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Solution: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/solutions/7062883/no-cycle-just-simple-cumulative-and/
        mask = (1 << 30) - 1

        for i in range(len(nums)):
            if i == nums[i]:
                continue 

            mask &= nums[i]

        return 0 if mask == (1 << 30 ) -1 else mask

            