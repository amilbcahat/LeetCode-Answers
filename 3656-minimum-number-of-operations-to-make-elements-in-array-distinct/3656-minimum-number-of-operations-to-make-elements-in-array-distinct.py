class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)): 
            return 0

        k = 0
        for i in range(len(nums)): 
            if (i + 1) % 3 == 0: 
                k += 1
                if len(set(nums[i + 1:])) == (len(nums) - i - 1): 
                    print(nums[i + 1:], len(nums) - i - 1)
                    return k 

        return k + 1