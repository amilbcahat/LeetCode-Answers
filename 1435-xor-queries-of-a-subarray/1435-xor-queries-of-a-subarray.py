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
        blockSize = int(math.sqrt(n))  # Size of each block for Mo's algorithm
        answer = [0] * q

        # Create an array of Query objects to hold the queries with their indices
        qs = [Query(queries[i][0], queries[i][1], i) for i in range(q)]

        # Sort the queries according to the block and then by the right index
        qs.sort(key=lambda x: (x.left // blockSize, x.right))

        currentLeft, currentRight, currentXor = 0, -1, 0  # Initialize pointers and current XOR

        # Process each query in the sorted order
        for query in qs:
            # Expand the right boundary to include new elements in the XOR calculation
            while currentRight < query.right:
                currentRight += 1
                currentXor ^= arr[currentRight]
            # Shrink the right boundary to exclude elements from the XOR calculation
            while currentRight > query.right:
                currentXor ^= arr[currentRight]
                currentRight -= 1
            # Expand the left boundary to exclude elements from the XOR calculation
            while currentLeft < query.left:
                currentXor ^= arr[currentLeft]
                currentLeft += 1
            # Shrink the left boundary to include new elements in the XOR calculation
            while currentLeft > query.left:
                currentLeft -= 1
                currentXor ^= arr[currentLeft]

            answer[query.index] = currentXor

        return answer