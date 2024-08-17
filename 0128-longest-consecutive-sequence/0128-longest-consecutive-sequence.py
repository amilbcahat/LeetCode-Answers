class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for n in nums : 
            if n not in numSet : 
                length = 1 
                while n + length in numSet : 
                    length += 1
                longest = max(longest , length)

        return longest