class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0 
        q = deque()
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            while l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
        
        return output

        # output = []
        # l = r = 0 
        # #Monotically decreasing queue 
        # q = collections.deque()
        # while (r < len(nums)):
        #     #Pop small values than from q than current element
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)
        #     #Remove left value from queue , when window moves forward
        #     if l > q[0]:
        #         q.popleft()
            
        #     #Condition for maintaining the window size 
        #     if (r+1)>=k:
        #         output.append(nums[q[0]])
        #         l += 1
        #     r += 1
        # return output 