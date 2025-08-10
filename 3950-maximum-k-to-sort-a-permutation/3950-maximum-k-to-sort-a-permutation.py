class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        mask = (1 << 30) - 1

        for i in range(len(nums)):
            if i == nums[i]:
                continue 

            mask &= nums[i]

        return 0 if mask == (1 << 30 ) -1 else mask

            