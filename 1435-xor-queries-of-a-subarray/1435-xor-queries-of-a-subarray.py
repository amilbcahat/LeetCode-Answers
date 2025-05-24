class Query: 
    def __init__(self, left, right, index): 
        self.left = left
        self.right = right 
        self.index = index

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        #MO's Algorithm 

        n = len(arr)
        q = len(queries)
        blockSize = int(math.sqrt(n))

        qs = [Query(queries[i][0], queries[i][1], i) for i in range(q)]
        qs.sort(key=lambda q: (q.left // blockSize, q.right))
        res = [0] * len(queries)
        currentRight = -1
        currentLeft = 0
        currentXor = 0
        for q in qs: 
            left = q.left
            right = q.right
            while currentRight < right: 
                currentRight += 1
                currentXor ^= arr[currentRight]

            while currentRight > right: 
                currentXor ^= arr[currentRight]
                currentRight -= 1
            

            while currentLeft < left: 
                currentXor ^= arr[currentLeft]
                currentLeft += 1
                

            while currentLeft > left: 
                currentLeft -= 1
                currentXor ^= arr[currentLeft]

            res[q.index] = currentXor

        return res