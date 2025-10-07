class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #We are going from smallest to greater , thats why this works 
        minHeap = [(matrix[0][0], 0, 0)]
        n = len(matrix)
        visited = set()
        while k > 0 and minHeap: 
            val, i, j = heapq.heappop(minHeap)

            if i + 1 < n and (i + 1, j) not in visited: 
                heapq.heappush(minHeap, (matrix[i + 1][j], i  + 1, j))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))

            k -= 1

        return val
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
        
