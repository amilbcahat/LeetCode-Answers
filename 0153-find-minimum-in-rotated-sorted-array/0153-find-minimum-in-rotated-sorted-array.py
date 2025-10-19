class Solution:
    def findMin(self, arr: List[int]) -> int:
        #algozenith
        def check(arr, mid): 
            if arr[0] > arr[len(arr) - 1]:
                if arr[0] > arr[mid]: 
                    return  1 
                return 0                
            else:                   
                return 1
            

        l = 0 
        r = len(arr) - 1                    
        res = float("inf")
        while l <= r: 
            mid = (l  + r) // 2
            if check(arr, mid) == 1: 
                r = mid - 1
                res = arr[mid]
            else:   
                l = mid + 1         

        return res