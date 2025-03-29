class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize result array for each query
        res = [0] * len(queries)
        
        # Create list of (query_value, original_index) pairs and sort by query_value
        # This allows us to process queries in ascending order while keeping track of original positions
        sortedQueries = sorted([(queries[i], i) for i in range(len(queries))])
        
        # Set to track visited cells
        visit = set()
        
        # Min heap to process cells in order of increasing value
        # Format: (cell_value, row, column)
        minHeap = [(grid[0][0], 0, 0)]
        
        # Counter for cells with values less than current query
        points = 0
        
        # Process each query in ascending order
        for query, queryIndx in sortedQueries:
            # Process all cells with values less than current query
            while minHeap and minHeap[0][0] < query:
                w, r, c = heapq.heappop(minHeap)
                
                # Skip if we've already visited this cell
                if (r, c) in visit:
                    continue
                
                # Increment point count for each new valid cell
                points += 1
                
                # Mark current cell as visited
                visit.add((r, c))
                
                # Check all four adjacent cells (left, down, right, up)
                for dr, dc in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                    row, col = r + dr, c + dc
                    
                    # Skip if the cell is out of bounds
                    if row < 0 or col < 0 or col >= cols or row >= rows:
                        continue
                    
                    # Add valid neighbor to the min heap
                    heapq.heappush(minHeap, (grid[row][col], row, col))
            
            # Store the current point count for this query
            res[queryIndx] = points
        
        return res