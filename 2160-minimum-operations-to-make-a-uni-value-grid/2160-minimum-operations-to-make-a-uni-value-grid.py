class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        row = len(grid)
        col = len(grid[0])
        arr = []
        for i in range(row):
            for j in range(col):
                arr.append(grid[i][j])

        arr.sort()
        l = 0 
        r = len(arr) - 1
        mid = ((l + r) // 2)
        required = arr[mid]
        ops = 0
        for i in range(len(arr)):
            if i != mid: 
                diff = abs(required - arr[i])
                if diff % x == 0:
                    ops += (diff // x)
                else:
                    return -1
        return ops