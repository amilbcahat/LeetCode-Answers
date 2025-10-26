class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]: 
                l = mid + 1
            elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]: 
                r = mid - 1
            else: 
                return mid 
