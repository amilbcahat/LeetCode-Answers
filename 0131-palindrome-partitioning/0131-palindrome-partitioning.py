class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        part = []

        def dfs(i):
            if i >= len(s) : 
                ans.append(part.copy())
                return 

            #aab -> a , aa , aab
            #a - a - a (Good Partition)
            #aa - b (Good Partition)
            #aab - (Not a pali)
            for j in range(i , len(s)):
                if isPali(i , j) : 
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        

        def isPali(l , r):
            
            while l < r : 
                if s[l] != s[r]:
                    return False 
                l += 1 
                r -= 1
            return True 

        dfs(0)
        return ans 