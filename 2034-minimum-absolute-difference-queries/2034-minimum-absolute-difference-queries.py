class Query: 
    def __init__(self, left, right, index): 
        self.left = left
        self.right = right
        self.index = index

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)

        blockSize = int(math.sqrt(n))

        qs = [Query(queries[i][0], queries[i][1], i) for i in range(q)]
        qs.sort(key=lambda q: (q.left // blockSize, q.right))

        res = [-1] * q
        freq = [0] * 101
        currentLeft = 0 
        currentRight = -1 
        def getMinDiff(): 
            present = []
            for i in range(101): 
                if freq[i] > 0: 
                    present.append(i)

            if len(present) < 2: 
                return -1 

            minDiff = float("inf")
            for i in range(1, len(present)): 
                minDiff = min(minDiff, present[i] - present[i - 1])

            return minDiff

        for q in qs:
            left = q.left
            right = q.right
            while currentRight < right: 
                currentRight += 1
                freq[nums[currentRight]] += 1

            while currentRight > right: 
                freq[nums[currentRight]] -= 1
                currentRight -= 1

            while currentLeft < left: 
                freq[nums[currentLeft]] -= 1
                currentLeft += 1

            while currentLeft > left: 
                currentLeft -= 1
                freq[nums[currentLeft]] += 1

            res[q.index] = getMinDiff()
        return res
                
                

        













