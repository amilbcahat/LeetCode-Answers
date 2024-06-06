class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M , N = len(grid) , len(grid[0])

        res = [[0] * N for _ in range(M)]
        def posToVal(r , c):
            return r * N + c 

        def valToPos(v):
            return [v // N , v % N]

        for r in range(M):
            for c in range(N):
                #Change to pos in 1D array 
                newVal = (posToVal(r , c) + k) % (N * M)
                #changed back to 2D matrix
                newR , newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]

        return res


            