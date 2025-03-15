class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #KOKO algo 

        def is_valid(capacity): 
            indx = 0
            possible_thefts = 0  
            while indx < len(nums): 
                if nums[indx] <= capacity: 
                    possible_thefts += 1
                    indx += 2 
                else: 
                    indx += 1
            return possible_thefts >= k

        l = 1 
        r = max(nums)
        # The confusion might be coming from the example explanation. It's not about taking the maximum value of all robbed houses. Rather, it's about finding the minimum capability such that the thief can rob at least k houses, where capability means "the maximum value the thief can handle in a single house."
        #The binary search approach starts with a capability and asks "can I rob k houses with this?"
        #The key insight is that when a greedy approach is used with a fixed capability threshold:

        # If we can rob a house, we always should (to maximize houses robbed)
        # If we can't rob a house, we must skip it
        # Non-adjacent constraint is handled by skipping the next house after each robbery

        res = float("inf")
        while l <= r : 
            mid = (l + r) // 2 
            
            if is_valid(mid): 
                res = min(res, mid)
            # every valid m that is not part of nums, there exists a smaller m which is part of the nums. The trick here is to understand that for a range [l, r], the smallest value that satisfies is_valid function would be part of nums because in is_valid we are checking nums[i] <= capability. So if a capability satisfies this condition and it is not part of nums, there is also a smaller capability which would satisfy the equality part of this condition i.e. would be part of nums.
                r = mid - 1
            else: 
                l = mid + 1

        return res
        #TLE n for space 
        # N = len(nums)
        # prev = [float("inf")] * (N + 2)
        # for i in reversed(range(N)):
        #     prev[i] = min(nums[i], prev[i + 1])
        
        # for j in reversed(range(2, k + 1)): 
        #     cur = [float("inf")] * (N + 2)
        #     for i in reversed(range(N)): 
        #         res1 = max(nums[i], prev[i + 2]) 
        #         res2 = cur[i + 1]
        #         cur[i] = min(res1, res2)
        #     prev = cur
        # return prev[0]

        # MLE -> n^2 for both 
        # cache = {}
        # def backtrack(i, k): 
        #     if i >= len(nums): 
        #         if k: 
        #             return float("inf")
        #         return 0
            
        #     if (i, k) in cache: 
        #         return cache[(i, k)]
        #     res1 = max(nums[i], backtrack(i + 2, k - 1))
        #     res2 = backtrack(i + 1, k)
        #     res = min(res1 , res2)
        #     cache[(i, k)] = res
        #     return res

        # return backtrack(0, k)