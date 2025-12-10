class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Binary search

        # k = 19
        #Count pair sum logic for any T sum 
        def count_pair_sum(T):
            #lets have nums[i] as rows and fix it
            j = len(nums1) - 1
            count = 0
            total = 0 
            pair_selected = []
            for i in range(len(nums2)):
                pairs = []

                while j >= 0 and nums2[i] + nums1[j] > T:
                    j -= 1

                count += (j + 1)
                
            return count

        l = nums1[0] + nums2[0]
        r = nums1[-1] + nums2[-1]

        targetSum = -1
        while l <= r: 
            mid = (l + r) // 2

            cnt = count_pair_sum(mid)
            # print(mid)
            if cnt >= k:
                targetSum = mid
                r = mid - 1
            else: 
                l = mid + 1

        res = []

        for n1 in nums1: 
            for n2 in nums2: 
                if (n1 + n2) < targetSum:
                    res.append((n1, n2))
                else:
                    break
        
        for i in range(len(nums2)):
            if len(res) >= k:
                break
            for j in range(len(nums1)):
                if len(res) >= k:
                    break
                if nums1[j] + nums2[i] == targetSum:
                    res.append([nums1[j], nums2[i]])
        return res
                 





        

                


        #Binary search on Ans (Here sum)






        #Smallest Pairs with Help of Djishktra Algo type logic 

        # m = len(nums1)
        # n = len(nums2)
        # visited = set()
        # minHeap = [(nums1[0] + nums2[0], 0 , 0)]
        # res = []
        # while k > 0 and minHeap: 
        #     curTotal , i, j = heapq.heappop(minHeap)
        #     res.append([nums1[i], nums2[j]])

        #     #Next minimum is either with pair , i , j + 1 -- or -- i + 1, j  
        #     if i + 1 < m and (i + 1, j) not in visited: 
        #         heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
        #         visited.add((i + 1, j))

        #     if j + 1 < n and (i, j + 1) not in visited: 
        #         heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
        #         visited.add((i, j + 1))           
            
        #     k -= 1 
        
        # return res

