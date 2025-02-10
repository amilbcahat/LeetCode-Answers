class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        #Maintain two pointer to find range , or lets say 
        k = len(nums)
        left  = right = nums[0][0]
        minHeap = []

        #[1, 3 , 54 554]
        #check vertical
        for i in range(k): 
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(minHeap, (l[0], i , 0))

        res = [left , right]

        #now keep iterating until reached end 
        #Greedy logic -> compare in all three array and increment pointer of min on k comparisons !
        while True: 
            n , i , idx = heapq.heappop(minHeap)
            idx += 1 

            if idx == len(nums[i]):
                return res
            
            next_val = nums[i][idx]
            heapq.heappush(
                minHeap, (next_val, i , idx)
            )
            right = max(right, next_val)
            left = minHeap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]

        return res
