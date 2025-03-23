class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        #KOKO + Difference Array Validity Check
        def isValid(k):
            temp_nums = nums.copy()
            diff = [0] * (len(nums) + 1)
            for i in range(k):
                start, end, val = queries[i]
                diff[start] += val 
                diff[end + 1] -= val 

            curr = diff[0]
            for i in range(1, len(nums)): 
                diff[i] += diff[i - 1]

            for i in range(len(nums)): 
                temp_nums[i] -= diff[i]
                if temp_nums[i] > 0: 
                    return False
            return True

        l = 0
        r = len(queries)
        res = -1
        while l <= r: 
            mid = (l + r) // 2
            if isValid(mid): 
                res = mid
                r = mid - 1
            else: 
                l = mid + 1
        return res


        