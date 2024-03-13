class Solution:
    def pivotInteger(self, n: int) -> int:
        #Using prefix and postfix Sum 
        prefixSum= 0
        postfixSum = 0
        prefix = []
        postfix = []
        for i in range(1, n + 1) : 
            prefixSum += i
            prefix.append(prefixSum )

        
        for i in range(n  ,0 , -1):
            postfixSum += i 
            postfix.append(postfixSum)

        postfix = postfix[::-1]

        for i in range(0 , n):
            print(prefix[i] ,postfix[i])
            if prefix[i] == postfix[i]:
                return i + 1
        return -1 