class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0 
        r = len(arr) - 1

        curGap = 0
        while l <= r : 
            mid = (l + r) // 2 
            #We run binary search on range of missingNo 
            missingNo = arr[mid] - (mid + 1)
            if missingNo < k : 
                l = mid + 1 
                #This is formula to get the missing No at kth position
                curGap = k - missingNo
            else : 
                r = mid - 1

        #When we go out , it gives , r , l (range between kth missing number value lies)
        #r is on left side and l is on right side because , while loop ends 
        #arr[r] + more 
        # more -> k - missingNo (5 - 3) -> 2 
        #arr[r] + (k - missingNo)
        #arr[r] + k - arr[r] + (r + 1)
        #r + k + 1

        return r + k + 1