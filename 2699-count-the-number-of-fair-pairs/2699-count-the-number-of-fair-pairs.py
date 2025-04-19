class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        
        nums.sort()
        res = 0
        for i in range(len(nums)): 
            l = i + 1
            r = len(nums) - 1
            low = len(nums)
            high = i
            #lower bound
            while l <= r : 
                mid = (l + r) // 2
                if nums[mid] + nums[i] >= lower:
                    low = mid
                    r = mid - 1
                else: 
                    l = mid + 1

            #upper bound
            l = i + 1
            r = len(nums) - 1
            while l <= r : 
                mid = (l + r) // 2
                if nums[mid] + nums[i] <= upper : 
                    high = mid
                    l = mid + 1
                else: 
                    r = mid - 1

            res += (high - low + 1)


        return res


            