class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = -1 
        prefixSum = nums[0] 
        for i in range(len(nums)):
            if i >= 2 : 
                #if sides are more than 3 
                if nums[i] < prefixSum:
                    print(nums[i] , prefixSum)
                    #if the longest side is smaller than sum of smaller sides
                    #Then update the newest max Perimeter (prefixSum + nums[i]) 
                    ans = max(ans , prefixSum + nums[i])
            if i > 0 :
                #
                prefixSum += nums[i] 
            
        
        return ans 