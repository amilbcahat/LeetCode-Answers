class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Merge Sort (Stable)
        def merge(arr , L  , M , R):
            left , right = arr[L : M + 1] , arr[M + 1 : R + 1]
            k , i , j = L , 0 , 0 

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else : 
                    arr[k] = right[j]
                    j += 1 
                k += 1 

            while i < len(left) : 
                arr[k] = left[i]
                i += 1 
                k += 1 
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        def mergeSort(arr , l , r):
            if l == r : 
                return arr 

            m = (l + r) // 2
            mergeSort(arr , l , m)
            mergeSort(arr , m+ 1, r)
            merge(arr , l , m , r)

            return arr 

        return mergeSort(nums , 0 , len(nums) - 1)

        
        #Insertion Sort (Stable)
        # for i in range(1 , len(nums)):
        #     j = i - 1
        #     while j >= 0 and nums[j + 1] < nums[j]:
        #         #tmp = a[j + 1]
        #         #a[j + 1] = a[j]
        #         #a[j] = tmp
        #         nums[j + 1] , nums[j] = nums[j] , nums[j + 1]
        #         j -= 1 

        # return nums