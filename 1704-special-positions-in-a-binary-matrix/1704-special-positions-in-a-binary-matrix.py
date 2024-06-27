class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        trans = [[0] * rows for _ in range(cols)]

        for i in range(rows): 
            for j in range( cols):
                trans[j][i] = mat[i][j]

        ans = 0 
        for i in range(rows):
            for j in range(cols):
                if sum(mat[i]) == 1 and sum(trans[j]) == 1 and mat[i][j] == 1 : 
                    ans += 1 
        return ans