class Solution:
    def findMin(self, arr: List[int]) -> int:
        l = 0 
        r = len(arr) - 1                    
        res = float("inf")
        
        while l <= r: 
            mid = (l + r) // 2
            
            if arr[l] == arr[mid] == arr[r]:
                res = min(res, arr[mid])
                l += 1
                r -= 1
            elif arr[mid] <= arr[r]:
                res = min(res, arr[mid])
                r = mid - 1
            else:   
                l = mid + 1         

        return res