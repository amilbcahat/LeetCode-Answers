class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #Logic is simple , if a number has some set bit , then at that place you cant have a set bit O(n)
        used_bits = 0 
        res = 0
        l = 0
        for r in range(len(nums)): 
            while used_bits & nums[r] != 0: 
                used_bits ^= nums[l]
                l += 1

            used_bits |= nums[r]
            res = max((r - l + 1), res)
        return res

            