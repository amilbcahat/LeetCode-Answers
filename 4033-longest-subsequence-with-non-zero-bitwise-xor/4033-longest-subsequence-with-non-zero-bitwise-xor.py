class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Property of XOR: If A ^ B = 0, then A = B
        xor = 0 
        for num in nums: 
            xor ^= num 

        if xor != 0: 
            return len(nums)

        for num in nums: 
            if xor ^ num != 0: 
                return len(nums) - 1

        return 0

    