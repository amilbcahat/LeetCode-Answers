class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        ap_info = {"has_articulation": False, "time": 0}

        parents = [[-1] * cols for _ in range(rows)]
        low_reachable = [[-1] * cols for _ in range(rows)]
        discovery_time = [[-1] * cols for _ in range(rows)]

        di = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def find_articulation_point(row, col): 
            discovery_time[row][col] = ap_info["time"]
            ap_info["time"] += 1
            low_reachable[row][col] = discovery_time[row][col]

            children = 0 

            for r , c in di: 
                new_col = c + col
                new_row = r + row 

                if (
                    0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    grid[new_row][new_col] == 1
                ): 
                    if discovery_time[new_row][new_col] == -1: 
                        children += 1
                        parents[new_row][new_col] = (
                            row * cols + col
                        )

                        find_articulation_point(new_row, new_col)

                        low_reachable[row][col] = min(
                            low_reachable[row][col], 
                            low_reachable[new_row][new_col]
                        )

                        if low_reachable[new_row][new_col] >= discovery_time[row][col] and parents[row][col] != -1: 
                            ap_info["has_articulation"] = True 

                    elif new_row * cols + new_col != parents[row][col]: 
                        low_reachable[row][col] = min(
                            low_reachable[row][col], 
                            discovery_time[new_row][new_col]
                        )
                    #backedge

            if parents[row][col] == -1 and children > 1: 
                ap_info["has_articulation"] = True

        islands = 0 
        lands = 0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    lands += 1
                    if discovery_time[i][j] == -1:
                        find_articulation_point(i, j)
                        islands += 1

        if islands == 0 or islands >= 2:
            return 0 

        if lands == 1: 
            return 1 

        if ap_info["has_articulation"]: 
            return 1

        return 2 

