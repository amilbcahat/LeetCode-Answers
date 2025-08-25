class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #check n queens ques 
        #intuition is that , pos diag elements in same diag are in r + c
        m, n = len(mat), len(mat[0])
        last = (m - 1) + (n - 1)
        diagMap = defaultdict(list)
        ans = [-1] * (m * n)
        for r in range(m): 
            for c in range(n): 
                if (r + c) & 1 == 0:     
                    diagMap[r + c].append(mat[r][c])
                else: 
                    diagMap[r + c].append(mat[r][c])

        idx = 0 
        for itemS, val in diagMap.items():
            if itemS & 1 == 0: 
                for i in range(len(val) - 1, -1 , -1): 
                    ans[idx] = val[i]
                    idx += 1
            else:
                for i in range(len(val)):
                    ans[idx] = val[i]
                    idx += 1

        return ans
            