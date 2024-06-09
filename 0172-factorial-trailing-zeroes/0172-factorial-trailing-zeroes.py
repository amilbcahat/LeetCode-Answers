class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + n//25 +n//125 + n//625 + n//3125
        #Brute force 
        # ans = 1 

        # for i in range(1, n + 1): 
        #     ans *= i 
        
        
        # print(ans)
        # count = 0 
        # #Find trailing zeroes 
        # while ans % 10 == 0 : 
            
        #     ans = ans // 10 
        #     count += 1 


        # return count 