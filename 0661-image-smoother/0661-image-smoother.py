class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        #Solution -2 
        #Stored the avg in the bits of the img[i][j] and that was 255 (constraints)

        ROWS , COLS = len(img) , len(img[0])

        for r in range(ROWS):
            for c in range(COLS):
                total , cnt = 0 , 0

                for i in range(r - 1 , r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == ROWS or j == COLS or j < 0 : 
                            continue 
                        total += img[i][j] % 256 #scrape and get the 101 part of 101 1111 1111 in bits 
                        cnt += 1 

                img[r][c] = img[r][c] ^ (total // cnt) << 8 #Puts the number before 1111 1111 bits of 255 

        for r in range(ROWS):
            for c in range(COLS):
                img[r][c] = img[r][c] >> 8  #Puts the average in current digits 

        return img      
        #Solution -1 
        # rows , cols = len(img) , len(img[0])

        # ans = [[0] * cols for _ in range(rows)]
        # di = [[1 , 1] , [0 , 1] , [1 ,0] , [-1 , -1] , [0 , -1] , [-1 , 0] ,[-1 , 1] , [1 ,-1]]

        # for i in range(rows):
        #     for j in range(cols):
        #         res = 0 
        #         #count itself
        #         res += img[i][j]
        #         count = 1 
        #         #Count valid neighbours ! 
        #         for r , c in di :
        #             row , col = i + r , j + c
        #             if row in range(rows) and col in range(cols):
        #                 res += img[row][col]
        #                 count += 1 

        #         el = math.floor(res / count)
        #         ans[i][j] = el 

        # return ans 