class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows , cols = len(img) , len(img[0])

        ans = [[0] * cols for _ in range(rows)]
        di = [[1 , 1] , [0 , 1] , [1 ,0] , [-1 , -1] , [0 , -1] , [-1 , 0] ,[-1 , 1] , [1 ,-1]]

        for i in range(rows):
            for j in range(cols):
                res = 0 
                #count itself
                res += img[i][j]
                count = 1 
                #Count valid neighbours ! 
                for r , c in di :
                    row , col = i + r , j + c
                    if row in range(rows) and col in range(cols):
                        res += img[row][col]
                        count += 1 

                el = math.floor(res / count)
                ans[i][j] = el 

        return ans 