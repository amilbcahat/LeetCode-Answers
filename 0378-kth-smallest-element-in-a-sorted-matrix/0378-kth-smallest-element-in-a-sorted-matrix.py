class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        def check(x): 
            cntless = 0
            for cur_row in matrix: 
                l = 0 
                r = len(cur_row) - 1
                ans = -1
                while l <= r: 
                    mid = (l + r) // 2
                    if cur_row[mid] <= x: 
                        ans = mid 
                        l = mid + 1
                    else: 
                        r = mid - 1

                cntless += (ans + 1)
            return 1 if cntless >= k else 0 

        l = matrix[0][0]
        r = matrix[-1][-1]

        res = 0
        while l <= r: 
            mid = (l + r) // 2
            if check(mid) == 1: 
                res = mid
                r = mid - 1
            else: 
                l = mid + 1

        return res

        


        #We are going from smallest to greater , thats why this works 
        # minHeap = [(matrix[0][0], 0, 0)]
        # n = len(matrix)
        # visited = set()
        # while k > 0 and minHeap: 
        #     val, i, j = heapq.heappop(minHeap)

        #     if i + 1 < n and (i + 1, j) not in visited: 
        #         heapq.heappush(minHeap, (matrix[i + 1][j], i  + 1, j))
        #         visited.add((i + 1, j))

        #     if j + 1 < n and (i, j + 1) not in visited:
        #         heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))
        #         visited.add((i, j + 1))

        #     k -= 1

        # return val
        # Same djishkra like logic to find minimum path 
        # minHeap = [(matrix[0][0], 0 , 0)]
        # n = len(matrix)
        # visited = set()
        # while k > 0 and minHeap : 
        #     val, i, j = heapq.heappop(minHeap)

        #     #Either go i + 1 , j or i , j + 1
        #     if i + 1 < n and (i + 1, j) not in visited: 
        #         heapq.heappush(minHeap, (matrix[i + 1][j], i + 1, j))
        #         visited.add((i + 1, j))
            
        #     if j + 1 < n and (i , j + 1) not in visited: 
        #         heapq.heappush(minHeap, (matrix[i][j + 1], i , j + 1))
        #         visited.add((i , j + 1))

        #     k -= 1 

        # return val
        
