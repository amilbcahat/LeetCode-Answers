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

        return k + 1 # +1 , atones to the fact, that the code comes here , if no removals could reach the condition of distinct, in that case, + 1 removal would be required for removal
        #of leftovers, which is < 3, left after removing other elements 