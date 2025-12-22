class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Base Case 
        #For [1,2,4,3]
        #LIS[3] =1 Base case 
        #LIS[2] = max(1, LIS[3]) X -> 1 
        #LIS[1] = max(1, LIST[2]+1 , LIS[3]+1) -> 2 
        #LIS[0] = max(1 , 1+1 , 1+1 ,1+2) -> 3  
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)