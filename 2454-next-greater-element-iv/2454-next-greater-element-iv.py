class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        n = len(A)
        stack = []
        minHeap = []
        res = [-1] * n 
        for i in range(n):
            while minHeap and minHeap[0][0] < A[i]:
                elem, targetIdx = heapq.heappop(minHeap)
                res[targetIdx] = A[i]

            while stack and A[stack[-1]] < A[i]:
                j = stack.pop()
                heapq.heappush(minHeap, (A[j], j))

            stack.append(i)

        return res

