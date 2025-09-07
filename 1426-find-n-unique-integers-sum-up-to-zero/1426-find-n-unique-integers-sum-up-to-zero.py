class Solution:
    def sumZero(self, n: int) -> List[int]:
        #Or can also append 0 when odd 
        #or Can append -(sum of pos natural number) , when summed everything 
        if n == 1: 
            return [0]
        res = []
        if n % 2 == 0: 
            for i in range(1, n//2 + 1): 
                res.append(i)
                res.append(-i)
        else:
            for i in range(1, n//2 + 2): 
                res.append(i)

            # res.append(res[0] + res[1])

            totalPosLast = res[-1] + res[-2]

            for i in range(1, n//2): 
                res.append(-i)

            res.append(-1 * totalPosLast)

        return res