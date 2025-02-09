class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Smallest Pairs with Help of Djishktra Algo type logic 

        m = len(nums1)
        n = len(nums2)
        visited = set()
        minHeap = [(nums1[0] + nums2[0], 0 , 0)]
        res = []
        while k > 0 and minHeap: 
            curTotal , i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            #Next minimum is either with pair , i , j + 1 -- or -- i + 1, j  
            if i + 1 < m and (i + 1, j) not in visited: 
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited: 
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))           
            
            k -= 1 
        
        return res

