class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Usual Prefix , Postfix 
        #Notice that we write res[i] before prefix or postfix calculation ,this is not to include value at nums[i]
        res = [0] * len(nums)

        prefix = 1 

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1 

        for i in range(len(nums) - 1 , -1 , -1) : 
            res[i] *= postfix 
            postfix *= nums[i]

        return res 