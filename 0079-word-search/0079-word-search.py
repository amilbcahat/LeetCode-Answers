class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS , COLS = len(board) , len(board[0])

        visit = set()
        def dfs(r , c , i): 
            if i == len(word):
                return True 

            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r , c) in visit or word[i] != board[r][c]:
                return False 

            visit.add((r , c))

            res = (dfs(r + 1 , c , i + 1 ) or 
            dfs( r , c + 1 , i + 1) or 
            dfs(r - 1, c , i + 1) or 
            dfs(r , c - 1 , i + 1))

            visit.remove((r , c))
            
            return res 
            
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int , sum(map(Counter,board),Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r , c , 0):
                    return True 

        return False 
