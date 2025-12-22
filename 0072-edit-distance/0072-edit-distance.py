class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j  # Insert remaining
            if j == len(word2):
                return len(word1) - i  # Delete remaining
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = dfs(i, j + 1)
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                cache[(i, j)] = 1 + min(insert, delete, replace)
            
            return cache[(i, j)]
        
        return dfs(0, 0)