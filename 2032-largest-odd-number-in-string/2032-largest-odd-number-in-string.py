class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        #Check from last , where is ODD indicie , and return start:end+1 , that would be the largest odd number 
        for i in range(len(num)-1 , -1 , -1):
            if int(num[i]) % 2 == 1 : 
                return num[:i+1]

        return ""