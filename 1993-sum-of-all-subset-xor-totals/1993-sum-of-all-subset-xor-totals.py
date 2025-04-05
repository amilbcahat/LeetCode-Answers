class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #Just neetcode's video
        res = 0
        for n in nums:
            res |= n 

        return res * (2 ** (len(nums) - 1))