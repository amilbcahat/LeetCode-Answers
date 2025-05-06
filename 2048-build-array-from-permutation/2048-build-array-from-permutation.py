class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = 1000
        for i in range(len(nums)): 
            nums[i] += n * (nums[nums[i]] % n) 

        for i in range(len(nums)): 
            nums[i] //= n

        return nums

        