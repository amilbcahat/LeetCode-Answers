class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Quick Sort(Not stable , inplace)
        # l , r = 0 , len(nums) - 1 


        # def quickSort(arr , l , r):
        #     # >= ensures that recursion stops  
        #     if l >= r : 
        #         return arr 

        #     pivot = arr[r]
        #     left = l 

        #     for i in range(l , r): 
        #         #Spot for pivot is left out 
        #         #Left pointer puts the less value than pivot at start 
        #         if arr[i] < pivot :
        #             tmp = arr[left]
        #             arr[left] = arr[i]
        #             arr[i] = tmp 
        #             left += 1 

        #     #Swap the pivot with left point , to partition the array 
        #     arr[r] = arr[left]
        #     arr[left] = pivot

        #     #Partition on basis of pivot and recursively sort them 
        #     quickSort(arr , l , left - 1)
        #     quickSort(arr , left + 1 , r)

        #     return arr 

        # return quickSort(nums , 0 , len(nums) - 1)


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