class Solution:
    def minMoves(self, balance: List[int]) -> int:
            
        rightSide = 0 
        leftSide = 0
        observed = False
        targetIdx = float("-inf")
        for i, n in enumerate(balance): 
            if n < 0: 
                observed = True 
                val = n
                targetIdx = i
            else:
                if observed: 
                    rightSide += n
                elif not observed: 
                    leftSide += n
        
        if targetIdx == float("-inf"):
            return 0

        if targetIdx == len(balance) - 1 and len(balance) == 1:
            return -1

        n = len(balance)
        l = targetIdx - 1
        r = targetIdx + 1
        target = balance[targetIdx]
        nxtL = (l % n)
        nxtR = (r % n)
        dist = 1
        minHeap = [(dist, -balance[nxtL] , nxtL, "left"), (dist,-balance[nxtR], nxtR, "right")] #(moves_min, dist, idx)
        heapq.heapify(minHeap)
        ans = 0
        total_moves = 0
        # print(minHeap)
        while nxtL != nxtR: 
            #where to go
            # print(minHeap)
            dist, thisSum, ptr, di = heapq.heappop(minHeap)
            
            print( thisSum, dist, ptr, di)

            if abs(target) <= abs(thisSum):
                required = abs(target)
                total_moves += (required * dist)
                return total_moves

            target += abs(thisSum)
            total_moves += (abs(thisSum) * dist)

            if di == "left": 
                nxtL = (ptr - 1) % n 
                heapq.heappush(minHeap, ( dist + 1,-balance[nxtL], nxtL, "left"))
            else: 
                nxtR = (ptr + 1) % n 
                heapq.heappush(minHeap, (dist + 1,-balance[nxtR],  nxtR, "right"))

        # print(minHeap)
        if minHeap: 
            dist, thisSum, ptr, di = heapq.heappop(minHeap)
            if abs(target) <= abs(thisSum):
                required = abs(target)
                total_moves += (required * dist)
                return total_moves

        return -1
                
            

        # return if (leftSide + rightSide - val) >= 0 else -1
                