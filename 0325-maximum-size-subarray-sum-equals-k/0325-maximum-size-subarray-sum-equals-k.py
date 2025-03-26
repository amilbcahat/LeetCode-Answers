class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: 
            return 1 if k == nums[-1] else 0

        total = 0 
        preMap = {0 : -1}
        preArr = []
        res = 0
        for r, num in enumerate(nums): 
            total += num 
            diff = total - k 
            if diff in preMap: 
                l = preMap[diff]
                res = max(res, r - l)
            if total not in preMap: 
                preMap[total] = r #For Maximum result 
        return res