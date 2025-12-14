class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

# 1.Pruning technique: if there's no enough chars to form a word, return False
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        for w in word:
            if word_count[w] > board_count[w]:
                return False

# 2.Pruning technique: counting 1st & last char of word in board and 
# if 1st char count is greater, reverse the word before calling dfs
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        rows, cols = len(board), len(board[0])
        choices = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n = len(word)

        visit = set()

        def dfs(level, curWord, r, c):
            if level == n - 1:
                if word[level] == curWord[-1]:
                    return True
                return False

            # print(word[level], curWord[-1], level)
            #word check to do pruning 
            if word[level] != curWord[-1]:
                return 

            visit.add((r, c))

            res = False
            for dx, dy in choices:
                nxtR = r + dx 
                nxtC = c + dy
                if 0 <= nxtR <= rows - 1 and 0 <= nxtC <= cols - 1 and (nxtR, nxtC) not in visit:
                    curWord.append(board[nxtR][nxtC])
                    res = res or dfs(level + 1, curWord, nxtR, nxtC)
                    curWord.pop()

            visit.remove((r, c))

            return res



        for r in range(rows):
            for c in range(cols):
                if dfs(0, [board[r][c]], r, c):
                    return True
        return False













        
        # ROWS , COLS = len(board) , len(board[0])
        # visit = set()
        # def dfs(r,c,i): 
        #     if i == len(word):
        #         return True 
        #     if (r < 0 or c < 0 or r >= ROWS or c >= COLS or ((r,c) in visit) or word[i] != board[r][c] ):
        #         return False
        #     visit.add((r,c))
        #     res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
        #     visit.remove((r,c))
        #     return res 
        # # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        # count = defaultdict(int , sum(map(Counter,board),Counter()))
        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if dfs(r,c,0):
        #             return True 
        # return False 
        #  # O(n * m * 4^n)