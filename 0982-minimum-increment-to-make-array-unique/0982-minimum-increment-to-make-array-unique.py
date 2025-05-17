class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #Solution 1 (Counting Pattern from Grokking)
        n = len(nums)
        max_val = max(nums)
        ans = 0
        freq = [0] * (n + max_val)

        for val in nums: 
            freq[val] += 1

        for i in range(len(freq)): 
            if freq[i] <= 1: 
                continue 

            duplicates = freq[i] - 1
            freq[i + 1] += duplicates
            freq[i] = 1 #Not necessary 
            ans += duplicates

        return ans

        # Solution 2 
        # nums.sort()

        # #Problem 1827 
        # ans =  0 
        # for i in range(1, len(nums)): 
        #     if nums[i - 1] >= nums[i]: 
        #         diff = (nums[i - 1] - nums[i] + 1)
        #         nums[i] += diff
        #         ans += diff

        # return ans