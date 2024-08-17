class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i , t in enumerate(temperatures):
            #Logic is simple  , append till you dont find a larger temperature 
            #When you find , pop all , and calculate indice like shown below 
            #return !
            while stack and t > stack[-1][0]:
                topTemp , topIndex = stack.pop()
                res[topIndex] = (i - topIndex)
            stack.append([t , i])

        return res 