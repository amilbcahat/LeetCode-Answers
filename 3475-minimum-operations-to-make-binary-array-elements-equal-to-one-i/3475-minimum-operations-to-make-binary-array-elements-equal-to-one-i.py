class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        flips = 0 #Just look if first bit is not 1 then you need to change next bits !!
        for r in range(2, len(nums)): 
            if nums[l] == 0: 
                for i in range(l, l + 3): 
                    nums[i] = nums[i] ^ 1 
                flips += 1
            l += 1
        
        return flips if nums == [1] * len(nums) else -1
