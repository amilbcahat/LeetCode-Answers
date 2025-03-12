class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0: 
            return len(nums)

        if nums[0] == 0 and nums[-1] == 0: 
            return 0

        l = 0 
        r = len(nums) - 1
        res = -1
        while l <= r: 
            mid = (l + r) // 2 
            if nums[mid] > -1:
                r = mid - 1
            else: 
                res = mid
                l = mid + 1

        #count zeroes 

        low = 0
        high = 0
        l = 0
        r = len(nums) - 1
        hasZero = False
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == 0:
                r = mid - 1
                low = mid
                hasZero = True
            elif nums[mid] > 0: 
                r = mid - 1
            else: 
                l = mid + 1

        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == 0:
                l = mid + 1
                high = mid
            elif nums[mid] > 0:
                r = mid - 1
            else: 
                l = mid + 1

        cntZero = (high - low + 1) if hasZero else 0
        neg = res + 1
        pos = len(nums) - neg - cntZero 
        print(cntZero, neg, high, low)
        return max(neg, pos)