class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxDeque = deque()
        minDeque = deque()
        l = 0
        res = 0
        for r in range(len(nums)): 

            while maxDeque and nums[maxDeque[-1]] < nums[r]: 
                maxDeque.pop()
            maxDeque.append(r)

            while minDeque and nums[minDeque[-1]] > nums[r]: 
                minDeque.pop()
            minDeque.append(r)

            while l <= r and (nums[maxDeque[0]] - nums[minDeque[0]] > 2 or nums[maxDeque[0]] - nums[minDeque[0]] < 0): 
                if maxDeque[0] == l: 
                    maxDeque.popleft()
                if minDeque[0] == l: 
                    minDeque.popleft()
                l += 1

            res += (r - l + 1)

        return res 