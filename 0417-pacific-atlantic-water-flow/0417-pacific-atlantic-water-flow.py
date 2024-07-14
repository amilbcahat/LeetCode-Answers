class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        alt , pac = set() , set()

        
        def dfs(r , c ,visit , prevHeight) : 
            if (r , c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight:
                return 

            visit.add((r , c))
            dfs(r + 1 , c , visit , heights[r][c])
            dfs(r - 1 , c , visit ,heights[r][c])
            dfs(r  , c  + 1,visit , heights[r][c])
            dfs(r  , c - 1,visit , heights[r][c])

        
        for c in range(cols) : 
            dfs(0 , c , pac , heights[0][c])
            dfs(rows - 1, c , alt , heights[rows - 1][c])

        for r in range(rows) : 
            dfs(r , 0 , pac , heights[r][0])
            dfs(r , cols - 1, alt , heights[r][cols - 1])
        #Bit Anding to Find the Common Ones !
        return (alt & pac)