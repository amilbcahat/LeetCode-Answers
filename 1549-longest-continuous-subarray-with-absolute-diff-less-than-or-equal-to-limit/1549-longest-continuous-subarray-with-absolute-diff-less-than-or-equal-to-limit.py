class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0 
        minDeque = deque()
        maxDeque = deque()
        res = float("-inf")
        for r in range(len(nums)): 
            while minDeque and minDeque[-1] > nums[r]: 
                minDeque.pop()
            minDeque.append(nums[r])

            while maxDeque and maxDeque[-1] < nums[r]: 
                maxDeque.pop()
            maxDeque.append(nums[r])

            while maxDeque[0] - minDeque[0] > limit: 
                if maxDeque[0] == nums[l]: 
                    maxDeque.popleft()
                if minDeque[0] == nums[l]: 
                    minDeque.popleft()
                l += 1
                
            res = max(res, r - l + 1)

        return res