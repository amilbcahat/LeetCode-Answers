class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        minHeap = [(matrix[0][0], 0 , 0)]
        n = len(matrix)
        visited = set()
        while k > 0 and minHeap : 
            val, i, j = heapq.heappop(minHeap)

            if i + 1 < n and (i + 1, j) not in visited: 
                heapq.heappush(minHeap, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < n and (i , j + 1) not in visited: 
                heapq.heappush(minHeap, (matrix[i][j + 1], i , j + 1))
                visited.add((i , j + 1))

            k -= 1 

        return val
        
