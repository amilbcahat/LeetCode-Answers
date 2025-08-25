class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #Editorial Solution 2- 

        N, M = len(mat), len(mat[0])
        res = []

        for d in range(N + M - 1): 
            if d % 2 == 0: 
                #reverse 
                r, c = d if d < N else N - 1 , 0 if d < N else d - N + 1 
                while r > -1 and c < M:
                    print(r, c)
                    res.append(mat[r][c])
                    r -= 1 
                    c += 1
            else:
                r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
                while r < N and c > -1 :
                    res.append(mat[r][c])
                    r += 1
                    c -= 1

        return res


        #Editorial Solution 1- 
        # N, M = len(mat), len(mat[0])
        # res, intermediate = [], []

        # for d in range(N + M - 1): 
        #     intermediate.clear()

        #     r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

        #     while r < N and c > -1: 
        #         intermediate.append(mat[r][c])
        #         r += 1
        #         c -= 1

        #     if d % 2 == 0: 
        #         res.extend(intermediate[::-1])
        #     else:
        #         res.extend(intermediate)

        # return res


        #My solution - 
        #check n queens ques 
        #intuition is that , pos diag elements in same diag are in r + c
        # m, n = len(mat), len(mat[0])
        # last = (m - 1) + (n - 1)
        # diagMap = defaultdict(list)
        # ans = [-1] * (m * n)
        # for r in range(m): 
        #     for c in range(n): 
        #         if (r + c) & 1 == 0:     
        #             diagMap[r + c].append(mat[r][c])
        #         else: 
        #             diagMap[r + c].append(mat[r][c])

        # idx = 0 
        # for itemS, val in diagMap.items():
        #     if itemS & 1 == 0: 
        #         for i in range(len(val) - 1, -1 , -1): 
        #             ans[idx] = val[i]
        #             idx += 1
        #     else:
        #         for i in range(len(val)):
        #             ans[idx] = val[i]
        #             idx += 1

        # return ans
            