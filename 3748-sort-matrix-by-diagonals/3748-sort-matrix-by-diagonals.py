class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 1

        heads = []

        for d in range(n + 1): 
            minHeap = []
            #increasing
            if True: 
                #head 1 (0, d) 
                r, c = d, 0
                while r <= n  and c <= n :
                    print(r, c)
                    heapq.heappush(minHeap, grid[r][c])
                    r += 1
                    c += 1                

                c = (n) - d
                r = n
                
                while minHeap and r >=  0 and c >= 0: 
                    val = heapq.heappop(minHeap)
                    grid[r][c] = val
                    r -= 1
                    c -= 1

                minHeap.clear()
                #head 1 (0, d) 
                r, c = 0 , d 
                if c > 0:
                    while r <= n  and c <= n :
                        heapq.heappush(minHeap, grid[r][c])

                        r += 1
                        c += 1
                    
                    r , c = 0, d
                    while minHeap and r <= n  and c <= n: 
                        val = heapq.heappop(minHeap)
                        grid[r][c] = val
                        r += 1
                        c += 1

                    minHeap.clear()



        return grid